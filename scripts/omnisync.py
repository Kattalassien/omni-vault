#!/usr/bin/env python3
"""omnisync - share Markdown knowledge across every project repo.

Hub-and-spoke model (chosen method, see 10-SHARED/README.md):
  * omni-vault is the hub. 10-SHARED/*-CORE.md are the canonical shared blocks.
  * `inject` writes those blocks into each repo between managed markers, so a
    repo's own notes are never touched.
  * `harvest` reads each repo's BRAIN facts, roadmap rows and planned features
    back into 10-SHARED/generated/, so BRAIN.md grows across every project.
  * `bundle` and `sql` produce mirrors for Supabase (kb_docs), Google Drive and
    Notion. Git stays the source of truth; mirrors are read models.

Standard library only. Every write is dry-run unless --apply is passed.
Never reads or prints secrets: files matching SECRET_PATTERNS are skipped.

Usage (from the omni-vault root):
  python scripts/omnisync.py check   --repos ../
  python scripts/omnisync.py harvest --repos ../ [--apply]
  python scripts/omnisync.py inject  --repos ../ [--only quick-console] [--apply]
  python scripts/omnisync.py bundle  --repos ../ --out build/knowledge-bundle.json
  python scripts/omnisync.py sql     --bundle build/knowledge-bundle.json --out build/kb-upsert.sql
  python scripts/omnisync.py todoist --repos ../ --out build/todoist-plan.json
"""
from __future__ import annotations

import argparse
import difflib
import fnmatch
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

VERSION = "1.0.0"
HUB = Path(__file__).resolve().parent.parent
REGISTRY = HUB / "08-CONFIG" / "projects.json"
AUTOMATIONS = HUB / "08-CONFIG" / "automations.json"
SHARED = HUB / "10-SHARED"
GENERATED = SHARED / "generated"

BLOCKS = {  # target file in each repo -> (block label, source file in hub)
    "BRAIN.md": ("core", SHARED / "BRAIN-CORE.md"),
    "AGENTS.md": ("agents", SHARED / "AGENTS-CORE.md"),
}
BEGIN = "<!-- omni:begin {label} v{ver} (managed by omni-vault/scripts/omnisync.py; edit the hub copy) -->"
BEGIN_RE = r"<!-- omni:begin {label}\b[^>]*-->"
END = "<!-- omni:end {label} -->"

DOC_GLOBS = ["*.md", "docs/**/*.md", "ai/**/*.md", "skills/**/*.md", "config/*.json",
             "[0-9][0-9]-*/**/*.md", "[0-9][0-9]-*/*.json", "[0-9][0-9]-*/*.yaml"]
SECRET_CONTENT = re.compile(r"(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}"
                            r"|-----BEGIN [A-Z ]*PRIVATE KEY|xox[bp]-[A-Za-z0-9-]{10,}|eyJ[A-Za-z0-9_-]{30,}\.[A-Za-z0-9_-]{20,})")
SECRET_PATTERNS = ["*.env", ".env*", "*secret*", "*credential*", "*token*", "*.pem", "*.key", "MASTER.env"]
MAX_DOC_BYTES = 200_000
DONE = {"done", "complete", "completed", "shipped", "merged", "closed", "verified"}
FACT_HEADINGS = ("facts learned", "decisions", "facts")


# ---------------------------------------------------------------- helpers
def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def registry(path: Path = REGISTRY) -> list[dict]:
    return load_json(path)["projects"]


def repo_dir(repos: Path, p: dict) -> Path | None:
    if p.get("slug") == "omni-vault":
        return HUB
    d = repos / (p.get("dir") or p["slug"])
    return d if d.is_dir() else None


def find_doc(root: Path, name: str, alts: list[str]) -> Path | None:
    for cand in [name, *alts]:
        f = root / cand
        if f.is_file():
            return f
    return None


DOC_ALTS = {
    "BRAIN.md": ["brain.md"],
    "ROADMAP.md": ["roadmap.md", "01-ROADMAP/ROADMAP.md", "IMPLEMENTATION-ROADMAP.md", "PLAN.md"],
    "CHANGELOG.md": ["99-LOG/CHANGELOG.md"],
    "PLANNEDFEATURES.md": ["docs/PLANNEDFEATURES.md"],
    "CONTINUE.md": ["06-PROMPTS/CONTINUATION-PROMPT.md", "docs/project/SESSION-HANDOFF.md"],
    "AGENTS.md": ["CLAUDE.md"],
}


