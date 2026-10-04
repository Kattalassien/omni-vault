# ROADMAP-ALL (generated 2026-10-04T07:50Z)

| Project | Ref | Item | Status | Owner |
|---|---|---|---|---|
| omnitask-portal | QC-1 | QuickConsole read-only module: qc help/doctor/runtime/disk/space/scoop/commands/report, cc list (docs/QC.md) | todo | Copilot |
| omnitask-portal | QC-2 | Runner allow-list IDs qc.* (read-only) + sanitized report contract v1 | todo | Copilot |
| omnitask-portal | QC-3 | Portal QC tab (mock JSON first): Overview, Disk, Runtime, Packages, Commands, Reports | todo | Copilot |
| omnitask-portal | QC-4 | Quick-add cc definitions in portal; PC-side validator rejects unsafe patterns | todo | Claude |
| omnitask-portal | QC-5 | qc clean -WhatIf previews; -Apply with typed local confirmation | todo | Copilot |
| omnitask-portal | QC-6 | Run baseline audit on PC and share redacted sections | todo | Human |
| omnitask-portal | OP-1 | Rebrand UI to OmniPortal, add five operating docs | in review (pr) | Computer |
| omnitask-portal | OP-2 | Project registry `config/projects.json` + Projects tab | in review (pr) | Computer |
| omnitask-portal | OP-3 | Layered, auto-refreshing settings + Settings tab + audit log | in review (pr) | Computer |
| omnitask-portal | OP-4 | Docs-contract health script + CI gate | in review (pr) | Computer |
| omnitask-portal | OP-5 | AI kit: 3 prompts, 3 skills, 2 agents in `ai/` | in review (pr) | Computer |
| omnitask-portal | OP-10 | Local runner on 127.0.0.1 (status, allow-listed commands, IDE launch) | in review (pr, untested on windows) | Computer |
| omnitask-portal | OP-11 | Test runner on owner PC: `scripts\start-omniportal.ps1` | todo | Human |
| omnitask-portal | OP-12 | Runner outbound polling of `jobs` (dedicated admin user, never service_role) | todo | Copilot |
| omnitask-portal | OP-13 | Run buttons in Projects tab calling runner (token prompt, live output) | todo | Copilot |
| omnitask-portal | OP-20 | New-project wizard: scaffold repo + 5 docs + AGENTS.md + CI | todo | Claude |
| omnitask-portal | OP-21 | Roll docs contract into every registry repo (one PR each) | todo | Computer |
| omnitask-portal | OP-30 | Long-term hosting research: Cloudflare, GitHub Pages, Netlify, Vercel, Supabase, AWS, self-host (docs/HOSTING.md) | in progress | Computer |
| omnitask-portal | OP-31 | Host-profile switcher writes deploy config per project | todo | Copilot |
| omnitask-portal | OP-32 | AWS escalation path (only for workloads that justify cost) | todo | Computer |
| omnitask-portal | OP-40 | Scheduled `docs:github` snapshot via GitHub Action | todo | Copilot |
| omnitask-portal | OP-6 | docsctl.py: generate + edit the five docs in any repo (Python, stdlib) | in review (pr) | Computer |
| omnitask-portal | OP-7 | Gen-1 environment foundation prompt, computer-operator agent, //mod skill | in review (pr) | Computer |
| omnitask-portal | OP-33 | AWS budget alert ($5) before any Lightsail instance; Lightsail only for always-on API | todo | Human |
| omnitask-portal | PT-0 | Supabase project, schema, RLS | done | Computer |
| omnitask-portal | PT-1 | Webhook receiver (fail-closed) | in progress (verified) | Computer |
| omnitask-portal | PT-2 | Portal UI MVP | in progress (verified live) | Computer |
| omnitask-portal | PT-3 | Repo, docs, rules, CI | in progress | Computer |
| omnitask-portal | PT-4 | Auth: Site URL + {{ .Token }} in email template | todo | Human |
| omnitask-portal | PT-5 | Free hosting on Cloudflare Pages | todo | Human |
| omnitask-portal | PT-6 | OPENROUTER_API_KEY secret | todo | Human |
| omnitask-portal | PT-7 | Start CloudCLI env (omnitask.cloudcli.ai) | todo | Human |
| omnitask-portal | PT-8 | GitHub webhooks into inbox | todo | Human |
| omnitask-portal | PT-9 | Notion roadmap sync | todo | Claude |
| omnitask-portal | PT-10 | Todoist mirror | todo | Copilot |
| omnitask-portal | PT-11 | Auto-import docs/sync/tasks.json | todo | Copilot |
| omnitask-portal | PT-12 | PC runner (superseded by OP-10..13) | in progress | Copilot |
| omnitask-portal | PT-13 | Opt-in client error reporter for omnitask-mobile (needs ADR there) | todo | Claude |
| omnitask-portal | PT-14 | Nightly export to Drive | todo | Copilot |
| omnitask-portal | PT-15 | Knowledge OS bridge (captures, retrieval logs) | todo | Claude |
| omnitask-mobile | R-1 | Fix code-review.mjs crash on large diffs (MAX_PATCH_LENGTH -> MAX_PATCH) | in_review |  |
| omnitask-mobile | DOC-1 | Correct stale QUICKSTARTGUIDE claims (reviewer paused-mode wording, hosting status) | todo |  |
| omnitask-mobile | DOC-2 | Honest package.json description (remove Drive/Obsidian sync claim) per ADR-004 | todo |  |
| omnitask-mobile | P0-5 | GitHub Pages deploy pipeline (zero-secret, GITHUB_TOKEN) | blocked | Human |
| omnitask-mobile | P0-6 | Protect main branch (require CI checks before merge) | blocked | Human |
| omnitask-mobile | P1-1 | Manual iPhone PWA smoke checklist (docs/testing.md) | todo |  |
| omnitask-mobile | P1-2 | Loading states for async Dexie boot (Suspense/spinner) | todo |  |
| omnitask-mobile | P1-3 | Service worker update prompt when a new version is waiting | todo |  |
| omnitask-mobile | P2-1 | Strict CSP in index.html (XSS hardening) | todo |  |
| omnitask-mobile | P2-2 | axe-core + Lighthouse CI (a11y + PWA budgets) | todo |  |
| omnitask-mobile | P2-3 | Evaluate dexie-react-hooks useLiveQuery vs useSyncExternalStore | todo | Human |
| omnitask-mobile | P2-4 | Vite 8 upgrade; consider React 19 (clears esbuild advisories) | todo |  |
| omnitask-mobile | P2-5 | ESLint + Prettier + CI lint job | todo |  |
| omnitask-mobile | P2-6 | docs/architecture.md (Mermaid) + docs/testing.md | todo |  |
| quick-console | P1 | Read-only core: doctor, runtime, startup, disk, space, commands, which, scoop, help | done (v0.1.0) |  |
| quick-console | P2 | Package reports and export: `qc packages`, cheat sheets | done (v0.1.0) |  |
| quick-console | P3 | Cleanup with preview by default and allowlisted `-Apply` | done (v0.1.0) |  |
| quick-console | P4 | `cc` registry: path/app/url/qc/script/shell, hash pinning, safety checks | done (v0.1.0) |  |
| quick-console | P5 | Security: `qc check`, `qc security` | done (v0.1.0) |  |
| quick-console | P6 | Continuity: config layering, `qc set`, `qc setup`, `qc sync`, `qc update` | done (v0.1.0) |  |
| quick-console | P7 | Validate on real Windows 10 and 11 machines; tune the defaults | next |  |
| quick-console | P8 | Optional integrations: a Todoist/Calendar maintenance rhythm, a Notion command catalog | planned (approval-gated) |  |
| quick-console | P9 | Optional opt-in telemetry summaries (Supabase), with redaction | later |  |
| quick-console |  | `qc space -Duplicates`: find duplicate ISOs, archives, and installers by hash | todo |  |
| quick-console |  | `qc clean -Target Downloads -OlderThan 90`: interactive picker for review-tier items (Out-GridView, or a console picker) | todo |  |
| quick-console |  | Docker and WSL disk views (`docker system df`, VHDX sizes) as report-only items | todo |  |
| quick-console |  | `qc startup -Disable <name>`: approval-gated, reversible (records the original state) | todo |  |
| quick-console |  | `qc packages diff`: compare two scoopfiles or PCs | todo |  |
| quick-console |  | More cheat sheets: choco, uv, pnpm, rustup, steamcmd | todo |  |
| quick-console |  | `cc add` from history: `cc add last` saves the last safe command | todo |  |
| quick-console |  | Scoop bucket manifest so `scoop install quick-console` works (once the repo is public, or with a token-free release asset) | todo |  |
| quick-console |  | Export the `cc` registry to Notion as a database (approval-gated) | todo |  |
| quick-console |  | Todoist recurring maintenance tasks generated from the docs/07 rhythm (approval-gated) | todo |  |
| quick-console |  | `qc security -Export` creates an evidence bundle (text only, redacted) for incident notes | todo |  |
| omni-vault | HUB-1 | Review and merge the omni-hub-sync PR (10-SHARED, omnisync.py, skills, automations config) | todo | Human |
| omni-vault | HUB-2 | Review the quick-console pilot PR (shared blocks + AGENTS.md) | todo | Human |
| omni-vault | HUB-3 | Roll shared blocks into the remaining repos (weekly sync opens up to 5 PRs per run) | todo | Computer |
| omni-vault | HUB-4 | Add the five operating docs to repos that are missing them (see `omnisync.py check`) | todo | Copilot |
| omni-vault | HUB-5 | Portal "Knowledge" tab that reads kb_docs and kb_project_summary | todo | Copilot |
| omni-vault | HUB-6 | Decide on a Todoist Pro upgrade (switches folders from sections to real projects; mode in automations.json) | todo | Human |
| omni-vault | C2 | Obsidian launcher setup on iPhone (shortcuts only) | todo | Human |
| omni-vault | C3 | iPhone capture Shortcuts: quick note, link, photo note -> portal webhook | todo | Human |
| omni-vault | C4 | Knowledge schema migration (items, chunks, edges, pgvector, FTS, RLS) | todo | Claude |
| omni-vault | C5 | Gate A: read-only inventory of GitHub, Drive, Notion, Todoist, Supabase, Photos | todo | Computer |
| omni-vault | C6 | Stay userscript + Scriptable router (private Safari capture) | todo | Claude |
| omni-vault | L1 | Todoist project 'OmniTask Portal' from this board | todo | Computer |
| omni-vault | L2 | Drive backup folder with all text/markdown files | todo | Computer |
| omni-vault | L3 | Changelog + continuation prompt updated after every message | todo | Computer |
| job-automation-suite | G1 | Step 2 Greenhouse + Lever discovery/submitter | todo | Copilot |
| job-automation-suite | G2 | Oracle Always-Free deploy (Step 3) | todo | Human |
| cjg-chaosjimgen | D1 | Rate the 120 yungfloop drafts (keep/post) | todo | Human |
| cjg-chaosjimgen | D2 | Approve or decline paid Apify run for bugsquelcher sample | todo | Human |
| pokemon-unbound-mod-workspace | F1 | iOS-only guides: Renegade Platinum patch+play, fusion games, Moon Black 2, other fan games | todo | Computer |
| pokemon-unbound-mod-workspace | F2 | emerald-companion and pokemon-unbound-mod-workspace: README, CHANGELOG, ROADMAP | todo | Computer |
| manga-memory-pipeline | E1 | Create manga-memory-pipeline repo (name your choice) and run checkpoint prompt | todo | Human |
| manga-memory-pipeline | E2 | Checkpoints 1-5 of manga pipeline | todo | Copilot |
| beans-and-roots-website | J1 | Beans and Roots plan + mock preview; Jim approval gate | todo | Claude |
| steamdeck-ops | SD-1 | deckops.sh v0.1.0 + smoke test + CI (PR #1) | in_review | Human |
| steamdeck-ops | SD-2 | Runbook docs/RUNBOOK.md (PR #2) | in_review | Human |
| steamdeck-ops | SD-3 | First real run on Deck: passwd, doctor, --dry-run all, backup to SD/USB | todo | Human |
| steamdeck-ops | SD-4 | EmuDeck Custom Mode install to SD + custom Library layout + SRM parse | todo | Human |
| steamdeck-ops | SD-5 | Syncthing pairing with iPhone via Mobius Sync; RetroArch saves round-trip test | todo | Human |
| steamdeck-ops | SD-6 | Weekly flatpak timer + admin-commands.txt customized | todo | Human |
| steamdeck-ops | SD-7 | Portal run reports: webhook.header on Deck, verify steamdeck events in Webhooks tab | todo | Human |
| steamdeck-ops | SD-8 | Steam Deck as PC-runner job target (allow-listed deckops kinds) after OP-12 | todo |  |
| consent-first-ai-lab |  | Establish non-negotiable scope, data, and safety rules. | done |  |
| consent-first-ai-lab |  | Create project brain, two skills, review template, and initial review. | done |  |
| consent-first-ai-lab |  | Create a localhost-only chat gateway that keeps keys server-side. | done |  |
| consent-first-ai-lab |  | Create a local-only browser companion demonstration. | done |  |
| consent-first-ai-lab |  | Create a written Rules of Engagement template and populate it for the first owned/lab target. | todo |  |
| consent-first-ai-lab |  | Choose one upstream: Ollama/LM Studio/vLLM locally, or OpenRouter with a budget-limited key. | todo |  |
| consent-first-ai-lab |  | Add model discovery and health checks to the gateway. | todo |  |
| consent-first-ai-lab |  | Add a local conversation export format with redaction. | todo |  |
| consent-first-ai-lab |  | Add a small standalone web UI served from localhost. | todo |  |
| consent-first-ai-lab |  | Add test fixtures marked `DUMMY DATA`; no third-party conversation import. | todo |  |
| consent-first-ai-lab |  | Add structured logging with prompt-content redaction. | todo |  |
| consent-first-ai-lab |  | Build a scope manifest and validation tool. | todo |  |
| consent-first-ai-lab |  | Add evidence templates, severity assessment, and responsible-disclosure drafts. | todo |  |
| consent-first-ai-lab |  | Practice only against local labs; document remediation, not exploitation. | todo |  |
| consent-first-ai-lab |  | Add CI secret scanning and dependency review. | todo |  |
