---
id: brain
type: memory
project: all
status: active
updated: 2026-10-04
---
# BRAIN (canonical shared memory)

## What this file is
BRAIN.md is the one portable memory that every AI tool reads before working for Preston: Perplexity Computer, ChatGPT, Claude, Copilot, Gemini, and OmniTask. None of these tools share memory natively, so this file is the bridge.

- It holds durable facts only: identity, accounts, devices, active projects, preferences, rules, decisions.
- It is not a task list (Todoist), not a log (99-LOG/LOG.md), not a changelog (99-LOG/CHANGELOG.md), and not settings (08-CONFIG/config.yaml).
- One fact per bullet, dated, terse. When a fact changes, edit the bullet and note the date; do not stack contradictions.

## How to use it
1. Start of any AI session: paste or attach BRAIN.md (or tell Computer "read omni-vault BRAIN.md").
2. Perplexity Projects and Custom GPTs: paste the Identity, Rules, and Preferences sections into their instructions.
3. When a tool learns something durable, append it here through a PR (Computer and Copilot) or directly on PC in Obsidian.
4. Older copies exist in Drive (omnitask-clones/omnitask-mobile/BRAIN.md and OmniTask Backup 2026-10-01/omnitask-mobile__BRAIN.md). Those now point here. This file wins on conflict.

---

## Identity
- 2026-07-14: Preston McGee (@yungfloop), Altamonte Springs FL. iPhone-first builder; GitHub account Kattalassien.
- 2026-10-04: Works at Beans & Roots (helps with its website; Jim approves anything live).

## Accounts and handles (names only, never secrets)
- 2026-10-04: Steam main: YungFloop (steamcommunity.com/id/yungfloop, SteamID64 76561198011626659). Profile public, but game details are private, so recent play time is not readable.
- 2026-10-04: Other Steam accounts seen in mail: ChaosJim (mcgee.preston@gmail.com) and lpmcgee (purchase receipts).
- 2026-10-04: PSN ID: TODO (needed for a PS5 games feed via a public PSNProfiles page).
- 2026-10-04: Sentry org chaosinc (no projects yet). Supabase projects: omnitask-portal (active), Main Chaos Project (inactive). Cloudinary free plan (65 assets, under 1% credits).

## Devices
- PS5 (BG3 with console mods via the in-game mod manager), PC with Steam, Steam Deck (EmuDeck on SD, steamdeck-ops repo), iPhone (Delta, RetroArch, Shortcuts, Möbius Sync).

## Active projects (detail lives in 02-PROJECTS/INDEX.md)
- OmniTask Mobile + Portal, Knowledge OS (this vault), Yungfloop generator, Steam Deck Ops, PokeRogue/PokéVoid overlay, Pokémon hack tooling (emerald-companion, pokemon-unbound-mod-workspace), Job automation suite, Manga memory pipeline, Beans & Roots website, Hardware deal tracker.

## Games (feeds the Daily Gaming Digest)
- Core: Baldur's Gate 3 (PS5 modded: Chocolate Edition, Mystra's Spells, Fade's AIO, 2024 Spell Updates), Elden Ring, Dark Souls (DSR modding, DS2, DS3), Pokémon games and ROM hacks (Unbound, Emerald Rogue, Infinite Fusion, PokeRogue/PokéVoid).
- Extra (up to 10): Bloodborne, Resident Evil Village, RimWorld, Steam Deck emulation tooling. Edit the list in 08-CONFIG/config.yaml.

## Rules (apply in every tool)
- Checkpoints: one PR per concern, never merge without Preston, no secrets in files or logs, no invented facts (write TODO).
- iPhone-first instructions. Free tiers first; ask before anything that bills (Apify paid runs, Leonardo credits, CloudConvert minutes).
- Never host or link ROMs.

## Preferences
- Concise, organized answers that end in clear next steps.
- Social writing must sound genuine, not forced.
- Strict dark mode for apps (#121212 / #BB86FC / #03DAC6), 48px tap targets, Markdown everything.

## Decisions
- 2026-10-01: omni-vault is the single vault; Drive is the file archive.
- 2026-10-04: The four gaming digests were merged into one Daily Gaming Digest at 9:00 AM ET.
- 2026-10-04: Knowledge is shared with a hub plus managed blocks: omni-vault 10-SHARED, copied into each repo by `scripts/omnisync.py`. Git is the source of truth; Supabase kb_docs, the Drive and Notion "Omni Knowledge Hub" and Todoist are mirrors.
- 2026-10-04: On Todoist Free, each project is a section of "Dev Projects". Roadmap items sync with an `omni-key:` line for dedupe.
- 2026-10-04: Stacked PRs are merged top-down (child into parent branch first), or rebased and retargeted to main before merging. Never merge a child after its parent was squash-merged.
- 2026-10-04: New project planned: a local-first, approval-gated browser automation panel (working name TODO). Plan only; no repo yet. See 99-LOG/LEARNINGS-2026-10-04.md.

## Facts learned
<!-- Append dated durable facts here. -->
- 2026-10-04: Squash-merging a stacked PR into its parent branch does not reach main. omnitask-mobile #9–#11 landed only in their stack branches, and main is still missing PROJECT-STATE.md, CONNECTOR-AUDIT.md, SESSION-HANDOFF.md and ADR-010. A recovery PR (cherry-pick of 5 commits, tested clean) is pending approval.
- 2026-10-04: omnitask-mobile main got commit 0e7c19b (bidirectional Todoist sync) without a PR. PR #15 quarantines it; merge #15 first.
- 2026-10-04: llm-knowledge-base was renamed to omnitool-knowledge. GitHub redirects the old URL. The hub slug stays llm-knowledge-base so linked records keep working.
- 2026-10-04: The red "review" and "code-review" checks are AI reviewers (OpenRouter, GitHub Models) failing without a key or quota. They are not test failures. omnitool-knowledge's reviewer action is unpinned (`@main`).
- 2026-10-04: Todoist Free limits are reached: project count and saved filters. Supabase project zlxtnknbblgqhdsynjco has only 3 older advisor findings.
- 2026-10-04: Cloudinary cloud `sewoj1wp` (public name). Project cards are transformation URLs on omni-hub/base/card-base, so nothing is stored per card.