def show_diff(path: Path, old: str, new: str) -> None:
    sys.stdout.writelines(difflib.unified_diff(
        old.splitlines(True), new.splitlines(True), f"a/{path.name}", f"b/{path.name}"))


def write(path: Path, new: str, apply: bool, label: str = "") -> bool:
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if old == new:
        return False
    if apply:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(new, encoding="utf-8")
        print(f"wrote {label or path}")
    else:
        print(f"--- dry-run: would change {label or path}")
        show_diff(path, old, new)
    return True


def slug_key(slug: str, ref: str | None, text: str) -> str:
    if ref:
        return f"{slug}:{ref}"
    return f"{slug}:{hashlib.sha1(text.encode()).hexdigest()[:8]}"


# ---------------------------------------------------------------- managed blocks
def render_block(label: str, body: str) -> str:
    return f"{BEGIN.format(label=label, ver=VERSION.split('.')[0])}\n{body.strip()}\n{END.format(label=label)}"


def upsert_block(text: str, label: str, body: str) -> str:
    block = render_block(label, body)
    pat = re.compile(BEGIN_RE.format(label=re.escape(label)) + r".*?" + re.escape(END.format(label=label)), re.S)
    if pat.search(text):
        return pat.sub(lambda _m: block, text, count=1)
    lines = text.splitlines()
    i = 0
    if lines and lines[0].strip() == "---":  # skip YAML frontmatter
        i = next((n + 1 for n in range(1, len(lines)) if lines[n].strip() == "---"), 0)
    h1 = next((n for n in range(i, len(lines)) if lines[n].startswith("# ")), None)
    at = (h1 + 1) if h1 is not None else i
    rest = lines[at:]
    while rest and not rest[0].strip():
        rest = rest[1:]
    out = lines[:at] + ["", block, ""] + rest
    return "\n".join(out).rstrip() + "\n"


# ---------------------------------------------------------------- parsing
def md_tables(text: str):
    """Yield (headers, rows) for every pipe table."""
    lines = text.splitlines()
    i = 0
    while i < len(lines) - 1:
        if lines[i].strip().startswith("|") and re.match(r"^\s*\|?\s*:?-{3,}", lines[i + 1]):
            hdr = [c.strip().lower() for c in lines[i].strip().strip("|").split("|")]
            rows, i = [], i + 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            yield hdr, rows
        else:
            i += 1


def roadmap_items(slug: str, text: str) -> list[dict]:
    items: list[dict] = []
    for hdr, rows in md_tables(text):
        if "status" not in hdr:
            continue
        col = {h: n for n, h in enumerate(hdr)}
        title_col = next((col[c] for c in ("item", "title", "scope", "task", "work") if c in col), None)
        if title_col is None:
            continue
        for r in rows:
            get = lambda k: r[col[k]] if k in col and col[k] < len(r) else ""  # noqa: E731
            title = r[title_col] if title_col < len(r) else ""
            if not title:
                continue
            ref = get("ref") or get("id") or (f"P{get('phase')}" if get("phase") else "")
            status = get("status").lower()
            items.append({
                "key": slug_key(slug, ref or None, title), "project": slug, "ref": ref,
                "phase": get("phase"), "title": title, "status": status,
                "owner": get("owner") or "", "open": not any(d in status for d in DONE),
                "source": "roadmap",
            })
    for m in re.finditer(r"^\s*[-*] \[( |x|X)\] (.+)$", text, re.M):
        title = m.group(2).strip()
        items.append({"key": slug_key(slug, None, title), "project": slug, "ref": "", "phase": "",
                      "title": title, "status": "done" if m.group(1).lower() == "x" else "todo",
                      "owner": "", "open": m.group(1) == " ", "source": "checklist"})
    return items


def brain_facts(text: str) -> list[str]:
    facts, take = [], False
    for line in text.splitlines():
        if line.startswith("## "):
            take = line[3:].strip().lower().startswith(FACT_HEADINGS)
            continue
        if take and line.lstrip().startswith(("- ", "* ")):
            facts.append(line.strip()[2:])
    return facts


def rank(item: dict) -> tuple:
    """Order open items: in progress/next, then todo, then in review, then blocked; P0 before P3."""
    s = item["status"]
    order = 0 if ("progress" in s or "next" in s) else 1 if ("todo" in s or not s) else 2 if "review" in s else 3
    prio = int(item["priority"][1]) if re.fullmatch(r"[Pp][0-4]", item.get("priority") or "") else 2
    return (order, prio)


