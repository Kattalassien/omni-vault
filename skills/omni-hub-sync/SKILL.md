---
name: omni-hub-sync
description: "Run Preston's Omni hub routines: knowledge sync (harvest BRAIN/ROADMAP from every repo, inject shared blocks by PR, mirror to Supabase, Drive and Notion), roadmap-to-Todoist next steps, and the monthly standards audit. Use for 'sync the hub', 'update Todoist from roadmaps', 'audit project standards'. Not for editing one repo's code."
license: MIT
metadata:
  author: Kattalassien
  version: "1.0"
  source: "github.com/Kattalassien/omni-vault/skills/omni-hub-sync"
  perplexity:
    connectors:
      - id: github_mcp_direct
        reason: Clone repos and open sync PRs with gh.
      - id: todoist
      - id: supabase
      - id: google_drive
      - id: notion_mcp
      - id: cloudinary
---

# Omni hub sync

The hub is `Kattalassien/omni-vault`. Config: `08-CONFIG/projects.json` (registry, Todoist IDs) and `08-CONFIG/automations.json` (modules, limits). Tool: `scripts/omnisync.py` (stdlib, dry-run unless `--apply`). Load `connector-router` for connector rules.

## Setup (every module)
1. Clone the hub and every registry repo that has a `repo` into one folder, using `gh repo clone <repo> <slug> -- --depth 1`.
2. Read `automations.json`. Skip a module whose `enabled` is false.
3. Run `python omni-vault/scripts/omnisync.py check --repos .` and keep the table for the summary.

## Module: knowledge_sync (weekly)
1. `harvest --repos . --apply`. Commit `10-SHARED/generated/` on branch `omni/sync-<date>` in omni-vault.
2. `inject --repos .`, a dry run. For each repo with a diff, up to `max_prs_per_run`: apply only for that repo with `--only <slug> --apply`, then branch `omni/shared-blocks-<date>` and open a PR with the label `omni-sync`. Skip a repo when an open `omni-sync` PR already exists; update that branch instead.
3. `bundle` and `sql`. Run each `build/kb-upsert-NN.sql` with Supabase `execute_sql`, then insert one `kb_sync_runs` row with counts.
4. Drive: update the files in the "Omni Knowledge Hub" folder (shared/, config/, projects/<slug>/). Update in place by fileId and never duplicate.
5. Notion: refresh the "Omni Projects" database rows (Next step, Last sync, Docs health) and the hub page's "Last sync" line.
6. Open or update one omni-vault PR with the generated files plus a LOG line. Never merge.

## Module: roadmap_to_todoist (weekdays)
1. Run `todoist --repos . --out build/todoist-plan.json`. Also read open rows from Supabase `public.roadmap_items` for projects that have no ROADMAP.md table.
2. For each project, find tasks in its `todoist.section_id` whose description contains `omni-key:`.
3. Add the missing planned tasks, keeping at most `max_open_per_project` open roadmap tasks per section. Complete the tasks whose key is in `close_keys`. Never edit tasks that have no `omni-key` line, because those are the user's own.
4. Owner `Human` gets the label `needs-you` and is listed first in the summary.

## Module: standards_audit (monthly)
Run `check --strict`, check that the CONTINUE.md date is no more than 30 days old, list open PRs older than 14 days, and run Supabase `get_advisors` (security). Add one Todoist task per failure, labelled `standard`, in that project's section. Dedupe by `omni-key: audit:<slug>:<check>`.

## Report (all modules)
Keep it under 150 words: a table of project, change and link, then "Needs you" items, then one bottom line. If nothing changed, say "No changes" in one line.
