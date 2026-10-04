---
id: master-merge-plan
type: plan
status: proposed
updated: 2026-10-04
---
# Master Plan 1: Merge and consolidate (what we discussed, plus what I did not get to)

Goal: one source of truth per kind of thing, so every tool reads the same facts and the system can improve itself piece by piece. Nothing is deleted without your OK; originals move to Drive "50 Backups".

## Canonical homes
| Kind | Canonical home | Mirrors (read-only pointers) |
|---|---|---|
| Durable memory | omni-vault/BRAIN.md | Drive BRAIN.md copies, Perplexity Project instructions, Notion hub page |
| Settings and IDs | omni-vault/08-CONFIG/config.yaml | Portal Config tab |
| Roadmap | omni-vault/01-ROADMAP (ROADMAP.md short, MASTER-PLAN.md full) | Notion hub, per-repo ROADMAP.md |
| What changed | 99-LOG/CHANGELOG.md (vault), CHANGELOG.md (each repo) | none |
| What ran | 99-LOG/LOG.md | Perplexity automation run history |
| Tasks | Todoist "Knowledge OS" | Portal Jobs tab |
| Files and binaries | Google Drive | Dropbox and OneDrive only as spare |
| Media | Cloudinary (web delivery), Google Photos (personal) | |

## Duplicate versions found (2026-10-04 Drive scan)
| File | Copies | Action |
|---|---|---|
| BRAIN.md | omnitask-clones/omnitask-mobile, OmniTask Backup 2026-10-01 | Done today: both now point to vault BRAIN.md; vault copy is canonical |
| Google-Gemini-Multi-Agent-Setup | 3 .md + 2 .docx at Drive root | Keep newest .md (2026-10-01 22:47) -> 03-DIGEST; others -> 99 Duplicates |
| Token-and-Credit-Saving-Playbook.md | 2 at Drive root + vault 07-COST | Vault wins; Drive copies -> 99 Duplicates |
| omnitask-knowledge-os-skill.md, yungfloop-content-skill.md, pokemon-modding-lab-skill.md | 2 each | Keep newest; consider a vault 10-SKILLS folder |
| master-memory-context.docx | 2 (Aug and Oct) | Diff, fold unique facts into BRAIN.md, archive both |
| iphone-automate.zip | 2 | Keep newest |
| MASTER.env | 2 at Drive root | Secrets file: move into a password manager, then delete from Drive. Never copy into the vault |
| PokéVoid plan.md, roadmap.md, changelog (Google Docs) | Drive root | Move into Kattalassien/pokerogue-mods as docs/PLAN.md, ROADMAP.md, CHANGELOG.md |
| Obsidian folders (Obsidian, Obsidian Vault, Shared Project Vault - Obsidian, NoteFlow Backup) | 4 | Diff against omni-vault, merge unique notes (existing Drive migration plan phase 4) |

Security note: a file named like a password combo list sits at Drive root. It is not yours to keep: delete it (or tell me to move it to Trash). It is a risk if Drive is ever shared or synced.

## Phases (each needs your OK)
1. Today, done: vault gets BRAIN, ROADMAP, LOG, config, plans. Drive BRAIN copies point here.
2. Drive: create 00 Inbox, 10 Projects, 30 School and Old, 40 Archive, 50 Backups, 99 Duplicates. Move duplicates in batches of 25 with an undo log.
3. Repos: every active repo gets the five-doc standard (BRAIN, ROADMAP, CHANGELOG, PLANNEDFEATURES, CONTINUE). One docs PR per repo. Start with pokerogue-mods and steamdeck-ops.
4. Notion: hub page gets a "Read first" block linking BRAIN.md, ROADMAP.md, and this plan. No duplicate content in Notion, links only.
5. Supabase: fix advisors, then mirror BRAIN.md and config.yaml into a read-only table so the portal and OmniTask can query them.
6. Self-improving loop: switch on the weekly gardener (SCHEDULE.md).

## What I did not get to this pass
- Did not move or delete any Drive file (needs your OK per batch).
- Did not change Supabase security settings (PR first).
- Did not read Dropbox or OneDrive (not selected this round).
- Did not run Apify, Leonardo, or CloudConvert jobs (they cost credits; nothing needed them yet).
