# Project standards (v1, 2026-10-04)

Each project in `08-CONFIG/projects.json` follows this contract. `omnisync.py check` and the monthly "Omni standards audit" automation check it.

## Files
| File | Purpose | Rule |
|---|---|---|
| BRAIN.md | Durable facts | Contains the `omni:begin core` block. Project facts go under `## Facts learned`, one dated bullet each |
| ROADMAP.md | Plan | A pipe table with `Ref`, `Item`, `Status` and `Owner` columns, or `Phase`, `Scope` and `Status`. Status is one of: todo, next, in progress, in review, blocked, done. Anything that contains "verified" also counts as done |
| CHANGELOG.md | History | Newest first. Keep a Changelog headings |
| PLANNEDFEATURES.md | Ideas | `- [ ]` checkboxes. The open ones feed Todoist |
| CONTINUE.md | Handoff | State, next 3 actions, open PRs, and a paste-ready continuation prompt |
| AGENTS.md | AI rules | Contains the `omni:begin agents` block. CLAUDE.md and copilot-instructions point here |

## Change rules
- Use a branch `omni/<topic>` or `feat|fix|docs/<topic>`. Open one PR per concern, under about 600 lines. Never merge without Preston.
- Preview before apply, everywhere: `--dry-run`, `-WhatIf`, or a printed diff.
- Use a log line in the format `YYYY-MM-DD HH:MM ET | actor | action | result`. Add it to omni-vault `99-LOG/LOG.md`.
- Secrets: names only. Keep them in the password manager, Supabase secrets, or GitHub secrets.

## Todoist mapping
- Each project gets a section of **Dev Projects**, because Todoist Free caps projects. omni-vault maps to **Knowledge OS > Computer**, and pokerogue-mods to its own project.
- Each roadmap row that is not done becomes a task named `[slug] Item`. Its description starts with `omni-key: <slug>:<ref>`, and the sync uses that line to dedupe.
- Labels: `roadmap` always. The owner label is `needs-you`, `computer`, `copilot` or `claude`. Audit findings get `standard`.
- At most 3 open roadmap tasks per project (`08-CONFIG/automations.json`). When a roadmap row turns done, its task is completed.

## Mirrors (read models; git wins on conflict)
| Mirror | Where | Updated by |
|---|---|---|
| Supabase | `public.kb_docs`, `public.kb_sync_runs`, `public.roadmap_items` (omnitask-portal) | knowledge_sync |
| Google Drive | Folder "Omni Knowledge Hub" (shared/, config/, projects/<slug>/) | knowledge_sync |
| Notion | Page "Omni Knowledge Hub" under "Preston Master Automation & Knowledge OS" | knowledge_sync |
| Cloudinary | `omni-hub/` folder: hub diagram, project cards | knowledge_sync (check only) |
| Perplexity | Project "Knowledge OS and Vault" files and Project Brain | Project wiki refresh |
