# Tech harvest: at least 3 useful pieces from each repo (2026-10-04)

"Adopted in" shows where the idea now lives in the hub system.

| Repo | Technique | Adopted in |
|---|---|---|
| omnitask-portal | 1 docsctl.py: idempotent edits, dry-run diffs, session close-out | omnisync `write()` dry-run diff |
| | 2 docs-health.mjs as a CI gate | `.github/workflows/hub-check.yml` |
| | 3 RLS `is_admin()` on every table | `kb_docs`, `kb_sync_runs` migration |
| | 4 Config registry `config/projects.json` | `08-CONFIG/projects.json` |
| omnitask-mobile | 1 AGENTS.md canonical, with CLAUDE/Copilot pointers | AGENTS-CORE block |
| | 2 Risk-prioritized diff truncation in AI review | connector-router cost rules (trim before sending) |
| | 3 Playwright smoke tests as acceptance | standards audit "evidence" rule |
| | 4 Brain Bot fact capture into BRAIN.md | `## Facts learned` harvest |
| quick-console | 1 Audit, then preview, then apply | every automation step |
| | 2 Layered config (defaults, user, machine) | automations.json defaults plus modules |
| | 3 Name-collision detection before adding commands | skill and automation names are checked before create |
| steamdeck-ops | 1 `run()` that honors `--dry-run` | omnisync `--apply` |
| | 2 `step()` with keep-going result ledger | automation run summary rows |
| | 3 Config-file overrides (deckops.conf) | automations.json limits editable on phone |
| cjg-chaosjimgen | 1 Data contract with provenance fields | `kb_docs.sha256`, `source`, `synced_at` |
| | 2 Supabase views for summaries | `kb_project_summary` view |
| | 3 User ratings separate from model scores | "Needs you" tasks stay separate from agent tasks |
| consent-first-ai-lab | 1 skills/ folders with SKILL.md | `omni-vault/skills/` |
| | 2 Versioned hard-boundary brain | `omni:begin core v1` markers |
| | 3 reviews/ baseline before change | standards_audit baseline |
| omnitool-knowledge (was llm-knowledge-base) | 1 agents.json retry policy and priority queues | automations retry once, then log |
| | 2 HMAC-signed webhooks with backoff | future portal ingest of sync runs |
| | 3 tools/*.md per AI tool | PERPLEXITY-PLAYBOOK.md |
| omni-vault | 1 work-packages.json (owner, depends, acceptance) | Todoist task description fields |
| | 2 Token-saving playbook | connector-router "cheapest tool first" |
| | 3 Append-only LOG line format | every automation logs one line |
| job-automation-suite | 1 Monorepo packages (core, connectors, llm, automation) | modular automation design |
| | 2 `jobs.config.example.json` (example config, no secrets) | automations.json has no secrets |
| | 3 Human-in-the-loop submit | approval gates |
| emerald-companion | 1 Bridge and relay split (game, then local relay, then web) | portal runner pattern |
| | 2 sym2profile.py generator | generated/ files never hand-edited |
| | 3 tests/ beside tools | tests/test_omnisync.py |
| pokerogue-mods | 1 originals/ kept beside mods/ (diffable patches) | managed blocks keep repo text untouched |
| | 2 Userscript menu | Brain Bot / Stay capture |
| | 3 test/ harness for a userscript | hub-check CI |
