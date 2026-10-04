---
id: roadmap
type: roadmap
status: active
updated: 2026-10-04
---
# ROADMAP (short view)

The full list of asks and workstreams is in MASTER-PLAN.md; tasks with owners are in OUTSOURCE-BOARD.md. This file is the one-screen "what's next" view for iPhone.

## Now (this week)
| # | Item | Owner | Done when |
|---|---|---|---|
| 1 | Review and merge omni-vault PR "admin pass 2026-10-04" | Human | Merged on GitHub mobile |
| 2 | Steam: Privacy > Game details = Public (YungFloop) | Human | Digest shows recently played PC games |
| 3 | Add PSN ID to 08-CONFIG/config.yaml and make PSNProfiles page public | Human | PS5 games appear in digest |
| 4 | Answer the strategy example question (09-MASTER-PLANS/TOOL-MASTERY-PLAN.md, section "Your example") | Human | First strategy recorded |
| 5 | Security: remove the credential-dump archive from Drive root and rotate anything in MASTER.env if exposed | Human | File gone; keys rotated |
| 6 | Supabase: fix 3 advisor findings on omnitask-portal (PR only) | Computer -> Human | Advisors clean |
| 7 | Merge omnitask-mobile PRs #8 then #9 (carried over) | Human | Merged |

## Next (2 to 4 weeks)
- Master Merge Plan phases 1 to 3 (09-MASTER-PLANS/MASTER-MERGE-PLAN.md).
- Sentry: create one project for omnitask-portal and one for omnitask-mobile once deployed.
- Move PokéVoid plan/roadmap/changelog from Drive root into the pokerogue-mods repo.
- Weekly "vault gardener" automation (proposed in SCHEDULE.md), only after you approve it.

## Later
- Knowledge schema with pgvector in Supabase (Workstream C Phase 2).
- Tool Mastery playbooks filled per connector (09-MASTER-PLANS/TOOL-MASTERY-PLAN.md).
- Manga pipeline repo, Job suite Step 2, Beans & Roots changes (Jim approves).

## Workstream added 2026-10-04
### M Media and Game Lab: Daily Gaming Digest
Live. One daily report: BG3 (PS5 console mods first), Elden Ring and Dark Souls, Pokémon and ROM hacks, and up to 10 extra games read from config.yaml plus Steam recently played (once public).

## Hub sync track (added 2026-10-04)
| Ref | Item | Status | Owner |
|---|---|---|---|
| HUB-1 | Review and merge the omni-hub-sync PR (10-SHARED, omnisync.py, skills, automations config) | todo | Human |
| HUB-2 | Review the quick-console pilot PR (shared blocks + AGENTS.md) | todo | Human |
| HUB-3 | Roll shared blocks into the remaining repos (weekly sync opens up to 5 PRs per run) | todo | Computer |
| HUB-4 | Add the five operating docs to repos that are missing them (see `omnisync.py check`) | todo | Copilot |
| HUB-5 | Portal "Knowledge" tab that reads kb_docs and kb_project_summary | todo | Copilot |
| HUB-6 | Decide on a Todoist Pro upgrade (switches folders from sections to real projects; mode in automations.json) | todo | Human |