# ---------------------------------------------------------------- commands
def cmd_check(a) -> int:
    reg, missing_total = registry(a.registry), 0
    required = load_json(a.registry).get("requiredDocs", [])
    rows = ["| Project | Repo found | Missing docs | Shared block |", "|---|---|---|---|"]
    for p in reg:
        d = repo_dir(a.repos, p)
        if not p.get("repo"):
            rows.append(f"| {p['slug']} | no repo (planned) | - | - |")
            continue
        if d is None:
            rows.append(f"| {p['slug']} | not cloned | ? | ? |")
            continue
        miss = [doc for doc in required if find_doc(d, doc, DOC_ALTS.get(doc, [])) is None]
        brain = find_doc(d, "BRAIN.md", DOC_ALTS["BRAIN.md"])
        has_block = bool(brain and re.search(BEGIN_RE.format(label="core"), brain.read_text(encoding="utf-8")))
        missing_total += len(miss)
        rows.append(f"| {p['slug']} | yes | {', '.join(miss) or 'none'} | {'yes' if has_block else 'no'} |")
    print("\n".join(rows))
    return 1 if (a.strict and missing_total) else 0


def extra_items(path: Path | None) -> dict[str, list[dict]]:
    """Rows exported from Supabase public.roadmap_items (JSON list) merged as a second source."""
    out: dict[str, list[dict]] = {}
    if not path:
        return out
    for r in load_json(path) if path.suffix == ".json" else []:
        notes = r.get("notes") or ""
        m = re.search(r"owner:\s*([A-Za-z]+)", notes)
        owner = m.group(1) if m else ("Human" if r.get("needs_human") else "")
        status = (r.get("status") or "todo").lower()
        out.setdefault(r["project_slug"], []).append({
            "key": slug_key(r["project_slug"], r.get("ref") or None, r["title"]), "project": r["project_slug"],
            "ref": r.get("ref") or "", "phase": r.get("phase") or "", "title": r["title"], "status": status,
            "owner": owner, "open": not any(d in status for d in DONE), "source": "supabase",
            "priority": r.get("priority") or ""})
    return out


