# Outsource Board

Owners: **Computer** = Perplexity Computer (connectors, multi-repo, research, QA). **Copilot** = GitHub Copilot coding agent (single-repo PR-sized code). **Claude** = Claude Code or Claude app (long-context design, refactors, writing, review). **Human** = Preston (clicks, approvals, secrets).

Rule of thumb: Copilot gets tasks with exact files and tests; Claude gets tasks needing judgment or many files; Computer gets anything crossing tools; Human gets anything with money, secrets, visibility or merging.

| ID | WS | Task | Owner | Depends | Done when | Size |
|---|---|---|---|---|---|---|
| A1 | A | Merge PR #8 then #9 (after reading checks)  | Human |  | Both merged on GitHub mobile | XS |
| A2 | A | P0-6 protect main: require CI checks | Human | A1 | Branch rule active | XS |
| A3 | A | Decide hosting: Cloudflare Pages free (keeps repo private) vs public repo for GitHub Pages; review BRAIN.md first | Human | A1 | Decision recorded in ADR | S |
| A4 | A | Remove cr-gpt app spam (Settings > Applications) | Human |  | No more OPENAI_API_KEY comments | XS |
| A5 | A | P1-2 Dexie boot loading states | Copilot | A1 | Spinner/skeleton while Dexie loads; smoke test added; build green | S |
| A6 | A | P1-3 service worker update prompt | Copilot | A5 | Toast when new version waits; test | S |
| A7 | A | P1-1 iPhone PWA manual smoke checklist (docs/testing.md) | Claude |  | Checklist covers install, offline, notes, export | S |
| A8 | A | P2-1 strict CSP | Copilot | A5 | CSP meta, app works, smoke green | S |
| A9 | A | P2-5 ESLint + Prettier + CI lint | Copilot | A5 | CI lint job passes | S |
| A10 | A | P2-2 axe-core + Lighthouse CI | Copilot | A8 | a11y/PWA budgets in CI | M |
| A11 | A | P2-4 Vite 8 upgrade (clears esbuild advisory) | Copilot | A9 | npm audit clean or documented | M |
| A12 | A | DOC-1 and DOC-2 stale-doc fixes | Copilot | A1 | QUICKSTART + package.json honest | XS |
| B1 | B | Finish portal frontend pages (Database, Roadmap, Jobs, Config, Assistant) + CSS | Computer |  | Build green, smoke green, QA login works | M |
| B2 | B | Supabase Auth: set Site URL and add {{ .Token }} to Magic Link template | Human | B1 | Email sign-in works from iPhone | XS |
| B3 | B | Set OPENROUTER_API_KEY in Supabase Edge Function secrets | Human |  | Assistant tab answers | XS |
| B4 | B | Host portal free on Cloudflare Pages (connect repo, build npm run build, output dist) | Human | B1 | Permanent URL stored in Config | S |
| B5 | B | Add GitHub webhook(s) pointing at portal webhook with secret from Webhooks tab | Human | B2 | Events appear in inbox | XS |
| B6 | B | capture Edge Function: POST note -> knowledge inbox + commit to omni-vault 00-INBOX | Copilot | B1 | Shortcut capture lands in repo and DB | M |
| B7 | B | PC runner script (Node, outbound polling of jobs table) | Copilot | B1 | Job created in portal runs on PC and reports result | M |
| B8 | B | Notion + Todoist sync functions (roadmap_items <-> Notion DB / Todoist) | Claude | B1 | Two-way sync documented and tested | L |
| C1 | C | Vault repo omni-vault created, digest + plan committed | Computer |  | Repo exists, README, digest | S |
| C2 | C | Obsidian launcher setup on iPhone (shortcuts only) | Human | C1 | Shortcut opens launcher note | XS |
| C3 | C | iPhone capture Shortcuts: quick note, link, photo note -> portal webhook | Human | B2 | Three Shortcuts installed | S |
| C4 | C | Knowledge schema migration (items, chunks, edges, pgvector, FTS, RLS) | Claude | B1 | Migration applies; RLS tests pass | L |
| C5 | C | Gate A: read-only inventory of GitHub, Drive, Notion, Todoist, Supabase, Photos | Computer | C1 | Inventory CSV in vault; no changes made | M |
| C6 | C | Stay userscript + Scriptable router (private Safari capture) | Claude | C4 | Scripts committed with README | M |
| D1 | D | Rate the 120 yungfloop drafts (keep/post) | Human |  | Ratings stored | S |
| D2 | D | Approve or decline paid Apify run for bugsquelcher sample | Human |  | Decision recorded | XS |
| E1 | E | Create manga-memory-pipeline repo (name your choice) and run checkpoint prompt | Human |  | Repo exists | XS |
| E2 | E | Checkpoints 1-5 of manga pipeline | Copilot | E1 | One PR per checkpoint | L |
| F1 | F | iOS-only guides: Renegade Platinum patch+play, fusion games, Moon Black 2, other fan games | Computer |  | Guide in vault, sources cited | M |
| F2 | F | emerald-companion and pokemon-unbound-mod-workspace: README, CHANGELOG, ROADMAP | Computer |  | Docs PRs open | S |
| G1 | G | Step 2 Greenhouse + Lever discovery/submitter | Copilot |  | Acceptance tests in plan pass | L |
| G2 | G | Oracle Always-Free deploy (Step 3) | Human | G1 | Health endpoint 200 | M |
| J1 | J | Beans and Roots plan + mock preview; Jim approval gate | Claude |  | Mock preview shared; no live change | M |
| L1 | L | Todoist project 'OmniTask Portal' from this board | Computer |  | Tasks created | S |
| L2 | L | Drive backup folder with all text/markdown files | Computer |  | Folder link | S |
| L3 | L | Changelog + continuation prompt updated after every message | Computer |  | 99-LOG/CHANGELOG.md current | XS |

Prompts to hand out: 06-PROMPTS/COPILOT-FOUNDATION-PROMPT.md (Copilot), 06-PROMPTS/CLAUDE-PROMPT.md (Claude), 06-PROMPTS/MASTER-PROMPT.md (Computer).
