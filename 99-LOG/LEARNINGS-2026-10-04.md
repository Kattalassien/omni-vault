---
id: learnings-2026-10-04
type: log
project: omni-vault
status: active
updated: 2026-10-04
---
# Learnings 2026-10-04

The most valuable things learned in the 2026-10-04 sessions (QuickConsole, the Omni hub, the PR review, and browser automation planning). Durable one-liners are in BRAIN.md. This file holds the detail.

## 1. Git and PR workflow
| Learning | Rule going forward |
|---|---|
| Squash-merging a stacked PR (base = another PR's branch) puts the work on that branch, not main. omnitask-mobile #9–#11 were lost this way. | Merge stacks top-down: child into parent first, then parent into main. Or rebase the child onto main and retarget it before merging. |
| After a parent is squash-merged, the child's diff still contains the parent's original commits and can conflict. | `git rebase --onto origin/main <old-parent-branch> <child>`, then `gh pr edit N --base main`. |
| A commit reached omnitask-mobile main without a PR (0e7c19b). | Turn on branch protection for main: require a PR and passing `test`. TODO: owner decision. |
| Red "review" checks were AI reviewers that need OPENROUTER_API_KEY or GitHub Models quota. | Treat AI review as advisory. Required checks are tests and lint only. Pin third-party actions to a commit SHA. |
| A stray `gws.err` file got committed. | Add tool stderr files (`*.err`) to .gitignore and run `git status` before every commit. |
| Repo renames (llm-knowledge-base → omnitool-knowledge) leave old names in docs and seeds. | Keep stable slugs and add `former_names` in 08-CONFIG/projects.json. |

## 2. Knowledge sharing across repos
- Hub plus managed blocks was chosen over a git submodule or Supabase as the source of truth. It works on iPhone, every repo stays self-contained, and changes are reviewable PRs.
- Markers: `<!-- omni:begin core v1 -->` … `<!-- omni:end core -->`. Facts that belong to one repo go under `## Facts learned`, and harvest collects them.
- Mirrors are write-only copies: Supabase kb_docs (117 docs at the first load), Drive "Omni Knowledge Hub" (IDs in 08-CONFIG/drive-index.json), and Notion "Omni Knowledge Hub" with the Omni Projects database.

## 3. Connectors and limits
- **Todoist Free:** the project cap and saved-filter cap are both reached. Use sections in "Dev Projects", labels, and `omni-key:` dedupe.
- **Supabase:** run `execute_sql` in chunks of about 120 KB. Use `security_invoker` on views. RLS uses `is_admin()`.
- **Drive (gws):** upload paths must be relative to the working directory. Update files in place by fileId; never permanently delete.
- **Notion:** fetch the database schema before creating rows. Dates are written as `date:<prop>:start`.
- **Cloudinary:** text overlays need commas double-encoded (`%252C`).
- **CloudConvert:** ask before any job (cost rule).
- **Perplexity:** automations are "Omni knowledge sync" (Sun 20:00), "Omni roadmap to Todoist" (weekdays 07:30) and "Omni standards audit" (1st, 08:00). The skills connector-router and omni-hub-sync are in My Skills.

## 4. Browser automation project: research notes (plan stage, no repo yet)
Status: planning only. A repo will be created after Preston approves the name, owner and plan.

| Fact | Source |
|---|---|
| A content script runs in an isolated world: it shares the DOM, not JS globals, with the page. | https://developer.chrome.com/docs/extensions/reference/manifest/content-scripts |
| `activeTab` gives temporary access only after a user gesture (action, context menu, keyboard command), shows no install warning, and is revoked on cross-site navigation. | https://developer.chrome.com/docs/extensions/develop/concepts/activeTab |
| An MV3 service worker stops after about 30 s idle, after a request longer than 5 min, or after a fetch response slower than 30 s. Persist state; don't rely on globals. | https://developer.chrome.com/docs/extensions/develop/concepts/service-workers/lifecycle |
| `chrome.storage.local` holds about 10 MB unless `unlimitedStorage` is granted. | https://developer.chrome.com/docs/extensions/reference/api/storage |
| Safari packaging: `xcrun safari-web-extension-packager <dir>` (previously `-converter`) needs a Mac with Xcode; `--ios-only`/`--macos-only`; there is a web packager in App Store Connect. | https://developer.apple.com/documentation/safariservices/packaging-a-web-extension-for-safari |
| WXT builds Safari with `wxt build -b safari`, then you run the Apple packager on `.output/safari-mv3`. It also has `createShadowRootUi` for an isolated panel. | Context7 /wxt-dev/wxt (https://wxt.dev) |
| Userscripts for Safari (quoid) needs iOS 15.1+ or macOS 12+/Safari 14.1+ and is GPL-3.0. The iOS app has no editor. | https://github.com/quoid/userscripts |
| `dispatchEvent()` and `HTMLElement.click()` produce events with `isTrusted === false`. Some sites ignore them, and they must never be used to get around site controls. | https://developer.mozilla.org/en-US/docs/Web/API/Event/isTrusted |
| Navigation API `navigate` events help detect SPA route changes (Chromium; check Safari support before relying on it). | https://developer.mozilla.org/en-US/docs/Web/API/Navigation/navigate_event |
| Prefer role- and name-based targeting (Playwright `getByRole` model) over brittle CSS selectors. | https://playwright.dev/docs/locators |
| OpenRouter structured outputs: `response_format: {type: "json_schema", json_schema: {name, strict: true, schema}}` plus `provider.require_parameters: true`. Support varies by provider, so always validate locally. | https://openrouter.ai/docs/guides/features/structured-outputs |
| OpenRouter limits: 402 means out of credits or in-flight budget, 429 means rate-limited. Free models allow 20 requests/min and 50/day (1,000/day with 10+ credits). | https://openrouter.ai/docs/api_reference/limits |
| Chrome DevTools Recorder exports JSON user flows that @puppeteer/replay (Apache-2.0) can replay. A good reference for the recording format. | https://developer.chrome.com/docs/devtools/recorder/reference |

Prior art, with licenses checked through the GitHub API on 2026-10-04:

| Project | License | Use |
|---|---|---|
| puppeteer/replay | Apache-2.0 | Step schema reference (selectors array, assertedEvents) |
| SeleniumHQ/selenium-ide | Apache-2.0 | Command vocabulary and locator fallbacks |
| microsoft/playwright | Apache-2.0 | Locator priority and auto-wait concepts (ideas only) |
| rrweb-io/rrweb | MIT | Patterns for recording DOM events and masking inputs |
| antonmedv/finder, fczbkk/css-selector-generator | MIT | Generating unique selectors (possible dependency) |
| eps1lon/dom-accessibility-api | MIT | Accessible name computation for role/name targeting |
| testing-library/dom-testing-library | MIT | ByRole/ByLabelText query model |
| dequelabs/axe-core | MPL-2.0 | Accessibility checks (file-level copyleft; use as a dependency only) |
| wxt-dev/wxt | MIT | Cross-browser build tool |
| violentmonkey/violentmonkey | MIT | Userscript manager reference |
| nanobrowser/nanobrowser | Apache-2.0 | LLM-agent extension design (planner/navigator split); reference only |
| browser-use/browser-use | MIT | Agent action schema ideas (Python; reference only) |
| AutomaApp/automa | AGPL-3.0 + commercial | Rejected as a code source (AGPL). Block-workflow UX ideas only |
| Tampermonkey/tampermonkey, quoid/userscripts | GPL-3.0 | Run our script inside them; don't copy their code |
| A9T9/RPA (UI.Vision) | TODO: license header unclear | Ideas only until the license is confirmed |