def collect(a) -> dict:
    data = {"generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), "projects": []}
    extra = extra_items(getattr(a, "extra", None))
    for p in registry(a.registry):
        d = repo_dir(a.repos, p)
        entry = {**p, "cloned": d is not None, "facts": [], "items": []}
        if d:
            for doc in ("ROADMAP.md", "PLANNEDFEATURES.md"):
                f = find_doc(d, doc, DOC_ALTS.get(doc, []))
                if f:
                    entry["items"] += roadmap_items(p["slug"], f.read_text(encoding="utf-8"))
            b = find_doc(d, "BRAIN.md", DOC_ALTS["BRAIN.md"])
            if b:
                entry["facts"] = brain_facts(b.read_text(encoding="utf-8"))
        entry["items"] += extra.get(p["slug"], [])
        seen, uniq = set(), []
        for it in entry["items"]:
            if it["key"] not in seen:
                seen.add(it["key"])
                uniq.append(it)
        entry["items"] = uniq
        data["projects"].append(entry)
    return data


def cmd_harvest(a) -> int:
    data = collect(a)
    stamp = data["generated"]
    brain = [f"# BRAIN-ALL (generated {stamp})", "",
             "Durable facts harvested from every project's BRAIN.md (`## Facts learned` / `## Decisions`).",
             "Do not edit here; edit the project's BRAIN.md and rerun `omnisync.py harvest`.", ""]
    road = [f"# ROADMAP-ALL (generated {stamp})", "", "| Project | Ref | Item | Status | Owner |", "|---|---|---|---|---|"]
    nxt = {"generated": stamp, "projects": {}}
    limit = a.limit or load_json(AUTOMATIONS)["modules"]["roadmap_to_todoist"]["max_open_per_project"] \
        if AUTOMATIONS.exists() else (a.limit or 3)
    for p in data["projects"]:
        brain += [f"## {p['name']} ({p['slug']})", *(f"- {f}" for f in p["facts"][-15:])] if p["facts"] \
            else [f"## {p['name']} ({p['slug']})", "- TODO: no BRAIN.md facts yet"]
        brain.append("")
        for it in p["items"]:
            road.append(f"| {p['slug']} | {it['ref']} | {it['title'].replace('|', '/')} | {it['status']} | {it['owner']} |")
        open_items = sorted((i for i in p["items"] if i["open"]), key=rank)[:limit]
        nxt["projects"][p["slug"]] = open_items
    nmd = [f"# NEXT-STEPS (generated {stamp})", "", f"Top {limit} open roadmap items per project. Synced to Todoist.", ""]
    for slug, items in nxt["projects"].items():
        nmd.append(f"## {slug}")
        nmd += [f"- [ ] {i['title']} ({i['status'] or 'todo'}{', ' + i['owner'] if i['owner'] else ''}) `{i['key']}`"
                for i in items] or ["- nothing open"]
        nmd.append("")
    changed = False
    changed |= write(GENERATED / "BRAIN-ALL.md", "\n".join(brain).rstrip() + "\n", a.apply)
    changed |= write(GENERATED / "ROADMAP-ALL.md", "\n".join(road) + "\n", a.apply)
    changed |= write(GENERATED / "NEXT-STEPS.md", "\n".join(nmd).rstrip() + "\n", a.apply)
    changed |= write(GENERATED / "next-steps.json", json.dumps(nxt, indent=2) + "\n", a.apply)
    print("harvest:", "changes" if changed else "no changes", "" if a.apply else "(dry-run)")
    return 0


def cmd_inject(a) -> int:
    n = 0
    for p in registry(a.registry):
        if a.only and p["slug"] not in a.only:
            continue
        d = repo_dir(a.repos, p)
        if d is None or p["slug"] == "omni-vault" or not p.get("repo"):
            continue
        for target, (label, src) in BLOCKS.items():
            f = find_doc(d, target, [x for x in DOC_ALTS.get(target, []) if x.lower() == target.lower()]) or (d / target)
            if not f.exists() and not a.create:
                print(f"skip {p['slug']}/{target}: missing (use --create)")
                continue
            body = src.read_text(encoding="utf-8").replace("{{project}}", p["name"].split(" (")[0]).replace("{{slug}}", p["slug"])
            old = f.read_text(encoding="utf-8") if f.exists() else f"# {target[:-3]} ({p['name']})\n"
            n += write(f, upsert_block(old, label, body), a.apply, f"{p['slug']}/{f.name}")
    print(f"inject: {n} file(s) {'changed' if a.apply else 'would change'}")
    return 0


def secret_like(rel: str) -> bool:
    name = Path(rel).name.lower()
    return any(fnmatch.fnmatch(name, pat.lower()) for pat in SECRET_PATTERNS)


def cmd_bundle(a) -> int:
    docs = []
    for p in registry(a.registry):
        d = repo_dir(a.repos, p)
        if d is None:
            continue
        files = sorted({f for g in DOC_GLOBS for f in d.glob(g) if f.is_file()})
        for f in files:
            rel = f.relative_to(d).as_posix()
            if secret_like(rel) or "node_modules" in rel or f.stat().st_size > MAX_DOC_BYTES:
                continue
            text = f.read_text(encoding="utf-8", errors="replace")
            if SECRET_CONTENT.search(text):
                print(f"skip {p['slug']}/{rel}: looks like it contains a secret", file=sys.stderr)
                continue
            kind = "config" if f.suffix in (".json", ".yaml", ".yml") else "prompt" if "PROMPTS" in rel else \
                "skill" if rel.startswith("skills/") or "/skills/" in rel else "generated" if "generated/" in rel else \
                "operating-doc" if f.name.upper() in {x.upper() for x in BLOCKS} | {
                    "ROADMAP.MD", "CHANGELOG.MD", "PLANNEDFEATURES.MD", "CONTINUE.MD"} else "doc"
            docs.append({"project_slug": p["slug"], "path": rel, "kind": kind, "bytes": len(text.encode()),
                         "sha256": hashlib.sha256(text.encode()).hexdigest(), "content": text})
    out = {"generated": datetime.now(timezone.utc).isoformat(timespec="seconds"), "version": VERSION, "docs": docs}
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"bundle: {len(docs)} docs, {sum(x['bytes'] for x in docs)} bytes -> {a.out}")
    return 0


def dq(s: str) -> str:
    """Dollar-quote a string with a tag that cannot occur inside it."""
    tag = "kb"
    while f"${tag}$" in s:
        tag += "x"
    return f"${tag}${s}${tag}$"


