---
id: master-plan
type: roadmap
status: active
updated: 2026-10-01
---
# Master Plan

Built from every request in recent conversations. Each ask is grouped into a workstream; each workstream has work packages in OUTSOURCE-BOARD.md.

## Operating principles (apply everywhere)
1. iPhone-first: every human step must be doable from Safari, GitHub mobile, Shortcuts or a phone call to a tool.
2. Free first: OpenRouter free models, free tiers (Supabase, Cloudflare Pages, GitHub Actions). Ask before anything that bills.
3. Markdown is canonical; Supabase indexes and syncs; GitHub holds code and docs; Drive holds backups and big files; Todoist holds tasks.
4. Checkpoints: one PR per concern, under ~600 changed lines, never merge without the owner, no secrets in files or logs, no invented facts.
5. PC (remote desktop) only for work a cloud box cannot do: GPU/ComfyUI, emulators, heavy builds, USB to iPhone.

## Every user ask, grouped
| # | Ask (source) | Workstream |
|---|---|---|
| 1 | Turn omnitask-mobile into a deployable app, no Replit, AWS or free host, one feature at a time (Sep 5) | A OmniTask Mobile |
| 2 | Cygwin installer, tmux, noctty "like Warp" on PC (Sep 5) | I PC tooling |
| 3 | Yungfloop tweet generator, AutoEdit, Bugsquelcher dial, ratings (Sep 29) | D Yungfloop |
| 4 | Knowledge OS: Obsidian canonical + Supabase index, Stay userscript, Scriptable router (pasted design) | C Knowledge OS |
| 5 | Ultimate prompt generator, coding rules, always-on master prompt | H Prompts |
| 6 | Easiest mobile method for memory (Obsidian or other), then easier options | C Knowledge OS |
| 7 | Pokemon on iOS: patch Renegade Platinum, fusion games, Moon Black 2, other fan games, which emulators support them | F Games |
| 8 | Grab Obsidian + Drive, update memory context | C Knowledge OS |
| 9 | Manga memory pipeline (ComfyUI + memory router), checkpointed Copilot prompts | E Manga |
| 10 | Website review for the business site (brkava.com), security + customer experience, Jim approves | J Beans and Roots |
| 11 | Job automation suite plan: Greenhouse/Lever, Oracle, n8n, human-in-the-loop (attachment) | G Jobs |
| 12 | Small items: meshcore-web-keygen link, Wojak/MS-Paint image prompt, beast-mode prompt, Sanity + WebScraping.ai docs | H Prompts / K Backlog |
| 13 | Portal: webhook, Notion, Supabase, admin panel, DB viewer, logs/errors, roadmaps, config | B Portal |
| 14 | OmniTask URL is omnitask.cloudcli.ai (domain is cloudcli.ai; currently 502 = container stopped) | A / B |
| 15 | Todoist project, Drive backup, master prompt, Copilot foundation prompt | L Ops |
| 16 | Connector advice, Google Photos, organize projects, list iPhone apps, Obsidian shortcuts-only, doc vault | C / L |
| 17 | A personal communication reminder | Not stored here (private; keep it in a private note) |

## Workstreams
### A OmniTask Mobile (omnitask-mobile) - status: Phase 0 merged, PRs #8/#9 open
Next: owner merges PR #8 then #9; branch protection (P0-6); visibility/hosting decision (P0-5); then P1-2 Dexie loading states, P1-3 SW update prompt, P1-1 iPhone checklist, P2-1 CSP, P2-5 lint, P2-2 axe/Lighthouse, P2-4 Vite 8. Phase 3 (sync, AI, vectors) stays gated on P1+P2 and BYOK/PKCE (ADR-008).
### B Portal (omnitask-portal) - status: Supabase live, frontend in progress
Supabase project with admin-only RLS, webhook and ai-chat Edge Functions. Frontend tabs: Overview, Webhooks, Logs, Database, Roadmap, Jobs, Assistant, Config. Next: auth setup (human), OpenRouter secret (human), free hosting (human), GitHub webhook (human), capture endpoint, PC runner.
### C Knowledge OS (omni-vault + Supabase)
Phase 0 vault (this repo) -> Phase 1 iPhone capture to inbox (Shortcut -> webhook) -> Phase 2 knowledge schema with pgvector and FTS (migration drafted in the earlier design) -> Phase 3 read-only inventories (Gate A) -> Phase 4 dedupe/archive only with object-level approval.
### D Yungfloop (cjg-chaosjimgen) - PR #2 open
Owner rates 120 drafts (keep/post); model scores stay provisional; Bugsquelcher expansion needs approval for a paid Apify run.
### E Manga memory pipeline - repo not created
Owner picks repo name; Copilot runs 5 checkpoints (audit, foundation, router MVP, ComfyUI dry-run adapter, sync + optional review). Live ComfyUI tests need the PC.
### F Games and ROM hacks
Deliver iOS-only guides (Delta, RetroArch) for Renegade Platinum, fusion games and Moon Black 2; keep emerald-companion and pokemon-unbound-mod-workspace separate. Never host or link ROMs; user supplies legally owned files.
### G Job automation suite - Step 1 done, Step 2 next
Greenhouse/Lever discovery + submitter; invariant: fit score never triggers submission; halt on CAPTCHA/2FA.
### H Prompts
Master prompt, Copilot foundation prompt, Claude prompt, continuation prompt (06-PROMPTS).
### I PC tooling
Cygwin/tmux/noctty notes; PC runner for portal jobs; remote desktop link in portal Config.
### J Beans and Roots website
Plan + mock preview; Jim approves before anything live.
### K Backlog
Meshcore keygen review, Wojak-style image prompt, Sanity/WebScraping.ai docs as connector candidates.
### L Ops
Todoist project, Drive backup folder, changelog on every message, project organization.

## Milestones
- M1 (this week): merge #8/#9, portal usable (login + webhooks + logs), vault live, iPhone capture Shortcut working.
- M2: omnitask-mobile deployed free (Cloudflare Pages), P1 items done, portal hosted free.
- M3: knowledge schema + search, Notion/Todoist sync, PC runner.
- M4: Phase 3 features for omnitask-mobile (sync, AI) per BYOK.
