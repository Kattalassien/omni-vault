# BRAIN-ALL (generated 2026-10-04T07:50Z)

Durable facts harvested from every project's BRAIN.md (`## Facts learned` / `## Decisions`).
Do not edit here; edit the project's BRAIN.md and rerun `omnisync.py harvest`.

## OmniPortal (omnitask-portal) (omnitask-portal)
- ADR-001..003 in docs/decisions. 2026-10-01: keep repo name, rebrand UI to OmniPortal; settings overrides stored in existing `app_config` (no migration); runner loopback-only with token.
- 2026-10-04: Docs are edited with scripts/docsctl.py (Python) so formatting stays machine-readable; docs-health.mjs remains the cross-repo snapshot. QC engine stays local on the PC; portal only requests allow-listed action IDs.

## OmniTask Mobile (omnitask-mobile)
- 2026-10-04 — Dexie IndexedDB supports additive multi-version schema upgrades; version(2) stores `todoist_id` and `sync_queue` without wiping existing user notes or tasks.
- 2026-10-04 — Todoist REST API v2 supports CORS and direct client-side Bearer authentication, making direct PWA sync viable without an intermediary server proxy.
- 2026-10-04 — Storing automated log streams directly in Git leads to high commit churn and merge conflicts; preferred pattern is structured Supabase telemetry or append-only Obsidian markdown.

## QuickConsole (qc + cc) (quick-console)
- TODO: no BRAIN.md facts yet

## Omni Vault (omni-vault)
- 2026-10-01: omni-vault is the single vault; Drive is the file archive.
- 2026-10-04: The four gaming digests were merged into one Daily Gaming Digest at 9:00 AM ET.

## LLM Knowledge Base (llm-knowledge-base)
- TODO: no BRAIN.md facts yet

## Job Automation Suite (job-automation-suite)
- TODO: no BRAIN.md facts yet

## Yungfloop voice engine (cjg-chaosjimgen) (cjg-chaosjimgen)
- TODO: no BRAIN.md facts yet

## PokéRogue mods (pokerogue-mods)
- TODO: no BRAIN.md facts yet

## Emerald Companion (emerald-companion)
- TODO: no BRAIN.md facts yet

## Pokémon Unbound mod workspace (pokemon-unbound-mod-workspace)
- TODO: no BRAIN.md facts yet

## Manga Memory Pipeline (manga-memory-pipeline)
- TODO: no BRAIN.md facts yet

## Beans & Roots website (beans-and-roots-website)
- TODO: no BRAIN.md facts yet

## Steam Deck Ops (steamdeck-ops)
- TODO: no BRAIN.md facts yet

## Consent-first AI Lab (consent-first-ai-lab)
- TODO: no BRAIN.md facts yet

## Hardware Deal Tracker (hardware-deal-tracker)
- TODO: no BRAIN.md facts yet
