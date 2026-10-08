# Best Claude Code Mods

**Hand-picked, validated, pinned. One add, 45 mods.**

A Claude Code plugin marketplace of **mods**: plugins made of function hooks that
watch, rewrite or answer what Claude Code does and draw their own UI. Add it once and
install any mod below by name: a few written here, and community mods we picked,
validated and pinned to a checked commit.

Needs Claude Code 2.1.287 or later. [中文说明](#中文说明)

## Install

In a Claude Code terminal session:

```
/plugin marketplace add claude-code-mods/best-claude-code-mods
/plugin install <mod>@best-claude-code-mods
```

For example `/plugin install terminal-browser@best-claude-code-mods`. Run
`/plugin marketplace update best-claude-code-mods` to pick up new mods and new pins.

## Catalogue

Every community mod is listed as its author published it, pinned to the commit we
checked with `claude plugin validate`; the link goes to that commit. **Reaches** is
what the validator reports the mod's code can do beyond drawing UI: open network
connections, run commands, call a model, read or write files, use MCP servers. Read a
mod's source before installing it. Validation reads code without running it; it is
not a security audit.

<!-- catalog:start -->
### From this repo · 本仓库自制

| Mod | What it does | 说明 | Reaches |
| --- | --- | --- | --- |
| [`env-guard`](env-guard) | Refuses reads and edits of .env files. | 拒绝 Claude 读取或修改 .env 文件 | — |
| [`turn-band`](turn-band) | A row above the prompt with the last turn's time and tool-call count. | 输入框上方显示上一轮用时和工具调用次数 | — |

### Dashboards and usage · 仪表盘与用量

| Mod | What it does | 说明 | Reaches |
| --- | --- | --- | --- |
| [`cache-clock`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/cache-clock)<br><sub>by hamzafer</sub> | A prompt-cache line under your status line: minutes left while warm, and how many tokens the next message re-caches once cold. /cache-clock setup adds it. | 状态栏下一行：提示缓存还热几分钟，冷了以后下一条要重新缓存多少 token | files, runs commands |
| [`context-bar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/context-bar)<br><sub>by hamzafer</sub> | Your context window as a stacked bar above the prompt, a color per category, with token counts and the compaction point. /context-bar shows or hides it. | 上下文窗口按类别分色的堆叠条，含 token 数和压缩点（/context-bar 开关） | — |
| [`openai-balance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/openai-balance)<br><sub>by hamzafer</sub> | Your OpenAI API credit above the prompt: an estimated balance with a gauge, today's spend, where the money mostly went, and the last call. /openai-balance shows the breakdown. | OpenAI API 余额估算、今日花费和主要去向（/openai-balance） | network, runs commands |
| [`token-weather`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/token-weather)<br><sub>by hamzafer</sub> | A live forecast of the context window, with a prompt-cache countdown, drawn above the prompt. | 把上下文占用画成天气预报，附提示缓存倒计时 | files, runs commands |
| [`usage-meter`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/usage-meter)<br><sub>by hamzafer</sub> | Your plan's 5-hour and 7-day usage as small bars above the prompt, with the reset countdown and the session's cost. | 5 小时和 7 天用量小进度条，带重置倒计时和本会话费用 | — |
| [`usage-band`](https://github.com/JetsonChan/CC-Usage-Band/tree/60cd60949b1f52c96ddba3ea24ed0848ff302196/usage-band)<br><sub>by JetsonChan</sub> | A band above the prompt showing your 5-hour and 7-day limits, context window and prompt-cache hit rate, styled for the terminal and the desktop app | 输入框上方显示 5 小时/7 天限额、上下文和缓存命中率，终端和桌面版都适配 | — |
| [`context-view`](https://github.com/kongyo2/context-view/tree/137e4e3db754684144ec953c5e66085bc2959766)<br><sub>by kongyo2</sub> | The context window as one row above the prompt, drawn the way Claude Code draws its own meters: the context's cells, the percentage used, the tokens over the window, and the tokens left before auto-compact. /context-view hides and shows it. | 一行显示上下文占用，样式同 Claude Code 自带的仪表，含距自动压缩还剩多少 | — |
| [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/f31daca523d36c501cd0df23a737a44c7dc56ad6)<br><sub>by scasella</sub> | Flightdeck: a live agent dashboard for Claude Code. Main model vitals, an on-call architect, every permission check, subagent cards and swimlanes, a turn receipt and a session log, all from real session events | agent 仪表盘：模型状态、每次权限判定、子 agent 卡片和泳道、本轮小票、会话日志 | — |
| [`cctop`](https://github.com/tomstagl/cctop/tree/6ceafc34a972f4e58d5e53b1c69f80e2a9759d41/plugin)<br><sub>by tomstagl</sub> | btop-style live dashboard for Claude Code internals: /cctop opens it in a side pane, cctop-insights lets the session answer questions from its numbers | btop 风格的实时面板：上下文、token、费用、缓存命中、限额、各工具耗时（/cctop） | files, runs commands |
| [`statuspane`](https://github.com/xuanji86/claude-statuspane/tree/13bd8e46edefdf282f117941b886cb529c7d79c3)<br><sub>by xuanji86</sub> | A floating status card above the Claude Code prompt — model, effort, context, 5h/week limits, cost, directory and branch, GitHub CI and deploys — with clickable settings and a progress-row API any script or mod can feed. | 输入框上方的浮动状态卡：模型、effort、上下文、5h/周限额、费用、分支、CI | files, runs commands |
| [`plan-progress`](https://github.com/zycck/claude-mods/tree/3539d02d7435397d293e3120ebad22c23214f6c0/plugins/plan-progress)<br><sub>by zycck</sub> | Live plan progress bars above the Claude Code prompt: stages, steps, a pixel fill and soft sounds for decision, error and done | 输入框上方的计划进度条：阶段、步骤、像素填充，决策/出错/完成时有提示音 | files, runs commands |

### Agents and subagents · Agent 与子 agent

| Mod | What it does | 说明 | Reaches |
| --- | --- | --- | --- |
| [`agent-flow`](https://github.com/Charlie0113-T/claude-agent-flow/tree/d87b2559dec03979e088026e8f48aee5f9d2cab5)<br><sub>by Charlie0113-T</sub> | The agent flow pane: /flow opens a live tree of the session's subagents and teammates beside the transcript, fed by engine events, with a text fallback where no pane can be drawn. | /flow 在对话旁打开子 agent 和队友的实时树状图 | — |
| [`agent-radar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/agent-radar)<br><sub>by hamzafer</sub> | One live line above the prompt per running subagent: time, tool count and what it's doing. /radar shows every agent and its messages. | 每个运行中的子 agent 一行：用时、工具次数、正在做什么（/radar 看全部） | — |
| [`browser-lanes`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/browser-lanes)<br><sub>by hamzafer</sub> | Shows if this session has a Playwright browser and who holds it. /browser clean closes leftover browsers. A subagent that wants the browser waits until the one using it is done. | 显示 Playwright 浏览器被谁占用；子 agent 要用浏览器时排队，/browser clean 清理残留 | runs commands |
| [`mission-control`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/mission-control)<br><sub>by hamzafer</sub> | /mission opens a live map of the main agent, its subagents and every tool call, plus a code map of the files they touch. | /mission 打开主 agent、子 agent 和所有工具调用的实时地图，外加文件代码地图 | files, model calls, runs commands |
| [`review-watch`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/review-watch)<br><sub>by hamzafer</sub> | A live line above the prompt for each running code review: Codex or a review subagent, its model, what it reviews, time, and Codex's latest output. A toast with the findings when it ends. | 每个进行中的代码审查（Codex 或审查子 agent）一行实时状态，结束时弹出结论 | runs commands |
| [`switchboard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/switchboard)<br><sub>by hamzafer</sub> | Picks the model for each subagent that names none, with OpenAI's Decisions API or Jev, from its short label only. One line per spawn above the prompt; /route shows each pick and what each subagent cost. | 为没指定模型的子 agent 自动选模型（调用 OpenAI Decisions API 或 Jev），/route 看选择和花费 | network |
| [`agentpane`](https://github.com/xuanji86/claude-agentpane/tree/17be88979e5782591a2a184959df1c4168600066)<br><sub>by xuanji86</sub> | A side pane for Claude Code that lists the subagents a session runs, what each is doing and what it costs in tokens, with each one's conversation a click away. | 侧边面板列出子 agent：各自在做什么、花了多少 token，点开看它的对话 | — |

### Productivity and context · 效率与上下文

| Mod | What it does | 说明 | Reaches |
| --- | --- | --- | --- |
| [`glance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/glance)<br><sub>by hamzafer</sub> | One line above the prompt with what needs you: next meeting, PRs, Linear issues and Slack DMs. /glance lists them all. | 一行显示需要你处理的事：下一个会议、PR、Linear 任务、Slack 私信（走已连接的 MCP） | MCP, runs commands |
| [`next-steps`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/next-steps)<br><sub>by hamzafer</sub> | After each turn, 2 or 3 likely next prompts above the prompt. Press 1, 2 or 3 in an empty prompt to draft one, 0 to dismiss. | 每轮结束后给出 2–3 个可能的下一条提示，空输入框里按 1/2/3 选用 | model calls |
| [`session-saver`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/session-saver)<br><sub>by hamzafer</sub> | Names untitled sessions through unpause. /park saves where you left off, and a resumed session shows it. | 给未命名会话起名；/park 记下进度，恢复会话时显示 | model calls, runs commands |
| [`where-am-i`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/where-am-i)<br><sub>by hamzafer</sub> | A live recap above the prompt: goal, doing now, waiting on you, next. /where for a longer one. | 输入框上方实时小结：目标、正在做、等你处理、下一步（/where 看详细） | model calls |
| [`aside`](https://github.com/JayDoubleu/aside/tree/cf2b7562ae7b376cdcf9e2436a926aba77dc759f)<br><sub>by JayDoubleu</sub> | Read-only side chat: /aside opens a pane beside the transcript where you ask about the session so far; answers come from a tool-less fork of the session's own transcript and nothing is written back into the main thread. | 只读旁聊：/aside 在侧边问关于当前会话的问题，不写回主对话 | model calls |
| [`lcm`](https://github.com/lossless-claude/lcm/tree/0c17dbffda452cf7fae46929af427dff355aeaa3)<br><sub>by lossless-claude</sub> | Lossless context management — DAG-based summarization that preserves every message | 无损上下文管理：用 DAG 做分层摘要，每条消息都还能找回 | files, network, model calls, runs commands |

### Rendering and previews · 渲染与预览

| Mod | What it does | 说明 | Reaches |
| --- | --- | --- | --- |
| [`gfm-render`](https://github.com/briangtn/claude-gfm-render/tree/a209ad5a0ec35c0813d2d80ab62b596140b0c807)<br><sub>by briangtn</sub> | GitHub Flavored Markdown in the transcript: alerts (> [!NOTE]), task lists, strikethrough and Mermaid diagrams | 在对话里渲染 GitHub 风格 Markdown：提示块、任务列表、删除线、Mermaid 图 | runs commands |
| [`md-preview`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/md-preview)<br><sub>by hamzafer</sub> | Shows the Markdown files Claude edits, rendered like GitHub, in a pane next to the chat. Before and after side by side. /md opens it. | Claude 编辑的 Markdown 文件在侧边面板按 GitHub 样式渲染，前后对照（/md） | files, runs commands |
| [`replay-theater`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/replay-theater)<br><sub>by hamzafer</sub> | Step through the last turn's file edits, one diff at a time. | 逐个 diff 回放上一轮的文件修改 | files |
| [`skins`](https://github.com/hellosverre/claude-skins/tree/342fbc0dd49ec44c824ed9c8eb95cd4927d7f81a)<br><sub>by hellosverre</sub> | Skins for Claude Code's transcript: themed tool rows, reply gutters and spinner words. /skin swaps them live. | 给对话记录换皮肤：工具行、回复边栏和 spinner 文案，/skin 实时切换 | — |
| [`mdview`](https://github.com/xuanji86/claude-mdview/tree/da646556714507acf5d41610605b9911eb9aa42a)<br><sub>by xuanji86</sub> | Click a .md path in the Claude Code conversation to read it rendered as markdown beside the session, pictures included, and point at any block to have Claude edit it. | 点击对话里的 .md 路径，在旁边渲染阅读（含图片），还能指着某段让 Claude 改 | files, runs commands |
| [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/2165ae76c9639e3996829ab0e6d54ddbd4f06ad8/claude-code-plugin)<br><sub>by zenbu-labs</sub> | A browser running directly inside claude code. Preview websites, view HTML documents, and let your agent control the built in browser. | 在对话旁开一个浏览器：预览网页和本地 HTML，也能让 agent 操作这个浏览器 | files, network, runs commands |

### Safety and guards · 安全与守卫

| Mod | What it does | 说明 | Reaches |
| --- | --- | --- | --- |
| [`blast-radius`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/blast-radius)<br><sub>by hamzafer</sub> | Holds risky Bash commands and shows what they would change before they run. | 拦住有风险的 Bash 命令，先展示会改动什么再让你确认 | runs commands |
| [`merge-gate`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/merge-gate)<br><sub>by hamzafer</sub> | Holds `gh pr merge` until CI passes and one Codex review (OpenAI's luna model) has run. A PR line above the prompt, and /gate shows the PR's status. | `gh pr merge` 要等 CI 通过且跑过一次 Codex 审查才放行 | files, runs commands |
| [`rulebook-guard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/rulebook-guard)<br><sub>by hamzafer</sub> | Writing and git rules: replaces em dashes in prose, and asks before git commit --amend, an unformatted push, or personal info in notes and commits. | 写作和 git 规则：替换正文里的破折号；amend、未格式化的 push、提交里带个人信息时先问你 | files, runs commands |
| [`secret-redactor`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/secret-redactor)<br><sub>by ray-amjad</sub> | Keeps secrets, email addresses and IP addresses out of the session transcript: swaps each one for a stable placeholder on the way in, and puts the real value back on the way into a tool call | 密钥、邮箱、IP 进对话前换成固定占位符，调用工具时再换回真实值 | — |

### Git, PRs and deploys · Git、PR 与部署

| Mod | What it does | 说明 | Reaches |
| --- | --- | --- | --- |
| [`vercel-deploy-status`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/vercel-deploy-status)<br><sub>by ray-amjad</sub> | Pins the Vercel deploy queue of the linked project under the prompt: every deploy queued, building or just finished, with its phase and elapsed time | 在输入框下方固定显示当前项目的 Vercel 部署队列和进度 | files, runs commands |
| [`cc-pr-tracker`](https://github.com/sezaakgun/cc-pr-tracker/tree/2d96fc7ed6bcca44a350700ac4c37e9066d58b46)<br><sub>by sezaakgun</sub> | Watch GitHub PRs from a Claude Code session: merge state, review and required checks above the prompt, with alerts when they change | 盯着的 GitHub PR 的合并状态、审查和必需检查，变化时提醒 | files, runs commands |

### While you wait · 等待时的消遣

| Mod | What it does | 说明 | Reaches |
| --- | --- | --- | --- |
| [`tw-stock-mod`](https://github.com/darrell-tw/darrelltw-mods/tree/649efd272da992051c48d25f30a393e0e0ce45b8/mods/tw-stock-mod)<br><sub>by darrell-tw</sub> | Watchlist band above the Claude Code prompt: Taiwan hours show the Taiwan list (紅漲綠跌), US hours show the US list (綠漲紅跌), in a broker-style table with a Solari split-flap footer, plus a 損益 mode (P&L view) for your holdings. 20 symbols a market, 10 on screen at a time. Live prices from Yahoo by default, no key and no account; 永豐 Shioaji (macOS/Linux) and 群益 Capital (Windows) are opt-in real-time routes the band runs itself, tried in your own preference order (twSources) - keep that order and any broker paths in a user-level ~/.claude/stock-band.json so a shared project config stays neutral. Needs function hooks (early access) and an interactive terminal. Zero model tokens. | 台股/美股自选股看板，按交易时段切换，含持仓损益模式 | files, network, runs commands |
| [`mindful-claude`](https://github.com/halluton/Mindful-Claude/tree/411c9c4f4f1c3d128159be7315823341ae7d9e2d)<br><sub>by halluton</sub> | Guided breathing exercises above the prompt while Claude works: coherent, box, 4-7-8 and the physiological sigh, four animation styles, and the spinner reads the breath. Appears when Claude starts, disappears when Claude answers. Needs function hooks (early access) and an interactive terminal. | Claude 干活时在输入框上方带你做呼吸练习，spinner 跟着呼吸计数 | — |
| [`now-playing`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/now-playing)<br><sub>by hamzafer</sub> | What Spotify is playing, one line above the prompt: track, progress and the lyric being sung, with ⏮ ⏸ ⏭ buttons. /music controls it too. macOS. | 一行显示 Spotify 正在播放的歌、进度和当前歌词，带控制按钮（仅 macOS） | network, runs commands |
| [`prayer-times`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/prayer-times)<br><sub>by hamzafer</sub> | The current prayer and how long is left, the next prayer, and zawal, above the prompt. Computed on your computer from your location; nothing is sent anywhere. | 当前和下一次礼拜时间及剩余时长，在本机按位置计算，不联网 | — |
| [`reels`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/reels)<br><sub>by hamzafer</sub> | YouTube Shorts in a terminal pane: plays while Claude works, pauses when Claude is done. | 在终端面板播 YouTube Shorts，Claude 工作时播放、完成时暂停 | files, network, runs commands |
| [`snake`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/snake)<br><sub>by hamzafer</sub> | Snake in a pane while Claude works, paused when it's done. Opt-in, so nothing opens until /snake. | Claude 工作时在面板里玩贪吃蛇，需要先 /snake 打开 | — |
| [`cc-arcade`](https://github.com/sezaakgun/cc-arcade/tree/0baff06d31295850283c2eebe052f39bbc35473f)<br><sub>by sezaakgun</sub> | Games above the Claude Code prompt (snake, Tetris, 2048, Minesweeper, Flappy, Pong, typing test, Space Invaders, Doom) plus a pet that grows as Claude tests, commits and edits. Clones of the genre, not affiliated with or endorsed by Tetris Holding, Taito, Atari or id Software. Needs function hooks (early access) and an interactive terminal. | 输入框上方 9 个小游戏（贪吃蛇、俄罗斯方块、2048 等），外加随测试和提交成长的宠物 | — |
<!-- catalog:end -->

## Add a mod

**A community mod**: add an entry to `community.json` with the repository, the
plugin's folder inside it (`""` for the root), the commit `sha` you checked, a
category, the license and a one-line Chinese summary. Then:

```bash
python3 scripts/build-catalog.py   # regenerates marketplace.json and the table above
claude plugin validate .
```

To move a mod to a newer version, review the new commits and change its `sha`.

**A mod of your own**, kept in this repo:

```bash
scripts/new-mod.sh my-mod "One line about what it does"
claude --plugin-dir "$PWD/my-mod"     # reloads on every save
```

then add it to `OURS` in `scripts/build-catalog.py`. A mod is a folder:

```
my-mod/
├── .claude-plugin/plugin.json   name, version, description (+ "types" if it keeps state)
├── hooks/hooks.json             { "modules": ["./register.ts"] }
├── hooks/register.ts(x)         export const register: Register = on => { ... }
├── types/index.d.ts             optional: the $.state contract
└── tests/my-mod.test.ts         run with: claude plugin test my-mod
```

Every hook is `($, e, next)`: call `next(e)` to pass the event on, `next({ ...e, x })`
to rewrite it, or return without calling `next` to answer it yourself. Keep values in
`$.state`; module variables reset on every reload. Run `scripts/check.sh` before you
push.

## Credits

Community mods belong to their authors and keep their own licenses (MIT, or
Apache-2.0 for `agent-flow`); this repository only lists them. Many were found through
[awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods).
To have a mod removed or its listing changed, open an issue.

---

## 中文说明

**精选 Claude Code mods：逐个挑选、校验、固定版本，添加一次就能装 45 个。**

这是一个 Claude Code 插件市场，收录的是 **mods**：用函数钩子写成的插件，可以观察、改写或接管
Claude Code 的行为，也能画自己的界面。添加一次市场，就能按名字安装下面任何一个 mod。其中少数是本仓库
自己写的，其余是挑选的社区 mod，都用 `claude plugin validate` 校验过，并固定在检查过的 commit 上。

需要 Claude Code 2.1.287 或更高版本。在 Claude Code 终端里输入：

```
/plugin marketplace add claude-code-mods/best-claude-code-mods
/plugin install <mod 名>@best-claude-code-mods
```

更新：`/plugin marketplace update best-claude-code-mods`。

表格里的 **Reaches** 一列是校验器报告的、除了画界面以外的能力：联网（network）、运行命令
（runs commands）、调用模型（model calls）、读写文件（files）、使用 MCP。安装前请看一下它的源码；
校验只是静态读代码，不等于安全审计。

社区 mod 的版权归原作者，沿用各自的许可证，本仓库只做收录。想下架或修改收录信息，请开 issue。

Unofficial; not an Anthropic product.
