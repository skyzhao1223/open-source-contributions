# Open Source Contributions

[![PRs merged](https://img.shields.io/badge/merged%20PRs-21-2ea44f?style=flat-square)](https://github.com/skyzhao1223/open-source-contributions)
[![Repositories](https://img.shields.io/badge/repositories-12-blue?style=flat-square)](https://github.com/skyzhao1223/open-source-contributions)
[![Lines](https://img.shields.io/badge/lines-%2B7.3k-informational?style=flat-square)](https://github.com/skyzhao1223/open-source-contributions)

Merged contributions into repositories I don't own — mostly AI agent runtimes, developer tooling and frontend infrastructure.
**21 merged PRs across 12 repositories** (2 projects above 200k stars, 5 above 30k), all reviewed and merged by their maintainers.

- 🔧 **Root-cause fixes** in [openclaw](https://github.com/openclaw/openclaw) (392k★), [DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) (35.8k★) and [FastGPT](https://github.com/labring/FastGPT) (29.8k★) — each shipped with regression tests.
- 🧪 **Built the test & CI foundation** for [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) (12k★): Vitest unit tests, a smoke-render harness over all 57 demos, two new CI jobs.
- 🚀 **Features**: buyer auto-messaging in [xianyu-auto-reply](https://github.com/zhinianboke/xianyu-auto-reply) (7.6k★), prompt-complexity model routing in [Codewhale](https://github.com/codewhale-hq/Codewhale) (41k★).

## Merged pull requests

| Repository | Stars | PR | Merged | Diff | What it does |
|---|---|---|---|---|---|
| [`openclaw`](https://github.com/openclaw/openclaw) | 392k★ | [#172379](https://github.com/openclaw/openclaw/pull/172379) | 2026-10-15 | +107/−6 | Fixed a Windows credential-staging failure where a cleanup `EBUSY`/`EPERM` **masked the real provider setup result** (false failure) — cleanup now retries and degrades to a warning without replacing the outcome. 4 parameterized regression cases. |
| [`opencode`](https://github.com/anomalyco/opencode) | 214k★ | [#42034](https://github.com/anomalyco/opencode/pull/42034) | 2026-08-12 | +3/−3 | Fixed provider config example and PAT doc typos. |
| [`opencode`](https://github.com/anomalyco/opencode) | 214k★ | [#42048](https://github.com/anomalyco/opencode/pull/42048) | 2026-08-12 | +2/−2 | Replaced two 404 docs links (DigitalOcean Inference Routers, opencode-daytona) with verified URLs. |
| [`Codewhale`](https://github.com/codewhale-hq/Codewhale) | 41k★ | [#5257](https://github.com/codewhale-hq/Codewhale/pull/5257) | 2026-08-08 | +274/−2 | Added `model = "auto"`: a rule-based prompt-complexity classifier that routes between pro and flash tiers before the TUI starts. |
| [`ant-design-pro`](https://github.com/ant-design/ant-design-pro) | 38.9k★ | [#11476](https://github.com/ant-design/ant-design-pro/pull/11476) | 2025-06-04 | +1/−1 | antd v5 deprecation migration — `destroyOnClose` → `destroyOnHidden`. |
| [`DeepSeek-Reasonix`](https://github.com/esengine/DeepSeek-Reasonix) | 35.8k★ | [#7309](https://github.com/esengine/DeepSeek-Reasonix/pull/7309) | 2026-08-04 | +126/−1 | Fixed subagent metadata timestamps (`CreatedAt` recorded completion time) and made storage failures converge to `failed` instead of a stuck `running`. |
| [`DeepSeek-Reasonix`](https://github.com/esengine/DeepSeek-Reasonix) | 35.8k★ | [#7708](https://github.com/esengine/DeepSeek-Reasonix/pull/7708) | 2026-08-06 | +370/−7 | Fixed a **permanent session hang**: SSE clients attaching after an approval was queued never received the parked prompt — now replays pending interactions on subscribe. +283 lines of tests. |
| [`DeepSeek-Reasonix`](https://github.com/esengine/DeepSeek-Reasonix) | 35.8k★ | [#7709](https://github.com/esengine/DeepSeek-Reasonix/pull/7709) | 2026-08-06 | +71/−5 | Fixed the desktop todo panel freezing at "In Progress" during long turns by preferring live `todo_write` events over stale metadata. |
| [`FastGPT`](https://github.com/labring/FastGPT) | 29.8k★ | [#7590](https://github.com/labring/FastGPT/pull/7590) | 2026-08-25 | +140/−3 | Root-caused "exported backup cannot be re-imported": header-only/single-row CSVs triggered a parser delimiter heuristic that was treated as invalid data. Full service suite (3,897 tests) green. |
| [`FastGPT`](https://github.com/labring/FastGPT) | 29.8k★ | [#7591](https://github.com/labring/FastGPT/pull/7591) | 2026-08-25 | +121/−121 | Normalized zh-CN typography across the RAG guide (textlint errors 98 → 4), diff stays line-for-line neutral. |
| [`awesome-dsh-plugin`](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | 18.8k★ | [#5777](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin/pull/5777) | 2026-09-23 | +6/−0 | Listed my `dsh-agent-token-stats` plugin in the DSH plugin marketplace. |
| [`video-shotcraft`](https://github.com/Vincentwei1021/video-shotcraft) | 12k★ | [#39](https://github.com/Vincentwei1021/video-shotcraft/pull/39) | 2026-08-21 | +291/−1 | Added `ClipCard` so the library's 152 shot cards can drive **real video footage** for the first time; fixed crossfade audio stacking, `startFrom` loop freeze and layer-count boundaries per maintainer review. |
| [`video-shotcraft`](https://github.com/Vincentwei1021/video-shotcraft) | 12k★ | [#40](https://github.com/Vincentwei1021/video-shotcraft/pull/40) | 2026-08-25 | +1989/−23 | Extracted 9 shot cards that only existed inside full-scene components into self-contained, copy-pasteable demos. |
| [`video-shotcraft`](https://github.com/Vincentwei1021/video-shotcraft) | 12k★ | [#41](https://github.com/Vincentwei1021/video-shotcraft/pull/41) | 2026-08-25 | +311/−6 | Implemented the 3 missing transition recipes (dark-tunnel, focus-handoff, black-card). |
| [`video-shotcraft`](https://github.com/Vincentwei1021/video-shotcraft) | 12k★ | [#42](https://github.com/Vincentwei1021/video-shotcraft/pull/42) | 2026-08-21 | +1812/−0 | Project had **zero tests** — introduced Vitest with 23 unit cases for the deterministic animation helpers, plus a CI job. |
| [`video-shotcraft`](https://github.com/Vincentwei1021/video-shotcraft) | 12k★ | [#43](https://github.com/Vincentwei1021/video-shotcraft/pull/43) | 2026-08-21 | +188/−1 | Added a smoke-render script covering all 57 demos (first-frame render assertions), closing the "compiles but crashes at runtime" blind spot. CI job added. |
| [`video-shotcraft`](https://github.com/Vincentwei1021/video-shotcraft) | 12k★ | [#48](https://github.com/Vincentwei1021/video-shotcraft/pull/48) | 2026-08-25 | +66/−1 | Documented the new test suite and full `ClipCard` parameter table in SKILL.md / demos README. |
| [`munder-difflin`](https://github.com/HarnessMD/munder-difflin) | 8.8k★ | [#412](https://github.com/HarnessMD/munder-difflin/pull/412) | 2026-09-06 | +8/−5 | Fixed queued messages being silently held by a half-typed terminal draft, with the "held" hint only appearing after the agent idled. |
| [`xianyu-auto-reply`](https://github.com/zhinianboke/xianyu-auto-reply) | 7.6k★ | [#332](https://github.com/zhinianboke/xianyu-auto-reply/pull/332) | 2026-09-19 | +384/−1 | Shipped "auto-message the buyer after a positive review" across three rating paths, with per-order dedup, failure isolation, platform-block detection, timeout idempotency and DB migration. |
| [`translated-content`](https://github.com/mdn/translated-content) | 2k★ | [#380](https://github.com/mdn/translated-content/pull/380) | 2021-04-14 | +1/−1 | zh-CN content fix in the JavaScript `void` operator page. |
| [`zspace_skill`](https://github.com/coracoo/zspace_skill) | 28★ | [#6](https://github.com/coracoo/zspace_skill/pull/6) | 2026-08-06 | +765/−6 | Added the `media-naming` skill: read-only compliance scanning for media library naming, with write ops gated behind MCP confirmation. |

> Stars are snapshots at the time of writing. Diffs include generated lock files where applicable.

<details>
<summary><b>Also opened — 21 PRs awaiting maintainer review</b> (not counted above)</summary>

Fixes and listings I opened that have not been merged yet. Listed for transparency; they are **not** part of the 21 merged PRs above.

| Repository | PRs | Theme |
|---|---|---|
| [coze-studio](https://github.com/coze-dev/coze-studio) · 21.7k★ | 16 | nil dereference, panic recovery, shared mutable state, SQL wildcards, float NaN, concurrent cache races |
| [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) · 96k★ | 3 | listing my MCP servers / CLI tools |
| [AionUi](https://github.com/iOfficeAI/AionUi) · 33.5k★ · [AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) · 7.3k★ | 2 | chat text parsing fix; tolerate single-worker failures |

</details>

## 中文说明

本仓库汇总我在**第三方开源项目**中已合并的 Pull Request（不含自建项目）。21 个已合并 PR 覆盖 12 个仓库，其中 2 个 20 万 star 级、5 个 3 万 star 以上；重点在 AI Agent 运行时、开发工具链与前端基础设施，全部经维护者 review 后合并。

## Maintenance

Curated manually; star counts are snapshots. Verified against the GitHub API
(`author:skyzhao1223 type:pr is:merged`) on 2026-10-16.

## License

MIT — see [LICENSE](LICENSE). Content is descriptive; linked projects keep their own licenses.

