# Vault Changelog (append only, newest first)

## 2026-10-04 (omni hub sync)
- Added 10-SHARED/: three sharing methods compared, with hub plus managed blocks chosen. Added BRAIN-CORE and AGENTS-CORE blocks, STANDARDS, SKILLS, AGENTS, FEATURES, CONNECTORS, PERPLEXITY-PLAYBOOK, TECH-HARVEST (3+ techniques per repo), and generated BRAIN-ALL / ROADMAP-ALL / NEXT-STEPS.
- Added scripts/omnisync.py (stdlib; check, harvest, inject, bundle, sql, todoist), tests/test_omnisync.py, and .github/workflows/hub-check.yml.
- Added 08-CONFIG/projects.json (hub registry with Todoist IDs and Cloudinary cards) and 08-CONFIG/automations.json (three modular automations).
- Added 06-PROMPTS/PERPLEXITY-OPERATOR-PROMPT.md v2, covering Projects, Skills, Automations, Agents, Model Council, Artifacts and Memory.
- Added skills/connector-router and skills/omni-hub-sync (source copies of the Perplexity skills).
- Mirrors: Supabase kb_docs, Drive "Omni Knowledge Hub", Notion "Omni Knowledge Hub", Cloudinary omni-hub/, Todoist "Dev Projects".

## 2026-10-04 (admin pass)
- Added BRAIN.md (canonical shared memory, with how-to-use notes), 01-ROADMAP/ROADMAP.md (one-screen view), 08-CONFIG/config.yaml (non-secret IDs, extra games list, connector status), 99-LOG/LOG.md (operations log).
- Added 09-MASTER-PLANS: MIND-MAP.md, SCHEDULE.md, MASTER-MERGE-PLAN.md (plan 1), TOOL-MASTERY-PLAN.md (plan 2).
- Connector health check recorded in 05-CONNECTORS/CONNECTORS.md.
- Daily Gaming Digest replaces four twice-weekly digests.
- Drive BRAIN.md copies (2) now point to the vault copy.

## 2026-10-01 (cost review)
- Added 07-COST/TOKEN-SAVING-PLAYBOOK.md: 20 methods from Reddit and GitHub, routing table, adopted rules.
- Project instructions: added handoff rule (about 10 messages or an hour).

## 2026-10-01 (later)
- Portal MVP built, QA-verified on live Supabase, pushed to Kattalassien/omnitask-portal; preview deployed.
- Docs PRs opened in omnitask-mobile (#10), llm-knowledge-base (#6), cjg-chaosjimgen (#3), emerald-companion (#1), pokemon-unbound-mod-workspace (#2). Nothing merged.
- Todoist board populated (34 tasks); Drive backup folder created (35 files).
- Found repo pokerogue-mods (not yet reviewed).

## 2026-10-01
- Created omni-vault: master plan, outsource board (38 work packages), file digest, iPhone guides, connector guide, project index, prompts.
- Reorganized Perplexity Projects (renamed 3, created 2, moved website thread, rewrote OmniTask Mobile instructions).
- Verified Google Photos connector sees only app-created media (empty list).
- Left out a private personal reminder from the digest.
- Created steamdeck-ops repo (PR #1 script+CI, PR #2 runbook); portal SD-1..SD-8 rows; mobile docs/steam-deck.md PR; Notion/Todoist/Drive mirrors.
