# Token and credit saving playbook (Computer first)

Updated 2026-10-01. Ranked by how often a method repeats across Reddit and GitHub sources, not by a popularity count. Savings figures are the authors' claims, not measured by us. TODO: measure our own credits per task for two weeks.

## A. Perplexity Computer (10)
| # | Method | Source |
|---|---|---|
| 1 | Plan, brainstorm and write the prompt in regular chat or Search (or Gemini/OpenRouter), then paste one finished, precise prompt into Computer. Precise prompts cut about 20% (commenter claim). | [Reddit: Yikes Max plan](https://www.reddit.com/r/perplexity_ai/comments/1vcmbv2/yikes_max_plan_crecit_consumption/), [Reddit: using Computer without burning credits](https://www.reddit.com/r/perplexity_ai/comments/1setno8/how_are_you_actually_using_computer_without/) |
| 2 | Do not use Computer as a search engine. Use Search or Pro Search for lookups (one guide says they do not cost credits; verify on your plan). Check each Space's default toggle (Computer vs Search). | [Reddit: Yikes](https://www.reddit.com/r/perplexity_ai/comments/1vcmbv2/yikes_max_plan_crecit_consumption/), [Karozi gist](https://gist.github.com/karozi/d5ae62a0c4c965cceedd1e7c3925b049/f7368be7d89d677e8007c7a4c55380ede06dfdfa) |
| 3 | Fresh thread per task. Long threads re-pay their whole context on every step. | [Karozi guide part 2](https://gist.github.com/karozi/395d6c2354eb56b761cfc07b5ec5205c) |
| 4 | Script instead of converse: have Computer write a script once, then run it yourself or in CI. A headless Playwright script is far cheaper than an agent driving a browser. | [Karozi guide](https://gist.github.com/karozi/395d6c2354eb56b761cfc07b5ec5205c), [Reddit thread](https://www.reddit.com/r/perplexity_ai/comments/1setno8/how_are_you_actually_using_computer_without/) |
| 5 | Tier or cancel recurring automations. Light effort for routine runs, weekly instead of daily. | [Karozi guide](https://gist.github.com/karozi/395d6c2354eb56b761cfc07b5ec5205c), [Reddit: Token Pyromaniac](https://www.reddit.com/r/perplexity_ai/comments/1u610ql/perplexity_computer_token_pyromaniac/) |
| 6 | Audit skills and add a terse-output instruction. A drop-in token-efficient SKILL.md exists for Computer. | [get-zeked](https://github.com/get-zeked), [Karozi guide](https://gist.github.com/karozi/395d6c2354eb56b761cfc07b5ec5205c) |
| 7 | Save reports and results to files and refer to the file instead of re-pasting. | [Karozi guide](https://gist.github.com/karozi/395d6c2354eb56b761cfc07b5ec5205c) |
| 8 | Ask for fewer subagents on simple tasks and use structured prompts. | [Reddit thread](https://www.reddit.com/r/perplexity_ai/comments/1setno8/how_are_you_actually_using_computer_without/) |
| 9 | Prefer DOM or accessibility-tree tools over screenshot agents (commenter claims about 10x cheaper; unverified). | [Reddit thread](https://www.reddit.com/r/perplexity_ai/comments/1setno8/how_are_you_actually_using_computer_without/) |
| 10 | Use the top model or high effort only when needed, and stop runaway loops early (one user reports a 5,000-credit loop). | [Reddit: Token Pyromaniac](https://www.reddit.com/r/perplexity_ai/comments/1u610ql/perplexity_computer_token_pyromaniac/), [Reddit: credit usage](https://www.reddit.com/r/perplexity_ai/comments/1rmfqvh/perplexity_computer_credit_usage/) |

## B. General agents: memory, context, cost (10)
| # | Method | Source |
|---|---|---|
| 11 | Prompt caching: stable instructions first, volatile content last; no timestamps in the prefix; keep tool order fixed. Reports of 93-99% hit rates. | [Reddit: cache hit rate](https://www.reddit.com/r/AI_Agents/comments/1vzq98j/stop_shortening_your_prompts_six_agents_9799/) |
| 12 | Compact or clear on a threshold (for example 40k tokens), and start fresh with a short brief after failed attempts. Do it while the cache is warm. | [Reddit: optimize token spend](https://www.reddit.com/r/AI_Agents/comments/1way89s/what_is_everyone_doing_to_optimize_token_spend/), [khasky guide](https://github.com/khasky/claude-code-token-optimization) |
| 13 | Filter command output before it reaches the model (rtk claims 60-90% on common dev commands). | [rtk](https://github.com/rtk-ai/rtk) |
| 14 | Load tools and large outputs on demand instead of eagerly (Cursor reports 46.9% less context). | [awesome-ai-tokenomics](https://github.com/QuesmaOrg/awesome-ai-tokenomics) |
| 15 | Prune the always-loaded surface: unused MCP servers, plugins, long instruction files; prefer a CLI over an MCP when equal. | [khasky guide](https://github.com/khasky/claude-code-token-optimization) |
| 16 | Persistent memory layer so sessions start from a summary, not a replay (mem0, Zep). Ours: PROJECT-STATE.md, SESSION-HANDOFF.md and this vault. | [mem0](https://github.com/mem0ai/mem0), [awesome-llm-token-reduction](https://github.com/congvmit/awesome-llm-token-reduction) |
| 17 | Prompt compression (LLMLingua, up to 20x claimed) for long documents sent to a cheap model. | [LLMLingua](https://github.com/microsoft/llmlingua) |
| 18 | Compact data formats for structured input (TOON claims 30-60% on uniform data; YAML over verbose JSON). | [awesome-llm-token-reduction](https://github.com/congvmit/awesome-llm-token-reduction) |
| 19 | Route by task: frontier model for planning and review, fast or free model for lookups and simple edits. | [Reddit: optimize token spend](https://www.reddit.com/r/AI_Agents/comments/1way89s/what_is_everyone_doing_to_optimize_token_spend/) |
| 20 | Hard caps and measurement: iteration limits in code, context caps, cost per completed task, fix contradictory rules before enabling automation. | [Reddit: cache hit rate](https://www.reddit.com/r/AI_Agents/comments/1vzq98j/stop_shortening_your_prompts_six_agents_9799/), [Reddit: optimize token spend](https://www.reddit.com/r/AI_Agents/comments/1way89s/what_is_everyone_doing_to_optimize_token_spend/) |

## C. Routing: what needs Computer
| Task | Use |
|---|---|
| Connector actions (GitHub, Supabase, Todoist, Drive, Notion), cross-tool jobs, file builds, browser work, deploys, live QA | Computer |
| Brainstorming, planning, prompt drafting, summarizing pasted text, explaining code, README or doc wording | Gemini or OpenRouter free (portal Assistant tab once the key is set) |
| Yungfloop draft generation and rating | Gemini or OpenRouter |
| In-repo code, tests, CI, dependency bumps | GitHub Copilot cloud agent (one checkpoint per session) |
| Lookups and quick facts | Perplexity Search, not Computer |
| Repeating jobs | GitHub Actions or a script, not a Computer automation |

## D. Our rules (adopted 2026-10-01)
1. Draft prompts outside Computer; send one precise prompt with the exact files, repo and stop condition.
2. One task per thread. Handoff block after about 10 messages or an hour (set in project instructions).
3. Start every Computer task from docs/project/PROJECT-STATE.md, not chat history.
4. Results go to files in the repo or vault; chat answers stay short.
5. No recurring Computer automations unless approved; prefer GitHub Actions.
6. Ask for at most one subagent unless the task is clearly parallel.
7. Stop a task that loops or repeats the same tool call twice.

## E. Still to do (owner or Computer)
- Pick one free Gemini or OpenRouter chat as the default drafting tool and keep its prompt template in 06-PROMPTS.
- Track credits per task in a note for two weeks, then revise this page.
- Optional: install the get-zeked token-efficient skill after reading it.
- Optional on the PC only: rtk for any local coding agent.
