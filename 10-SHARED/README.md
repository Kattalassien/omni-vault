# 10-SHARED: knowledge that every project shares

This folder lets BRAIN.md, AGENTS.md, SKILLS.md, FEATURES.md and CONNECTORS.md grow across every repo instead of drifting apart.

## Three ways we could share Markdown across projects

| | A. Hub + managed blocks (chosen) | B. Git submodule or subtree | C. Database as source of truth |
|---|---|---|---|
| How | omni-vault holds the canonical blocks. `scripts/omnisync.py inject` writes them into each repo between `<!-- omni:begin ... -->` markers. `harvest` pulls each repo's facts and roadmap back into `generated/`. | Each repo mounts `omni-vault/10-SHARED` as `.omni/` | Supabase `kb_docs` is canonical; Markdown is rendered from it |
| Works on iPhone | Yes. Every file is plain Markdown on GitHub mobile | Poor. Submodules show as links, and editing needs a PC | Only through the portal UI |
| Repo stays readable alone | Yes. The block is copied in | No. Content lives elsewhere | No. Files are generated |
| Two-way growth | Yes. Push shared, pull facts | One way | Yes, but needs an editor |
| Failure mode | A stale block until the next sync PR | Detached HEADs, auth in CI | Database outage or lost edits |
| Tooling | Python stdlib plus the weekly automation | git only | SQL, edge functions |

Favorite: A. It keeps git as the source of truth and works from a phone. It follows the patterns we already trust: docsctl.py idempotent edits, QuickConsole preview-then-apply, and PR-only changes. B and C are not thrown away. C becomes a read model: `kb_docs` in Supabase, mirrored to Drive and Notion so the portal and phone can search everything. The Perplexity Project knowledge (Project Brain) of "Knowledge OS and Vault" is a fourth, automatic layer.

## Files

| File | Role | Edited by |
|---|---|---|
| BRAIN-CORE.md | Shared block injected into every repo's BRAIN.md | Hub PR |
| AGENTS-CORE.md | Shared block injected into every repo's AGENTS.md | Hub PR |
| STANDARDS.md | Project contract: docs, branches, logs, Todoist mapping | Hub PR |
| SKILLS.md | Every skill (Perplexity, repo, Copilot) in one catalog | Hub PR |
| AGENTS.md | Every agent and who does what | Hub PR |
| FEATURES.md | Cross-project feature inventory | Hub PR |
| CONNECTORS.md | Connector routing and cost rules | Hub PR |
| PERPLEXITY-PLAYBOOK.md | Projects, Skills, Automations, Agents, Artifacts, Memory | Hub PR |
| TECH-HARVEST.md | 3+ reusable techniques from every repo | Hub PR |
| generated/ | BRAIN-ALL, ROADMAP-ALL, NEXT-STEPS (do not hand-edit) | omnisync.py |

## Run it

```bash
# all repos cloned side by side, e.g. ~/dev/<repo>
python scripts/omnisync.py check   --repos ..            # docs contract table
python scripts/omnisync.py harvest --repos .. --apply    # grow generated/BRAIN-ALL.md
python scripts/omnisync.py inject  --repos ..            # dry-run diff of shared blocks
python scripts/omnisync.py inject  --repos .. --only quick-console --apply
python scripts/omnisync.py bundle  --repos .. && python scripts/omnisync.py sql   # Supabase upsert files
python scripts/omnisync.py todoist --repos ..            # Todoist plan JSON (no API calls)
```

On iPhone you never run this. The weekly "Omni knowledge sync" automation runs it and opens PRs for you to approve.