def cmd_sql(a) -> int:
    b = load_json(a.bundle)
    stmts = []
    for d in b["docs"]:
        stmts.append(
            "insert into public.kb_docs (project_slug,path,kind,bytes,sha256,content,source,synced_at) values "
            f"({dq(d['project_slug'])},{dq(d['path'])},{dq(d['kind'])},{d['bytes']},{dq(d['sha256'])},"
            f"{dq(d['content'])},'omnisync',now()) on conflict (project_slug,path) do update set "
            "kind=excluded.kind,bytes=excluded.bytes,sha256=excluded.sha256,content=excluded.content,"
            "synced_at=now() where public.kb_docs.sha256 is distinct from excluded.sha256;")
    chunks, cur = [], []
    for s in stmts:  # keep each file under ~120 KB so connector calls stay small
        if sum(len(x) for x in cur) + len(s) > 120_000 and cur:
            chunks.append(cur)
            cur = []
        cur.append(s)
    if cur:
        chunks.append(cur)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    for n, c in enumerate(chunks, 1):
        path = a.out.with_name(f"{a.out.stem}-{n:02d}{a.out.suffix}")
        path.write_text("\n".join(c) + "\n", encoding="utf-8")
        print(f"sql: {path} ({len(c)} statements)")
    return 0


def cmd_todoist(a) -> int:
    """Plan (never call) Todoist changes: one section per project, tasks keyed by omni-key."""
    cfg = load_json(AUTOMATIONS)["modules"]["roadmap_to_todoist"] if AUTOMATIONS.exists() else {}
    a.limit = a.limit or cfg.get("max_open_per_project", 3)
    data = collect(a)
    plan = {"generated": data["generated"], "mode": cfg.get("mode", "sections"),
            "hub_project": cfg.get("hub_project", "Dev Projects"), "sections": []}
    owner_labels = cfg.get("owner_labels", {})
    for p in data["projects"]:
        if p.get("status") == "archived":
            continue
        items = sorted((i for i in p["items"] if i["open"]), key=rank)[: a.limit]
        plan["sections"].append({
            "project": p["slug"], "section": p.get("todoist", {}).get("section") or p["name"],
            "tasks": [{"content": f"[{p['slug']}] {i['title']}"[:240],
                       "description": f"omni-key: {i['key']}\nsource: {i['source']} ({i['status'] or 'todo'})",
                       "labels": [x for x in (cfg.get("always_label", "roadmap"), owner_labels.get(i["owner"].lower(), "")) if x],
                       "section_id": p.get("todoist", {}).get("section_id"),
                       "project_id": p.get("todoist", {}).get("project_id"),
                       "priority": {"P0": "p1", "P1": "p2"}.get(i.get("priority", ""), "p3")}
                      for i in items],
            "close_keys": [i["key"] for i in p["items"] if not i["open"]],
        })
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(plan, indent=2), encoding="utf-8")
    print(f"todoist plan: {sum(len(s['tasks']) for s in plan['sections'])} tasks in {len(plan['sections'])} sections -> {a.out}")
    return 0


def parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="omnisync", description=__doc__.split("\n")[0])
    ap.add_argument("--version", action="version", version=VERSION)
    ap.add_argument("--registry", type=Path, default=REGISTRY)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def add(name, fn, **kw):
        s = sub.add_parser(name)
        s.add_argument("--repos", type=Path, default=HUB.parent, help="folder that holds the cloned repos")
        s.set_defaults(fn=fn)
        for k, v in kw.items():
            s.add_argument(f"--{k.replace('_', '-')}", **v)
        return s

    add("check", cmd_check, strict={"action": "store_true"})
    extra = {"type": Path, "default": None, "help": "JSON export of Supabase roadmap_items"}
    add("harvest", cmd_harvest, apply={"action": "store_true"}, limit={"type": int, "default": 0}, extra=extra)
    add("inject", cmd_inject, apply={"action": "store_true"}, create={"action": "store_true"},
        only={"nargs": "*", "default": []})
    add("bundle", cmd_bundle, out={"type": Path, "default": HUB / "build" / "knowledge-bundle.json"})
    add("sql", cmd_sql, bundle={"type": Path, "default": HUB / "build" / "knowledge-bundle.json"},
        out={"type": Path, "default": HUB / "build" / "kb-upsert.sql"})
    add("todoist", cmd_todoist, out={"type": Path, "default": HUB / "build" / "todoist-plan.json"},
        limit={"type": int, "default": 0}, extra=extra)
    return ap


def main(argv: list[str] | None = None) -> int:
    a = parser().parse_args(argv)
    a.repos = a.repos.resolve()
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
