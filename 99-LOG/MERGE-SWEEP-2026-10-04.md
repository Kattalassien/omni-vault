# Merge sweep 2026-10-04

Merged (squash, docs-only, no secrets found): omnitask-mobile #8 #9 #10 #11 #13; omni-vault #1 #2; cjg-chaosjimgen #2 #3 #4; emerald-companion #1; pokemon-unbound-mod-workspace #2; omnitool-knowledge #6 #7 (repo renamed from llm-knowledge-base).

## Still to do (held on purpose)
| PR | Why held | Next step |
|---|---|---|
| omnitask-mobile #15 | edits ci.yml; code change | review diff, run npm ci/build/smoke, then merge |
| omnitask-mobile #12 | conflicting, 31 files / 1500 lines | rebase, split into <600-line PRs |
| omnitask-mobile #14 | draft; review check failed; adds SQL | finish, then re-review |
| omnitask-portal #1 #3 | edit ci.yml; #1 is ~950 lines | review workflows, merge in order #1, #3 |
| omnitask-portal #2 #4 | Supabase migrations | review SQL/RLS, merging does not apply them; apply separately with approval |
| omni-vault #3 | adds hub-check workflow, 2000+ lines | review workflow, merge |
| omnitool-knowledge #5 | draft, deletes ~1500 lines, Replit docs | decide keep/close (no-Replit rule) |
| pokemon-unbound-mod-workspace #1 | draft | finish |

## Owner actions
- Add repo secret OPENROUTER_API_KEY in omnitask-mobile and omnitool-knowledge (AI code-review check fails in seconds without it).
- Update remotes to omnitool-knowledge in Working Copy and on the computer.
- Replace old name llm-knowledge-base in omni-vault docs and omnitask-portal seed SQL.
- Stale branches can be deleted after confirmation.
