# Cross-project features

Shared capabilities. When one project builds one of these, others reuse it instead of rebuilding.

| Feature | Lives in | Reused by / planned for |
|---|---|---|
| Five-docs contract and idempotent doc edits (docsctl.py) | omnitask-portal `scripts/docsctl.py` | all repos (via omnisync check) |
| Docs-health CI gate | omnitask-portal `scripts/docs-health.mjs` | omni-vault hub-check workflow |
| Project registry JSON | omnitask-portal `config/projects.json`, omni-vault `08-CONFIG/projects.json` | portal Projects tab, omnisync, automations |
| Preview-then-apply safety loop | quick-console `qc clean`, steamdeck-ops `--dry-run` | omnisync `--apply`, portal runner |
| Safety rule engine (blocks iex, encoded PS, wscript) | quick-console `Private/Safety.ps1` | portal cc validator (QC-4) |
| Local-first storage (Dexie) | omnitask-mobile | offline review of Yungfloop drafts |
| AI code review (OpenRouter free, severity tags) | omnitask-mobile `scripts/code-review.mjs` | any repo PR workflow |
| Ratings kept separate from model scores | cjg-chaosjimgen | OmniTask review surface |
| Apify ingest with provenance | cjg-chaosjimgen `scripts/ingest-apify.ts` | deal tracker (approval-gated) |
| Agent registry with retry and priority queues | llm-knowledge-base `config/agents.json` | omni automations retry policy |
| Signed webhooks (HMAC-SHA256, backoff) | llm-knowledge-base `config/webhooks.json` | portal `webhook_events` |
| Hard-boundary brain with a version header | consent-first-ai-lab `brain.md` | BRAIN-CORE versioned block |
| Userscript mod menus | pokerogue-mods | Brain Bot capture, Stay scripts |
| Hub sync (managed blocks, harvest, mirrors) | omni-vault `scripts/omnisync.py` | every repo |
