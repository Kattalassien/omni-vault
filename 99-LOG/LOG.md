# Operations Log (append only, newest first)

What agents and automations did, when, and the result. CHANGELOG.md records what changed in the vault; this file records the work and checks behind it.

Format: `YYYY-MM-DD HH:MM ET | actor | action | result`

## 2026-10-04
- 01:34 | Computer | Created 4 twice-weekly gaming digests (BG3, Souls, Pokémon, Persona) | Active
- 01:52 | Computer | Merged into one Daily Gaming Digest (9:00 AM ET); Persona slot became "up to 10 extra games" | Active, id b82806e0
- 01:53 | Computer | Deleted the 3 now-redundant digests (no runs had happened) | Deleted
- 01:53 | Computer | Steam lookup: YungFloop profile public, game details private; ChaosJim and lpmcgee have no public custom URL | Partial
- 01:53 | Computer | PS5: no Sony connector or public API; needs PSN ID + PSNProfiles | Blocked on human
- 01:54 | Computer | Connector health check: 13 of 14 OK, Google Photos limited by API | See 05-CONNECTORS
- 01:54 | Computer | Supabase advisors (omnitask-portal): 1 info (admin_emails RLS without policy), 2 warn (SECURITY DEFINER is_admin, portal_tables callable by signed-in users) | Logged, not changed
- 01:55 | Computer | Drive scan: found duplicate versions (BRAIN.md x2, Gemini setup x5, skills x2 each, MASTER.env x2) and a credential-dump archive at Drive root | Listed in 09-MASTER-PLANS/MASTER-MERGE-PLAN.md
- 01:56 | Computer | Added BRAIN.md, ROADMAP.md, LOG.md, config.yaml, master plans; PR opened | Not merged

## 2026-10-04 (omni hub sync)
- 03:40 | Computer | Todoist Free hit the project cap; archived empty "Movies to watch" and created "Dev Projects" (board) with 13 project sections plus 6 labels | Done (unarchive anytime: Settings > Archived)
- 03:45 | Computer | Moved 42 project-tagged tasks from Knowledge OS into their project sections and added owner labels; added 9 new roadmap tasks keyed by omni-key | Ledger in PR description
- 03:46 | Computer | Todoist saved filters: blocked by the Free plan filter cap | Use label views instead
- 03:47 | Computer | Supabase migration kb_mirror (kb_docs, kb_sync_runs, kb_project_summary view, roadmap ref index) on omnitask-portal; advisors show only the same 3 older items | Done
- 03:48 | Computer | Cloudinary: uploaded omni-hub/hub/omni-hub-diagram and omni-hub/base/card-base; 15 transformation-based project cards return 200 | Done
- 03:50 | Computer | Added 10-SHARED, omnisync.py (8 tests), hub-check CI, skills, operator prompt v2, automations.json | PR opened, not merged
