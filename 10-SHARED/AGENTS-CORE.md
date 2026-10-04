## Shared agent rules (from omni-vault)
1. Read BRAIN.md, ROADMAP.md and CONTINUE.md before working. Do not redo finished work.
2. Check live docs with Context7 before writing framework code.
3. Make the smallest change that works. Use a branch `omni/<topic>` and open a PR. Never merge.
4. Preview before apply: dry-run, `-WhatIf`, or a diff first. Destructive steps need approval for the specific object.
5. Never print, log or commit secrets. Use only key names. Do not use service_role in clients.
6. Finish by updating CHANGELOG.md and CONTINUE.md. Add durable facts to BRAIN.md `## Facts learned`.
7. Route work: in-repo PR-sized code goes to Copilot, long-context design or review goes to Claude, and cross-tool work goes to Perplexity Computer. Catalog: omni-vault/10-SHARED/AGENTS.md.
