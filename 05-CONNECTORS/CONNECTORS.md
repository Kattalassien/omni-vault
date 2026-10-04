---
id: connectors
type: guide
updated: 2026-10-04
---
# Connectors: what is set up, what to add

## Already connected and what each owns
| Connector | Owns | Notes |
|---|---|---|
| GitHub | Code, docs, PRs, Actions | Computer works through the gh CLI; never merges |
| Supabase | Portal DB, auth, Edge Functions | Project zlxtnknbblgqhdsynjco |
| Notion | Optional roadmap hub | Set notion_roadmap_url in portal Config |
| Todoist | Tasks | Listed as a new Perplexity connector |
| Google Drive | Backups, big files | Via gws CLI |
| Context7 | Up-to-date library docs | Use before writing framework code |
| Apify | Web data collection | Paid runs need your approval |
| Google Photos | Upload, create albums, add app-uploaded items | Cannot see your existing library (below) |
| Dropbox, OneDrive, Gmail/Calendar | Extra storage, mail, calendar | Use Drive as the primary backup |

## Google Photos: what is possible
Since April 2025 the Library API only works with content your app created. It cannot list or search your whole library, and shared-album methods were removed ([Google](https://developers.google.com/photos/support/updates)). A live test of the connected Photos connector returned an empty list, which matches this. To use existing photos you select them with the Picker API. So: no automatic reorganizing of your library. What works: Computer uploads files and creates albums for new content; you pick photos manually when you want me to use them.

## Most useful connectors to add next (in order)
1. Cloudflare (not a built-in Perplexity connector): add via API token for free Pages hosting of omnitask-mobile and the portal. Needed for the hosting decision.
2. Telegram (available, not connected): free push alerts to your iPhone for portal errors and needs-human items.
3. Sentry (built-in, listed by Perplexity) once something is deployed: crash and error tracking beyond portal logs.
4. Vercel (built-in): only if Cloudflare Pages is not wanted; a second free host.
5. Skip: Linear, Atlassian, Evernote. Todoist + Notion + GitHub already cover tasks, docs and code.
Sources: [Perplexity connectors](https://www.perplexity.ai/computer/connectors), [Perplexity connectors list](https://github.com/rdmgator12/Perplexity-Connectors-awesome-list-/blob/main/README.md).

## Popular MCP servers worth knowing
GitHub's official MCP server is the top GitHub-related server by stars ([Glama, Sept 2026](https://glama.ai/mcp/best/github)). Playwright and GitHub lead overall adoption ([MCP leaderboard](https://awesomeagents.ai/leaderboards/mcp-server-ecosystem-leaderboard/)). A community Google Photos MCP exists ([thenavidm](https://github.com/thenavidm/google-photos-mcp-cli)) but is bound by the same API limits.

## Health check 2026-10-04
| Connector | Status | Finding |
|---|---|---|
| GitHub | OK | 50+ repos; omni-vault PR for this pass |
| Google Drive | OK | Duplicates and a security-risk file at root (see 09-MASTER-PLANS/MASTER-MERGE-PLAN.md) |
| Gmail + Calendar | OK | Steam accounts YungFloop, ChaosJim, lpmcgee found in mail; next event Oct 11 |
| Notion | OK | Hub page "Preston Master Automation & Knowledge OS" plus Steam Deck Ops page |
| Todoist | OK | Knowledge OS board, 4 owner sections |
| Supabase | OK | omnitask-portal healthy, 3 advisor findings; Main Chaos Project inactive |
| Sentry | OK | Org chaosinc, 0 projects |
| Jam | OK | 0 recordings |
| Cloudinary | OK | Free plan, 65 assets, 0.68% credits |
| Context7 | OK | Test lookup (Phaser) returned /phaserjs/phaser |
| Apify, CloudConvert, Leonardo AI | OK | Not run (cost credits) |
| Google Photos | Limited | Only app-created media visible |
| PlayStation | None | No connector or public API; use PSN ID + PSNProfiles |
