# Agents catalog

| Agent | Runs where | Best for | Prompt / spec |
|---|---|---|---|
| Perplexity Computer (operator) | Perplexity, with connectors, a browser and a sandbox | Cross-tool work, research, automations, artifacts, PRs | `06-PROMPTS/PERPLEXITY-OPERATOR-PROMPT.md` |
| Computer subagents | Spawned by Computer when asked | Parallel research or independent bounded tasks | Ask "use subagents for ..." |
| Model Council | Perplexity | Hard decisions that need several models to agree | Ask "run Model Council on ..." |
| Omni hub curator | Weekly automation | knowledge_sync module | `skills/omni-hub-sync` |
| Roadmap steward | Weekday automation | roadmap_to_todoist module | `skills/omni-hub-sync` |
| Standards auditor | Monthly automation | standards_audit module | `skills/omni-hub-sync` |
| GitHub Copilot (coding agent) | GitHub, assigned to issues | In-repo PR-sized code | `06-PROMPTS/COPILOT-FOUNDATION-PROMPT.md` |
| Claude | Claude app / Claude Code | Long-context design, refactor, review, writing | `06-PROMPTS/CLAUDE-PROMPT.md` |
| computer-operator, omniportal-architect, omniportal-implementer | omnitask-portal `ai/agents/` | Portal work | repo files |
| AI code review bot | omnitask-mobile `scripts/code-review.mjs` (OpenRouter free) | Severity-tagged PR review | repo file |

Handoff contract (all agents): State, Changes (links), Evidence, Decisions, Security impact, Needs you (click path), Next 3 actions.
