# Perplexity Computer playbook (what is unique and how we use it)

| Feature | What it gives us | How we use it |
|---|---|---|
| Projects (formerly Spaces) | Instructions, a persistent file repo, a Project knowledge wiki (Project Brain), and member and Slack links | Use one Project per domain. "Knowledge OS and Vault" owns the hub. Project instructions hold the rules from BRAIN-CORE. Put durable files in the Project file repo, not only in session sandboxes |
| Skills | Reusable SKILL.md playbooks that load when they match | Use `connector-router` and `omni-hub-sync`. Keep source copies in `omni-vault/skills/` |
| Automations | Scheduled runs (one-time or recurring) and event triggers (connector events, price alerts), with completion notifications | Three modules from `08-CONFIG/automations.json`: knowledge_sync (weekly), roadmap_to_todoist (weekdays), standards_audit (monthly). A run can only change things through PRs and connectors under the same rules |
| Agents and subagents | Background workers for parallel, bounded tasks | Only when asked ("use subagents"). Example: one subagent per repo for a docs audit |
| Model Council | Several models answer on their own, then the answers are combined | Architecture decisions and risky changes |
| Artifacts | Every file, site, chart and doc goes to the library and can be published to a link | Shared deliverables: hub diagram, PDFs of guides, the deployed portal preview |
| Memory | Durable facts and preferences across sessions | Mirrors BRAIN.md Identity, Rules and Preferences. Git BRAIN.md wins on conflict |
| Connectors | GitHub, Drive, Notion, Supabase, Todoist, Cloudinary, CloudConvert, Context7 and more | Routed by `connector-router` |
| Browser (cloud or your local browser) | Sites with no connector | Last resort after search and connectors |
| Website deploy | Private preview URLs, with backends proxied to the sandbox | Portal and tool previews before Cloudflare Pages |
| Notifications | Push, in-app and email | Automations notify when done. Silence routine no-change runs |

## Prompt patterns that use these features
- "In the Knowledge OS and Vault project, run omni-hub-sync knowledge_sync now" runs an on-demand sync.
- "Create an automation from 08-CONFIG/automations.json module X" adds a new module.
- "Save this as a skill to My Skills" captures a repeatable workflow.
- "Publish the artifact" gives a share link. Do this only for non-private content.
