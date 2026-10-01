---
id: file-digest
type: digest
updated: 2026-10-01
---
# File Digest: three or more useful things per Markdown file

Scope: the 2 uploaded attachments, all Markdown in the omnitask-mobile repo (as of PR #9), the OmniTask working files, and the Markdown outputs and conversations in recent memory (Sep 5 and Sep 28 to Oct 1). Other repos (llm-knowledge-base, cjg-chaosjimgen, emerald-companion) have their own docs: not yet digested (see C5).
Omitted on purpose: one personal relationship reminder inside Prompt-.-Connectors.md. It does not belong in a project repo.

## Uploaded attachments
### Job-Auto-FINAL_PLAN.md (job-automation-suite)
1. Hard invariant: a fit score only ranks the queue; submitting needs mode auto + allowAutoSubmit + a daily cap + a real submitter + an audit log.
2. Step order is deliberate: Greenhouse/Lever (stable public JSON/forms) -> Oracle Always-Free + tunnel -> n8n + Shortcuts -> LinkedIn/Indeed as prepare/approve only.
3. Every step has checkbox acceptance tests; Step 1 (monorepo, 33+16+38 tests) is verified, so Step 2 can start without re-auditing.
4. Safe-by-default security: tunnel (Cloudflare or Tailscale) instead of public ports; rotate any exposed keys.
### Prompt-.-Connectors.md
1. Three reusable prompt seeds: Wojak/MS-Paint sketch prompt, a "beast mode" master-prompt request, and docs links for Sanity HTTP and WebScraping.ai (connector candidates for site audits).
2. meshcore-web-keygen link is a possible small tool to review later (backlog K).
3. The beast-mode request is the spec for 06-PROMPTS/MASTER-PROMPT.md: connectors, best practices, research first, then improve.

## omnitask-mobile repo
### README.md
1. Product shape: Dashboard (agentic to-do), Notes (Export .md with Obsidian frontmatter), Knowledge (client-side keyword search + activity log).
2. Theme contract is testable: #121212 / #BB86FC / #03DAC6, tap targets at least 48px.
3. iPhone install path is Add to Home Screen from Safari: no App Store needed.
4. Backend advice: avoid Cloud Run (billing card), prefer Cloudflare Workers free tier if a proxy is ever needed.
### AGENTS.md (canonical agent rules; CLAUDE.md and copilot-instructions.md must mirror it)
1. Hard rules: no Replit, BYOK/PKCE only, no VITE_ secrets, never merge to main.
2. Workflow: verify with npm ci && build && smoke; update roadmap + ADR in the same PR; Conventional Commits.
3. "Needs human" checklist pattern for anything needing a secret, decision or device.
### CLAUDE.md and .github/copilot-instructions.md
1. Thin pointers to AGENTS.md prevent three rule sets drifting apart.
2. Same pattern should be copied to every repo (portal already done).
3. Copilot instructions double as the standing context for PR review.
### BRAIN.md
1. Format rule: one dated fact per bullet, terse: good atomic-memory format for the vault.
2. Contains personal data and stale tooling facts (Cloudflare auto-deploy, Replit): review before any repo goes public.
3. Designed to be pasted into Custom GPT or Perplexity project instructions: the vault now supersedes it.
### QUICKSTARTGUIDE.md
1. Two-minute local start; no keys needed because the app is local-first.
2. Feature table doubles as a user-facing inventory.
3. Stale: says the AI reviewer is paused, but it is live (DOC-1).
### docs/decision-log.md (ADR-001..009)
1. Dexie over localStorage; plain JS; Replit removed; honest UI labels.
2. ADR-008 BYOK/PKCE rule gates every Phase 3 integration and is why the portal is a separate repo.
3. ADR-009 zero-dependency OpenRouter review script is the cheap AI-review pattern to reuse elsewhere.
### docs/deployment.md
1. Blocker is exact: private repo + free plan cannot use GitHub Pages. Options: public, Pro $4/mo, or Cloudflare Pages.
2. AWS option documented: S3 + CloudFront with GitHub OIDC, about $0-0.50/month, budgets at $1 and $5.
3. Rollback and "do not provision without approval" are written down.
### docs/feature-roadmap.md
1. Priority table P0..P3 with Files, Status, Effort, Decision columns: copy the format for all repos.
2. P0 is merged except P0-5 (visibility) and P0-6 (branch protection).
3. P1-2, P1-3, P1-1, P2-1, P2-5, P2-2, P2-4 are ready to hand to Copilot.
### docs/sync/SYNC.md and cross-repo-issues.md
1. Maps artifacts to destinations: tasks -> Todoist, status -> Perplexity project, BRAIN -> Obsidian.
2. Cross-repo issue drafts are explicitly "do not open until ready."
3. Says a vault-context CLI is not yet created, while knowledge-os-v2 says it exists on a llm-knowledge-base feature branch. Conflict: verify in work package C5.
### docs/project/{PROJECT-STATE, SESSION-HANDOFF, CHANGELOG}.md
1. PROJECT-STATE replaces itself each session; SESSION-HANDOFF replaces; CHANGELOG appends only.
2. Handoff lists open PRs, Needs-human items and the next three actions.
3. Gives any new agent a cold start in under a minute.
### .github/skills/code-review/SKILL.md
1. Three severity tags: BLOCKER, SHOULD-FIX, NIT, with a fixed output contract.
2. Scope boundaries stop pedantic reviews: security, data loss, rule violations first.
3. Documents the MAX_PATCH guard that exposed bug R-1.

## OmniTask working files (this project)
### PHASE1-AUDIT.md
1. Verified baseline: npm ci, build, 6/6 smoke, npm audit 2 dev-chain vulns.
2. Root cause of the red AI-review check (undefined MAX_PATCH_LENGTH) and its two-line fix.
3. Stale-doc list and the owner-only blockers.
### CHANGELOG.md and CONTINUATION-PROMPT.md
1. Newest-first changelog entries with Done / Found stale / Next.
2. Continuation prompt is self-propagating: blanks marked [INSERT], emits a fresh copy at the end.
3. Connector list and source list belong inside the prompt.
### perplexity/omnitask-mobile-project-instructions.md
1. Compact Project instructions: rules, source-of-truth order, connectors, end-of-task format.
2. Replaces stale Phase 0 instructions in the Perplexity Project.
3. Keep under 8k characters.

## Recent conversations and outputs
### omnitask-knowledge-os-v2.md
1. Decision: Obsidian Markdown canonical, Supabase for metadata, chunks, graph edges, embeddings, provenance.
2. Storage ownership matrix: tasks -> Todoist, code -> GitHub, photos -> Google Photos, attachments -> Drive.
3. Never start with bulk cleanup: read-only inventory, backups, stable IDs, dry-run manifests, restore tests, then object-level approvals.
4. Keep llm-knowledge-base and game repos separate.
### yungfloop-autoedit-test-1.md
1. Experiment contract: 20 sets x 6 drafts, AutoEdit on, Bugsquelcher dial 0-5 as a restraint modifier, not a voice replacement.
2. Evidence rule: generated drafts are negative evidence until the user marks keep or post.
3. Model self-scores are provisional triage; ratings from the user are truth.
### Session 07016c31 (Yungfloop + planning)
1. PR #2 in cjg-chaosjimgen holds the experiment.
2. A paid Apify run for more samples was never approved: gate it.
3. The follow-up design package was exploratory, not authorization to reorganize anything.
### Session f4ade4a4 (manga pipeline + Copilot prompts)
1. Manga system = ComfyUI generation + Markdown memory router, kept separate from OmniTask.
2. Principles worth reusing: Markdown canonical, retrieval before generation, human-controlled memory, reproducible generations, replaceable adapters.
3. A manager-agent review pass removed unverified claims: keep that review step.
4. Checkpointed prompts: stop and wait for approval after each checkpoint.
### Session 3f5b9852 (deploy prompt, Sep 5)
1. Founding prompt: no Replit, compare AWS to free hosts, one core feature at a time.
2. Retain/improve/defer/cut framework for features.
3. Confirmation required before paid resources or default-branch pushes.
### Session 0b42e327 (Cygwin installer, tmux, noctty)
1. The installer .bat mostly works; the weak link is apt-cyg (lightly maintained).
2. noctty is minimal: get Warp-like behavior by layering tmux and shell config.
3. A tmux.conf plus reload gives a cohesive base; useful for the PC side of remote development.
### Summaries (sessions_index, asset_index, changelog)
1. Index files list which sessions exist and which assets were produced.
2. Use them to find a transcript before asking the user to repeat context.
3. Treat memory/ as read-only.
