# Skills catalog

## Perplexity Computer skills (My Skills)
| Skill | Use when | Source copy |
|---|---|---|
| connector-router | Picking and calling a connector: Context7, CloudConvert, Cloudinary, Notion, Supabase, Drive, GitHub, Todoist | `skills/connector-router/SKILL.md` |
| omni-hub-sync | Running the knowledge sync, Roadmap to Todoist sync, or standards audit | `skills/omni-hub-sync/SKILL.md` |
| mod-foundation | Rewriting text into a stronger foundation prompt with `//mod` | omnitask-portal `ai/skills/mod-foundation` |

## Repo skills (SKILL.md folders, readable by Claude Code, Copilot and Computer)
| Repo | Skills |
|---|---|
| omnitask-portal | mod-foundation, omniportal-ops, project-docs-contract, free-hosting-governance |
| consent-first-ai-lab | local-ai-gateway, authorized-security-research |
| omni-vault | connector-router, omni-hub-sync |

## Rules
- A skill does one job, and its description says when to load it. Keep it under about 4,000 characters, with details in `references/`.
- Keep a source copy in a repo (`skills/<name>/SKILL.md`). The saved Perplexity copy must match it, and the standards audit compares versions.
- Never put secrets or account IDs that grant access in a skill.
