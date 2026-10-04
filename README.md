# omni-vault

![Omni Knowledge Hub](https://res.cloudinary.com/sewoj1wp/image/upload/f_auto,q_auto,w_1600/omni-hub/hub/omni-hub-diagram.png)

Start here: BRAIN.md (memory), 01-ROADMAP/ROADMAP.md (next steps), 08-CONFIG/config.yaml (settings).

Master documentation vault for Preston's projects. Plain Markdown, Obsidian-compatible, canonical memory. Private repo.

| Folder | What lives here |
|---|---|
| 00-INBOX | Raw captures (Shortcuts, portal, PC runner). Triage weekly. |
| 01-ROADMAP | MASTER-PLAN (all asks -> workstreams), OUTSOURCE-BOARD (who does what), work-packages.json |
| 02-PROJECTS | Index of every Perplexity Project and GitHub repo, with owner and status |
| 03-DIGEST | Per-file takeaways from every Markdown file reviewed |
| 04-IPHONE | Obsidian shortcuts-only setup, listing iPhone apps, capture Shortcuts |
| 05-CONNECTORS | Which connectors to enable and what each one owns |
| 06-PROMPTS | Master prompt, Copilot foundation prompt, Claude prompt, continuation prompt |
| 07-COST | Token and credit saving playbook, routing table (Computer vs Gemini/OpenRouter vs Copilot) |
| 08-CONFIG | config.yaml: non-secret IDs, extra games, connector status |
| 09-MASTER-PLANS | Mind map, schedule, merge plan, tool mastery plan |
| 10-SHARED | Shared knowledge for every repo: BRAIN/AGENTS core blocks, STANDARDS, SKILLS, AGENTS, FEATURES, CONNECTORS, Perplexity playbook, generated BRAIN-ALL / ROADMAP-ALL / NEXT-STEPS |
| scripts/omnisync.py | Hub sync tool: check, harvest, inject, bundle, sql, todoist (dry-run unless --apply) |
| skills/ | Source copies of Perplexity skills: connector-router, omni-hub-sync |
| 99-LOG | CHANGELOG (what changed) and LOG (what ran) |

Rules: no secrets in this repo (names only, e.g. OPENROUTER_API_KEY). No invented facts: use TODO. Frontmatter on new notes: id, type, project, status, updated.
Open this repo in Obsidian only on a PC. On iPhone, Obsidian is a launcher (see 04-IPHONE/OBSIDIAN-SHORTCUTS-ONLY.md).

## Hub sync in one command

```bash
python scripts/omnisync.py check --repos ..   # then harvest / inject / bundle / todoist (see 10-SHARED/README.md)
```

Three Perplexity automations run this for you (config: `08-CONFIG/automations.json`). They open PRs and never merge.
