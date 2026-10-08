# Best Claude Code Mods · 精选 Claude Code 模组

[English](README.md) · **简体中文** · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

**逐个挑选、校验、固定版本。添加一次，43 个 mod 随装随用。**

Mod 是用函数钩子写成的 Claude Code 插件：可以观察、修改或接管 Claude Code 的行为，也能绘制自己的界面。这个市场收录了社区里最好的 mod。每一个都用 `claude plugin validate` 校验过，并固定在校验时的 commit 上，作者之后的改动不会未经审核就到你这里。

需要 Claude Code 2.1.287 或更高版本。

## 安装

在 Claude Code 终端会话中输入：

```
/plugin marketplace add claude-code-mods/best-claude-code-mods
/plugin install <mod 名>@best-claude-code-mods
```

例如 `/plugin install terminal-browser@best-claude-code-mods`。运行 `/plugin marketplace update best-claude-code-mods` 获取新 mod 和更新。

## 目录

**权限**一列是校验器报告的、该 mod 除绘制界面以外还能做的事。安装前请先看看它的源码：校验只是静态读取代码，并不运行它，也不等于安全审计。

### 仪表盘与用量

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 功能 | 权限 |
| --- | --- | --- |
| [`cache-clock`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/cache-clock)<br><sub>作者 hamzafer</sub> | 状态栏下一行：提示缓存还热几分钟，冷了以后下一条要重新缓存多少 token | 读写文件, 运行命令 |
| [`context-bar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/context-bar)<br><sub>作者 hamzafer</sub> | 上下文窗口按类别分色的堆叠条，含 token 数和压缩点（/context-bar 开关） | — |
| [`openai-balance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/openai-balance)<br><sub>作者 hamzafer</sub> | OpenAI API 余额估算、今日花费和主要去向（/openai-balance） | 联网, 运行命令 |
| [`token-weather`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/token-weather)<br><sub>作者 hamzafer</sub> | 把上下文占用画成天气预报，附提示缓存倒计时 | 读写文件, 运行命令 |
| [`usage-meter`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/usage-meter)<br><sub>作者 hamzafer</sub> | 5 小时和 7 天用量小进度条，带重置倒计时和本会话费用 | — |
| [`usage-band`](https://github.com/JetsonChan/CC-Usage-Band/tree/60cd60949b1f52c96ddba3ea24ed0848ff302196/usage-band)<br><sub>作者 JetsonChan</sub> | 输入框上方显示 5 小时/7 天限额、上下文和缓存命中率，终端和桌面版都适配 | — |
| [`context-view`](https://github.com/kongyo2/context-view/tree/137e4e3db754684144ec953c5e66085bc2959766)<br><sub>作者 kongyo2</sub> | 一行显示上下文占用，样式同 Claude Code 自带的仪表，含距自动压缩还剩多少 | — |
| [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/f31daca523d36c501cd0df23a737a44c7dc56ad6)<br><sub>作者 scasella</sub> | agent 仪表盘：模型状态、每次权限判定、子 agent 卡片和泳道、本轮小票、会话日志 | — |
| [`cctop`](https://github.com/tomstagl/cctop/tree/6ceafc34a972f4e58d5e53b1c69f80e2a9759d41/plugin)<br><sub>作者 tomstagl</sub> | btop 风格的实时面板：上下文、token、费用、缓存命中、限额、各工具耗时（/cctop） | 读写文件, 运行命令 |
| [`statuspane`](https://github.com/xuanji86/claude-statuspane/tree/13bd8e46edefdf282f117941b886cb529c7d79c3)<br><sub>作者 xuanji86</sub> | 输入框上方的浮动状态卡：模型、effort、上下文、5 小时/周限额、费用、分支、CI | 读写文件, 运行命令 |
| [`plan-progress`](https://github.com/zycck/claude-mods/tree/3539d02d7435397d293e3120ebad22c23214f6c0/plugins/plan-progress)<br><sub>作者 zycck</sub> | 输入框上方的计划进度条：阶段、步骤、像素填充，决策/出错/完成时有提示音 | 读写文件, 运行命令 |

### Agent 与子 agent

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 功能 | 权限 |
| --- | --- | --- |
| [`agent-flow`](https://github.com/Charlie0113-T/claude-agent-flow/tree/d87b2559dec03979e088026e8f48aee5f9d2cab5)<br><sub>作者 Charlie0113-T</sub> | /flow 在对话旁打开子 agent 和队友的实时树状图 | — |
| [`agent-radar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/agent-radar)<br><sub>作者 hamzafer</sub> | 每个运行中的子 agent 一行：用时、工具次数、正在做什么（/radar 看全部） | — |
| [`browser-lanes`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/browser-lanes)<br><sub>作者 hamzafer</sub> | 显示 Playwright 浏览器被谁占用；子 agent 要用时排队，/browser clean 清理残留 | 运行命令 |
| [`mission-control`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/mission-control)<br><sub>作者 hamzafer</sub> | /mission 打开主 agent、子 agent 和所有工具调用的实时地图，外加文件代码地图 | 读写文件, 调用模型, 运行命令 |
| [`review-watch`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/review-watch)<br><sub>作者 hamzafer</sub> | 每个进行中的代码审查（Codex 或审查子 agent）一行实时状态，结束时弹出结论 | 运行命令 |
| [`switchboard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/switchboard)<br><sub>作者 hamzafer</sub> | 为没指定模型的子 agent 自动选模型（调用 OpenAI Decisions API 或 Jev），/route 看选择和花费 | 联网 |
| [`agentpane`](https://github.com/xuanji86/claude-agentpane/tree/17be88979e5782591a2a184959df1c4168600066)<br><sub>作者 xuanji86</sub> | 侧边面板列出子 agent：各自在做什么、花了多少 token，点开看它的对话 | — |

### 效率与上下文

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 功能 | 权限 |
| --- | --- | --- |
| [`glance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/glance)<br><sub>作者 hamzafer</sub> | 一行显示需要你处理的事：下一个会议、PR、Linear 任务、Slack 私信（通过已连接的 MCP） | MCP, 运行命令 |
| [`next-steps`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/next-steps)<br><sub>作者 hamzafer</sub> | 每轮结束后给出 2–3 个可能的下一条提示，在空输入框里按 1/2/3 选用 | 调用模型 |
| [`session-saver`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/session-saver)<br><sub>作者 hamzafer</sub> | 给未命名会话起名；/park 记下进度，恢复会话时显示 | 调用模型, 运行命令 |
| [`where-am-i`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/where-am-i)<br><sub>作者 hamzafer</sub> | 输入框上方实时小结：目标、正在做、等你处理、下一步（/where 看详细） | 调用模型 |
| [`aside`](https://github.com/JayDoubleu/aside/tree/cf2b7562ae7b376cdcf9e2436a926aba77dc759f)<br><sub>作者 JayDoubleu</sub> | 只读旁聊：/aside 在侧边问关于当前会话的问题，不写回主对话 | 调用模型 |
| [`lcm`](https://github.com/lossless-claude/lcm/tree/0c17dbffda452cf7fae46929af427dff355aeaa3)<br><sub>作者 lossless-claude</sub> | 无损上下文管理：用 DAG 做分层摘要，每条消息都还能找回 | 读写文件, 联网, 调用模型, 运行命令 |

### 渲染与预览

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 功能 | 权限 |
| --- | --- | --- |
| [`gfm-render`](https://github.com/briangtn/claude-gfm-render/tree/a209ad5a0ec35c0813d2d80ab62b596140b0c807)<br><sub>作者 briangtn</sub> | 在对话里渲染 GitHub 风格 Markdown：提示块、任务列表、删除线、Mermaid 图 | 运行命令 |
| [`md-preview`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/md-preview)<br><sub>作者 hamzafer</sub> | Claude 编辑的 Markdown 文件在侧边面板按 GitHub 样式渲染，修改前后对照（/md） | 读写文件, 运行命令 |
| [`replay-theater`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/replay-theater)<br><sub>作者 hamzafer</sub> | 逐个 diff 回放上一轮的文件修改 | 读写文件 |
| [`skins`](https://github.com/hellosverre/claude-skins/tree/342fbc0dd49ec44c824ed9c8eb95cd4927d7f81a)<br><sub>作者 hellosverre</sub> | 给对话记录换皮肤：工具行、回复边栏和 spinner 文案，/skin 实时切换 | — |
| [`mdview`](https://github.com/xuanji86/claude-mdview/tree/da646556714507acf5d41610605b9911eb9aa42a)<br><sub>作者 xuanji86</sub> | 点击对话里的 .md 路径，在旁边渲染阅读（含图片），还能指着某段让 Claude 改 | 读写文件, 运行命令 |
| [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/2165ae76c9639e3996829ab0e6d54ddbd4f06ad8/claude-code-plugin)<br><sub>作者 zenbu-labs</sub> | 在对话旁开一个浏览器：预览网页和本地 HTML，也能让 agent 操作它 | 读写文件, 联网, 运行命令 |

### 安全与守卫

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 功能 | 权限 |
| --- | --- | --- |
| [`blast-radius`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/blast-radius)<br><sub>作者 hamzafer</sub> | 拦住有风险的 Bash 命令，先展示会改动什么再让你确认 | 运行命令 |
| [`merge-gate`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/merge-gate)<br><sub>作者 hamzafer</sub> | `gh pr merge` 要等 CI 通过且跑过一次 Codex 审查才放行 | 读写文件, 运行命令 |
| [`rulebook-guard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/rulebook-guard)<br><sub>作者 hamzafer</sub> | 写作和 git 规则：替换正文里的破折号；amend、未格式化的 push、提交里带个人信息时先问你 | 读写文件, 运行命令 |
| [`secret-redactor`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/secret-redactor)<br><sub>作者 ray-amjad</sub> | 密钥、邮箱、IP 进对话前换成固定占位符，调用工具时再换回真实值 | — |

### Git、PR 与部署

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 功能 | 权限 |
| --- | --- | --- |
| [`vercel-deploy-status`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/vercel-deploy-status)<br><sub>作者 ray-amjad</sub> | 在输入框下方固定显示当前项目的 Vercel 部署队列和进度 | 读写文件, 运行命令 |
| [`cc-pr-tracker`](https://github.com/sezaakgun/cc-pr-tracker/tree/2d96fc7ed6bcca44a350700ac4c37e9066d58b46)<br><sub>作者 sezaakgun</sub> | 盯着的 GitHub PR 的合并状态、审查和必需检查，变化时提醒 | 读写文件, 运行命令 |

### 等待时的消遣

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 功能 | 权限 |
| --- | --- | --- |
| [`tw-stock-mod`](https://github.com/darrell-tw/darrelltw-mods/tree/649efd272da992051c48d25f30a393e0e0ce45b8/mods/tw-stock-mod)<br><sub>作者 darrell-tw</sub> | 台股/美股自选股看板，按交易时段切换，含持仓损益模式 | 读写文件, 联网, 运行命令 |
| [`mindful-claude`](https://github.com/halluton/Mindful-Claude/tree/411c9c4f4f1c3d128159be7315823341ae7d9e2d)<br><sub>作者 halluton</sub> | Claude 干活时在输入框上方带你做呼吸练习，spinner 跟着呼吸计数 | — |
| [`now-playing`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/now-playing)<br><sub>作者 hamzafer</sub> | 一行显示 Spotify 正在播放的歌、进度和当前歌词，带控制按钮（仅 macOS） | 联网, 运行命令 |
| [`prayer-times`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/prayer-times)<br><sub>作者 hamzafer</sub> | 当前和下一次礼拜时间及剩余时长，在本机按位置计算，不联网 | — |
| [`reels`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/reels)<br><sub>作者 hamzafer</sub> | 在终端面板播放 YouTube Shorts，Claude 工作时播放、完成时暂停 | 读写文件, 联网, 运行命令 |
| [`snake`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/snake)<br><sub>作者 hamzafer</sub> | Claude 工作时在面板里玩贪吃蛇，需先 /snake 打开 | — |
| [`cc-arcade`](https://github.com/sezaakgun/cc-arcade/tree/0baff06d31295850283c2eebe052f39bbc35473f)<br><sub>作者 sezaakgun</sub> | 输入框上方 9 个小游戏（贪吃蛇、俄罗斯方块、2048 等），外加随测试和提交成长的宠物 | — |

## 推荐 mod

开一个 issue，附上 mod 仓库的链接。也可以自己添加：在 `community.json` 里加一条（仓库、目录、审核过的 commit、分类、许可证），在 `readme/summaries.json` 里写上各语言的一句话简介，运行 `python3 scripts/build-catalog.py`，然后提交 pull request。

## 致谢

每个 mod 归其作者所有，沿用各自的许可证；本仓库只做收录。作者如需修改或下架收录信息，请开 issue。

非官方项目，与 Anthropic 无关。
