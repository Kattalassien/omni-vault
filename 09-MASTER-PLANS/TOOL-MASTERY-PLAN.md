---
id: tool-mastery-plan
type: plan
status: draft
updated: 2026-10-04
---
# Master Plan 2: Tool mastery (each tool's abilities, and clever ways to combine them)

Each row is what the connected tool can actually do through Perplexity today (checked 2026-10-04), its best job in your system, and its limits. Strategies at the bottom combine them. Fill "Your example" so we can turn your answer into the first reusable strategy.

## Abilities per tool
| Tool | Can do (verified tool list) | Best job for you | Limits and rules |
|---|---|---|---|
| GitHub | Repos, branches, PRs, issues, Actions via gh CLI | Home of code and the vault; every change is a PR | Never merge for you |
| Google Drive | Search, read, export, upload, move via gws CLI | Archive of originals, backups, big files | Moves need your OK per batch |
| Gmail + Calendar | Search mail, drafts, labels, send; search and update events | Receipts (Steam, Nexus), deal alerts, reminders | Sending mail or invites needs your OK |
| Notion | Search, fetch, create and update pages and databases, comments | Visual hub page with links to the vault | Do not duplicate vault text; link it |
| Todoist | Tasks, sections, labels, reminders, filters, project health stats | The single task inbox, split by owner | Free plan limits project count |
| Supabase | SQL, migrations, Edge Functions, advisors, logs, branches | Portal DB and future knowledge index | DDL and secrets changes via PR and your OK |
| Sentry | Issues, errors, traces, logs, Seer analysis | Error watch once apps are deployed | Org chaosinc has no projects yet |
| Jam | Bug recordings with console, network, video; folders, comments | Record an iPhone or browser bug once, hand it to Copilot with full logs | Empty today |
| Cloudinary | Upload, tag, search, transform, generate images, archives | Web-ready media for portal, OmniTask, Yungfloop posts | Free plan, 25 credits |
| Context7 | Live docs for libraries (Phaser, Vite, Dexie, Supabase) | Check docs before any code is written | Docs only |
| Apify | Run actors (scrapers), datasets, RAG web browser | Bulk collection: tweets for Yungfloop, mod lists, prices | Paid runs need approval |
| CloudConvert | Convert, merge to PDF, archive, import by URL | Turn Drive .docx into Markdown for the vault | Limited free minutes |
| Leonardo AI | Generate, upscale, unzoom, motion | Manga panels, thumbnails, mod-showcase art | Spends credits; ask first |
| Google Photos | Upload, albums, share; only app-created items | Send generated art to an album on your phone | Cannot read your existing library |
| Web search | Current news, mod pages, threads | Powers the gaming digest and research | Links must come from real pages |

## Strategies (combinations)
1. Bug to fix loop: Jam recording -> Computer reads console and network -> Context7 docs -> Copilot PR -> Sentry confirms the error stops.
2. Doc migration loop: Drive .docx -> CloudConvert to Markdown -> PR into omni-vault 03-DIGEST -> Drive original to 50 Backups.
3. Mod showcase loop: digest finds a big mod -> Leonardo makes a cover image -> Cloudinary hosts it -> draft Yungfloop post for your rating.
4. Memory loop: any session learns a fact -> LOG.md -> Sunday gardener PR updates BRAIN.md -> Notion hub and Project instructions point to it.
5. Deal loop: Gmail Steam wishlist and Slickdeals alerts -> hardware deal tracker -> Todoist task only when price beats your target.
6. Error budget loop: weekly infra watch reads Supabase advisors and Sentry -> one Todoist task per finding -> PR per fix.

## Your example
Template: "If [trigger] happens, then [tools] should [action], and I only want to be bothered when [condition]."
Example to answer: "If a mod I use in BG3 on PS5 gets a big update, what should happen?" Your solution goes here and becomes Strategy 7.

- Trigger: TODO
- Tools and steps: TODO
- When to notify me: TODO
