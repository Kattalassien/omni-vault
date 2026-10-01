# Continuation Prompt (self-propagating)

```text
Continue Preston's project work. Catch me up, update the roadmap, do the next work package, and give me the next prompt.

INPUTS (fill blanks; delete lines that do not apply)
- Last session summary: [INSERT paste SESSION-HANDOFF.md]
- Decisions since then: [INSERT]
- Files/screenshots: [INSERT file from ____]
- Secrets state: [INSERT which secrets are set, names only]
- Remote desktop link/tool: [INSERT]
- Hosting choice (Cloudflare Pages / public repo / Pro): [INSERT]
- Work package(s) to do: [INSERT IDs from OUTSOURCE-BOARD or "next"]

CONNECTORS NEEDED: GitHub, Supabase, Todoist, Google Drive, Notion (optional), Context7, Apify (approval for paid runs).
SOURCES: omni-vault (MASTER-PLAN, OUTSOURCE-BOARD, FILE-DIGEST), each repo's AGENTS.md and docs/project/*, open PRs, Actions runs.

DO
1 Read sources. 2 Report what changed since last time (PRs merged, checks, new issues). 3 Update roadmap statuses. 4 Execute the work package within the rules in MASTER-PROMPT.md. 5 Verify with evidence. 6 Append 99-LOG/CHANGELOG.md.

FINISH WITH
State, changes with links, evidence, Needs human (exact clicks), next three actions, and a fresh copy of this prompt with updated blanks.
```
