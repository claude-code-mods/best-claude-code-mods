# Best Claude Code Mods · 精选 Claude Code 模组

[English](README.md) · **简体中文** · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

**逐个挑选、校验、固定版本。添加一次，41 个 mod 随装随用。**

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

每张卡片的**权限**是校验器报告的、该 mod 除绘制界面以外还能做的事。安装前请先看看它的源码：校验只是静态读取代码，并不运行它，也不等于安全审计。

### 仪表盘与用量

[![token-optimizer](https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/docs-site/public/media/token-optimizer-desktop-status-bar.gif)](https://github.com/alexgreensh/token-optimizer/tree/e3f1a2dcad8d8999096b8a881c4d98cdba4ef1a5/desktop/token-optimizer-desktop)

#### [`token-optimizer`](https://github.com/alexgreensh/token-optimizer/tree/e3f1a2dcad8d8999096b8a881c4d98cdba4ef1a5/desktop/token-optimizer-desktop)

*作者 alexgreensh* · token 优化状态栏，显示 token 去向并给出更省钱的调整。

**权限:** 运行命令, 调用模型, 读写文件

`/plugin install token-optimizer@best-claude-code-mods`

[![claude-council](https://github.com/hex/claude-council/raw/main/assets/desktop-code-tab.png)](https://github.com/hex/claude-council/tree/f2f7f42122b288599cef8cea97dcc490acea98a5)

#### [`claude-council`](https://github.com/hex/claude-council/tree/f2f7f42122b288599cef8cea97dcc490acea98a5)

*作者 hex* · 同时咨询多个 AI agent 获取多种视角，带流式面板和可选的额外复查提示。

**权限:** 运行命令, 调用模型, 读写文件

`/plugin install claude-council@best-claude-code-mods`

[![codex-attachment-manager](https://github.com/chipfighter/context-attachment-manager/raw/main/docs/images/hero.gif)](https://github.com/chipfighter/context-attachment-manager/tree/d68a721b7432059c9056d546ff2a26b11b3c0e0c)

#### [`codex-attachment-manager`](https://github.com/chipfighter/context-attachment-manager/tree/d68a721b7432059c9056d546ff2a26b11b3c0e0c)

*作者 chipfighter* · 较早的图片以占位符发送、按 ID 取回原图，让长图片会话保住 prompt 缓存。

**权限:** 联网, MCP

`/plugin install codex-attachment-manager@best-claude-code-mods`

[![cache-tax](https://github.com/karanb192/cache-tax/raw/main/site/assets/refusal.gif)](https://github.com/karanb192/cache-tax/tree/535ff33225e666e605e731d78f5ac5efe243c7c3)

#### [`cache-tax`](https://github.com/karanb192/cache-tax/tree/535ff33225e666e605e731d78f5ac5efe243c7c3)

*作者 karanb192* · 在休息时保持一小时 prompt 缓存温热，冷启动前先询问并显示重写成本。

**权限:** 调用模型

`/plugin install cache-tax@best-claude-code-mods`

[![agent-standup-band](https://atoll92.github.io/agent-standup/media/banner.png)](https://github.com/Atoll92/agent-standup/tree/846d5324f7c00f06d598c86e87ed8b51d774b3ac/plugin-band)

#### [`agent-standup-band`](https://github.com/Atoll92/agent-standup/tree/846d5324f7c00f06d598c86e87ed8b51d774b3ac/plugin-band)

*作者 Atoll92* · 本机其他会话需要你时在提示上方显示一行，结束时给一个提醒。

**权限:** 运行命令, 读写文件

`/plugin install agent-standup-band@best-claude-code-mods`

[![shunt](docs/assets/shunt.png)](https://github.com/pleaseai/shunt/tree/57182b328e92d3c70bc9ca5a1fd1ee9104cfbabb/plugins/shunt)

#### [`shunt`](https://github.com/pleaseai/shunt/tree/57182b328e92d3c70bc9ca5a1fd1ee9104cfbabb/plugins/shunt)

*作者 pleaseai* · shunt 网关的用量条：各窗口花费与重置时间，以及完整的 /shunt:usage 明细。

**权限:** 联网, 运行命令

`/plugin install shunt@best-claude-code-mods`

[![tokendoctor](https://github.com/localixai/tokendoctor/raw/main/docs/demo.gif)](https://github.com/localixai/tokendoctor/tree/051fa9598f0a50ed30974b618f2911381b7dcf90)

#### [`tokendoctor`](https://github.com/localixai/tokendoctor/tree/051fa9598f0a50ed30974b618f2911381b7dcf90)

*作者 localixai* · 回放你过去的会话，展示每项改动能省多少，然后只应用你选择的改动。

**权限:** 运行命令, 调用模型

`/plugin install tokendoctor@best-claude-code-mods`

[![skins](https://github.com/hellosverre/claude-skins/raw/main/docs/demo.gif)](https://github.com/hellosverre/claude-skins/tree/cf0d39f3785d5c5a4b6189ecc487b1ac479efea0)

#### [`skins`](https://github.com/hellosverre/claude-skins/tree/cf0d39f3785d5c5a4b6189ecc487b1ac479efea0)

*作者 hellosverre* · 转录皮肤的十五种主题、丰富卡片与用量条；/skin 实时切换。

**权限:** 联网, 运行命令, 调用模型, 读写文件

`/plugin install skins@best-claude-code-mods`

[![ctx-handoff](docs/assets/ctx-handoff-mod.png)](https://github.com/cablate/ctx-handoff-mod/tree/a416713a0495be799a31f3650e18458e242270c7)

#### [`ctx-handoff`](https://github.com/cablate/ctx-handoff-mod/tree/a416713a0495be799a31f3650e18458e242270c7)

*作者 cablate* · 把你教给 Claude 的内容沉淀为项目笔记，捕捉常见疏漏，保温缓存并续接长会话。

**权限:** 调用模型, 读写文件

`/plugin install ctx-handoff@best-claude-code-mods`

[![great-cto](docs/assets/great_cto.png)](https://github.com/avelikiy/great_cto/tree/12dfd86e99627cd6dd1ed394de4786f4ba08499b)

#### [`great-cto`](https://github.com/avelikiy/great_cto/tree/12dfd86e99627cd6dd1ed394de4786f4ba08499b)

*作者 avelikiy* · 把 Claude Code 当作 73 个专家 agent 的流水线运行，每个阶段由独立模型复核。

**权限:** 联网

`/plugin install great-cto@best-claude-code-mods`

[![ripple](https://github.com/PBJ-2/clauderipple/raw/main/docs/media/demo.webp)](https://github.com/PBJ-2/clauderipple/tree/c1c6b76a9e4e7a51df2ec5907d6e41d6bf8591e3/packages/mod)

#### [`ripple`](https://github.com/PBJ-2/clauderipple/tree/c1c6b76a9e4e7a51df2ec5907d6e41d6bf8591e3/packages/mod)

*作者 PBJ-2* · 为每条提示选择推理强度、为每个委派任务选择执行者，保温缓存并显示请求去向。

**权限:** 联网, 运行命令, 调用模型, MCP, 读写文件

`/plugin install ripple@best-claude-code-mods`

[![tavernweave-agent-skills](https://github.com/LiarMTTT/TavernWeave/raw/main/docs/assets/tavernweave-v1-cover.png)](https://github.com/LiarMTTT/TavernWeave/tree/f9863d2b05305457fe9ed8b0c5688d52aca400a5)

#### [`tavernweave-agent-skills`](https://github.com/LiarMTTT/TavernWeave/tree/f9863d2b05305457fe9ed8b0c5688d52aca400a5)

*作者 LiarMTTT* · 23 个共享技能用于角色卡、软件工作和有界云任务，提示上方有 Soul 模式开关。

**权限:** —

`/plugin install tavernweave-agent-skills@best-claude-code-mods`

[![agent-usage-guard](https://github.com/rbartoli/agent-usage-guard/releases/download/agent-usage-guard--v1.0.0/agent-usage-guard.gif)](https://github.com/rbartoli/agent-usage-guard/tree/02594c2620be9eb60c32e2f77d9d512d9f61b205)

#### [`agent-usage-guard`](https://github.com/rbartoli/agent-usage-guard/tree/02594c2620be9eb60c32e2f77d9d512d9f61b205)

*作者 rbartoli* · 在子 agent 扩散、重上下文提示和重试循环消耗你的用量窗口之前将其拦下。

**权限:** 调用模型, 读写文件

`/plugin install agent-usage-guard@best-claude-code-mods`


### Agent 与子 agent

[![shared-session](https://github.com/Paradigm-Study/claude-share/raw/main/docs/assets/invitation-demo.png)](https://github.com/Paradigm-Study/claude-share/tree/9d88f996ac4245c756a89b34e98cfde375028950/plugin)

#### [`shared-session`](https://github.com/Paradigm-Study/claude-share/tree/9d88f996ac4245c756a89b34e98cfde375028950/plugin)

*作者 Paradigm-Study* · 用链接或团队共享会话；队友用自己的 Claude Code 加入并实时看到每一轮。

**权限:** —

`/plugin install shared-session@best-claude-code-mods`

[![flightdeck](https://github.com/scasella/claude-flightdeck/raw/main/docs/media/demo.gif)](https://github.com/scasella/claude-flightdeck/tree/626cc0b46d417f81bbff9f5ba3b49abaf8912a85)

#### [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/626cc0b46d417f81bbff9f5ba3b49abaf8912a85)

*作者 scasella* · 实时 agent 仪表盘：模型体征、值班架构师、权限检查、子 agent 卡片与会话日志。

**权限:** —

`/plugin install flightdeck@best-claude-code-mods`

[![start](https://github.com/rsmdt/the-startup/raw/main/logo.png)](https://github.com/rsmdt/the-startup/tree/e803d51fdb423271d3dde189f5416f3ec51386a9/plugins/start)

#### [`start`](https://github.com/rsmdt/the-startup/tree/e803d51fdb423271d3dde189f5416f3ec51386a9/plugins/start)

*作者 rsmdt* · 面向 agent 软件开发的流程编排命令。

**权限:** 读写文件

`/plugin install start@best-claude-code-mods`

[![lane-stack](docs/assets/claude-lane-stack.png)](https://github.com/VKirill/claude-lane-stack/tree/8bac2b876b72053aa445bb9d1c7c6079bfc4ba8c/plugins/lane-stack)

#### [`lane-stack`](https://github.com/VKirill/claude-lane-stack/tree/8bac2b876b72053aa445bb9d1c7c6079bfc4ba8c/plugins/lane-stack)

*作者 VKirill* · 单人 PM 流水线：编排 agent、泳道手册、入职与续接命令。

**权限:** 联网, 调用模型

`/plugin install lane-stack@best-claude-code-mods`


### 效率与上下文

[![pebrel-prompt-suggestions](https://github.com/Kuddev/pebrel/raw/main/docs/screenshots/nebula-claude-session.png)](https://github.com/Kuddev/pebrel/tree/ed9b2331340877ba3d775e38c4df6bd1a2abb1fe/pebrel_app/res/prompt-suggestions/claude)

#### [`pebrel-prompt-suggestions`](https://github.com/Kuddev/pebrel/tree/ed9b2331340877ba3d775e38c4df6bd1a2abb1fe/pebrel_app/res/prompt-suggestions/claude)

*作者 Kuddev* · 通过 Pebrel 会话桥在空输入框里给出原生提示预测。

**权限:** 联网

`/plugin install pebrel-prompt-suggestions@best-claude-code-mods`

[![fast-jev-compaction](docs/assets/fast-jev-compaction.png)](https://github.com/tamaratran/fast-jev-compaction/tree/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0)

#### [`fast-jev-compaction`](https://github.com/tamaratran/fast-jev-compaction/tree/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0)

*作者 tamaratran* · 为 Claude Code 会话提供逐字保留的 Jev 压缩。

**权限:** 联网, 调用模型

`/plugin install fast-jev-compaction@best-claude-code-mods`

[![lot-map](https://github.com/alexeyw/lot-map/raw/main/docs/demo.gif)](https://github.com/alexeyw/lot-map/tree/ad60f057902765d778eedde770d337be45fac3af)

#### [`lot-map`](https://github.com/alexeyw/lot-map/tree/ad60f057902765d778eedde770d337be45fac3af)

*作者 alexeyw* · 聊天旁的实时地图：记忆、文件、Shell、网络、模型、agent、技能与 hooks 被使用时点亮。

**权限:** —

`/plugin install lot-map@best-claude-code-mods`

[![storybloq](https://raw.githubusercontent.com/Storybloq/storybloq/main/assets/board.png)](https://github.com/Storybloq/storybloq/tree/f0b4c08e3a15ffb9841e5a3058c6b1ca57607154/plugins/storybloq)

#### [`storybloq`](https://github.com/Storybloq/storybloq/tree/f0b4c08e3a15ffb9841e5a3058c6b1ca57607154/plugins/storybloq)

*作者 Storybloq* · 项目记忆：把工单、问题、交接和经验存进仓库里的 .story/ 目录。

**权限:** 读写文件

`/plugin install storybloq@best-claude-code-mods`

[![just-do-it](docs/assets/claude-ops.png)](https://github.com/Lifecycle-Innovations-Limited/claude-ops/tree/e434ef7e612f2ff5769def6101fc9d984888d377/claude-ops/skills/ops-jdi/plugin)

#### [`just-do-it`](https://github.com/Lifecycle-Innovations-Limited/claude-ops/tree/e434ef7e612f2ff5769def6101fc9d984888d377/claude-ops/skills/ops-jdi/plugin)

*作者 Lifecycle-Innovations-Limited* · 把已授权的工作推进到验证与交付，并暴露需要修复的配置问题。

**权限:** 运行命令, 调用模型

`/plugin install just-do-it@best-claude-code-mods`

[![filetree](https://github.com/data-goblin/claude-code-filetree/raw/main/media/filetree-shimmer.gif)](https://github.com/data-goblin/claude-code-filetree/tree/1fdc3a963f2dc22a939f661ff0ff5a76646c9112)

#### [`filetree`](https://github.com/data-goblin/claude-code-filetree/tree/1fdc3a963f2dc22a939f661ff0ff5a76646c9112)

*作者 data-goblin* · IDE 风格的目录树，显示 Claude 正在做什么、改到哪个文件。

**权限:** 运行命令, 调用模型, 读写文件

`/plugin install filetree@best-claude-code-mods`

[![jev-auto-compact](https://github.com/notque/vexjoy-agent/raw/main/docs/repo-hero.png)](https://github.com/notque/vexjoy-agent/tree/c68ac1fea2a03e437ccc95112d1e56e467a9bd00/plugins/jev-auto-compact)

#### [`jev-auto-compact`](https://github.com/notque/vexjoy-agent/tree/c68ac1fea2a03e437ccc95112d1e56e467a9bd00/plugins/jev-auto-compact)

*作者 notque* · 上下文到 60% 时以零生成裁剪陈旧工具调用；无可裁剪时跳过而非退化为 LLM 摘要。

**权限:** 联网, 调用模型

`/plugin install jev-auto-compact@best-claude-code-mods`

[![caliber-jev-compaction](https://github.com/caliber-ai-org/ai-setup/raw/master/assets/readme/pillars.png)](https://github.com/caliber-ai-org/ai-setup/tree/f5dbc002022a8a10acad25c1cce23ddefdc19d0d/plugin/caliber-jev-compaction)

#### [`caliber-jev-compaction`](https://github.com/caliber-ai-org/ai-setup/tree/f5dbc002022a8a10acad25c1cce23ddefdc19d0d/plugin/caliber-jev-compaction)

*作者 caliber-ai-org* · 为 Claude Code 会话提供逐字保留的 Jev 压缩。

**权限:** 联网, 调用模型

`/plugin install caliber-jev-compaction@best-claude-code-mods`

[![operator](https://github.com/aerovato/operator-memory/raw/main/docs/assets/change-the-loop.png)](https://github.com/aerovato/operator-memory/tree/93c3fce64f0a72adeb89fa868600eb418548ec07/packages/claude-code)

#### [`operator`](https://github.com/aerovato/operator-memory/tree/93c3fce64f0a72adeb89fa868600eb418548ec07/packages/claude-code)

*作者 aerovato* · 面向 agent 开发的持久项目与用户记忆。

**权限:** —

`/plugin install operator@best-claude-code-mods`

[![claude-carbon](https://github.com/gwittebolle/claude-carbon/raw/main/docs/desktop-pane.png)](https://github.com/gwittebolle/claude-carbon/tree/9ad53f1dd07fb0e11fcdb94d294ed794d660cf4b)

#### [`claude-carbon`](https://github.com/gwittebolle/claude-carbon/tree/9ad53f1dd07fb0e11fcdb94d294ed794d660cf4b)

*作者 gwittebolle* · 在终端和桌面应用中追踪 Claude Code 会话的碳足迹。

**权限:** 读写文件

`/plugin install claude-carbon@best-claude-code-mods`

[![work-mode](https://github.com/danyuchn/claude-work-mode/raw/main/promo/demo-poster-en.png)](https://github.com/danyuchn/claude-work-mode/tree/e19eda1e8465308bd79a74fad295cf9b6d9cdf71/plugins/work-mode)

#### [`work-mode`](https://github.com/danyuchn/claude-work-mode/tree/e19eda1e8465308bd79a74fad295cf9b6d9cdf71/plugins/work-mode)

*作者 danyuchn* · 会话模式：auto（不中途提问）、out（委派批量工作）、wrap（收敛并收尾）。

**权限:** 运行命令, 读写文件

`/plugin install work-mode@best-claude-code-mods`

[![show-your-work](https://github.com/iamumeransari/claude-show-your-work/raw/main/docs/homepage.jpg)](https://github.com/iamumeransari/claude-show-your-work/tree/71e546044e3ba61b98a6938a03270da791f9ca2e)

#### [`show-your-work`](https://github.com/iamumeransari/claude-show-your-work/tree/71e546044e3ba61b98a6938a03270da791f9ca2e)

*作者 iamumeransari* · 在终端里展示成品：截图、操作录屏和前后对比的 QA。

**权限:** 联网, 运行命令, 调用模型, 读写文件

`/plugin install show-your-work@best-claude-code-mods`

[![inbox](docs/assets/inbox.png)](https://github.com/petekp/inbox/tree/02e441cd447edf86fc30fbd03e9117a8ead9da7a)

#### [`inbox`](https://github.com/petekp/inbox/tree/02e441cd447edf86fc30fbd03e9117a8ead9da7a)

*作者 petekp* · 汇总会话中等待你处理的问题、任务、发现与 PR。

**权限:** —

`/plugin install inbox@best-claude-code-mods`

[![compact-adviser](https://github.com/kunchenguid/compact-adviser/raw/main/docs/hint-status-line.png)](https://github.com/kunchenguid/compact-adviser/tree/37fa1a665b8933de68c90014312060e862cf121a/packages/claude-mod)

#### [`compact-adviser`](https://github.com/kunchenguid/compact-adviser/tree/37fa1a665b8933de68c90014312060e862cf121a/packages/claude-mod)

*作者 kunchenguid* · 在完成的检查点建议或执行 /compact，由 TypeSafe Jev 判定。

**权限:** 联网, 调用模型, 读写文件

`/plugin install compact-adviser@best-claude-code-mods`


### 渲染与预览

[![terminal-browser](docs/assets/terminal-browser.webp)](https://github.com/zenbu-labs/terminal-browser/tree/fa9e5eb053d2a1da11f7ccba720a0d3d389c05a6/claude-code-plugin)

#### [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/fa9e5eb053d2a1da11f7ccba720a0d3d389c05a6/claude-code-plugin)

*作者 zenbu-labs* · 内置在 Claude Code 里的浏览器：预览网站和 HTML，并可让 agent 操作这个浏览器。

**权限:** 联网, 运行命令, 调用模型, 读写文件

`/plugin install terminal-browser@best-claude-code-mods`

[![prismantis](https://github.com/NahumLitvin/prismantis/raw/main/docs/tour.gif)](https://github.com/NahumLitvin/prismantis/tree/3718a40abc57b836108a65bd9f01d06d3237e52d/plugin)

#### [`prismantis`](https://github.com/NahumLitvin/prismantis/tree/3718a40abc57b836108a65bd9f01d06d3237e52d/plugin)

*作者 NahumLitvin* · 为回复提供可换主题的彩色渲染：表格、标题、代码、数字、路径与链接。

**权限:** 运行命令, 读写文件

`/plugin install prismantis@best-claude-code-mods`


### 安全与守卫

[![lcu-approve](https://github.com/amontlabs/lcu/raw/main/docs/assets/approval-demo.gif)](https://github.com/amontlabs/lcu/tree/1bd45b304295c7665b559fcc32f7b3a8f1b1d859/adapters/claude-mod/lcu-approve)

#### [`lcu-approve`](https://github.com/amontlabs/lcu/tree/1bd45b304295c7665b559fcc32f7b3a8f1b1d859/adapters/claude-mod/lcu-approve)

*作者 amontlabs* · 电脑使用的按应用授权：本次允许、始终允许或拒绝，并有已授权应用面板。

**权限:** 运行命令, MCP, 读写文件

`/plugin install lcu-approve@best-claude-code-mods`

[![agentctl](https://raw.githubusercontent.com/sd0xdev/sd0x-harness/main/banner.jpg)](https://github.com/sd0xdev/sd0x-harness/tree/b0206637edd2e44c993da12b6b30858f96bc3cdc/mods/agentctl)

#### [`agentctl`](https://github.com/sd0xdev/sd0x-harness/tree/b0206637edd2e44c993da12b6b30858f96bc3cdc/mods/agentctl)

*作者 sd0xdev* · 会话级 agent 控制面板：任务范围、证据与交接。

**权限:** 运行命令, 调用模型, 读写文件

`/plugin install agentctl@best-claude-code-mods`

[![multi-core](docs/assets/cc-multi-cli-plugin.png)](https://github.com/greenpolo/cc-multi-cli-plugin/tree/66d9b0a6b06b25fd648ecd53311a647bb57e2fb4/plugins/multi-core)

#### [`multi-core`](https://github.com/greenpolo/cc-multi-cli-plugin/tree/66d9b0a6b06b25fd648ecd53311a647bb57e2fb4/plugins/multi-core)

*作者 greenpolo* · 在单个会话里使用 ChatGPT、Cursor、OpenCode 与 Antigravity 模型，用 /model 切换。

**权限:** 联网, 调用模型

`/plugin install multi-core@best-claude-code-mods`

[![jevmem-pane](docs/assets/jevmem.png)](https://github.com/Avinash-jetwani/jevmem/tree/c29753ccb2c9706e417fda25efa422682358955b/pane)

#### [`jevmem-pane`](https://github.com/Avinash-jetwani/jevmem/tree/c29753ccb2c9706e417fda25efa422682358955b/pane)

*作者 Avinash-jetwani* · 侧栏显示 jevmem 召回了什么、守卫判定什么、上一轮保存了什么。

**权限:** 运行命令, 读写文件

`/plugin install jevmem-pane@best-claude-code-mods`


### Git、PR 与部署

[![fm](https://github.com/kunchenguid/firstmate/raw/main/assets/banner.png)](https://github.com/kunchenguid/firstmate/tree/427056c4181c41074ad24f051f79919330df0fa5/.claude/mods/firstmate-calm)

#### [`fm`](https://github.com/kunchenguid/firstmate/tree/427056c4181c41074ad24f051f79919330df0fa5/.claude/mods/firstmate-calm)

*作者 kunchenguid* · 帆船工作动画与会话专用转录显示，跨会话共享 calm 模式偏好。

**权限:** 读写文件

`/plugin install fm@best-claude-code-mods`

[![turbo](https://github.com/tobihagemann/turbo/raw/main/assets/logo/thunderbolt-icon-256.png)](https://github.com/tobihagemann/turbo/tree/3bc6b4436d96be22497109e16e68fe4dfa323531/claude)

#### [`turbo`](https://github.com/tobihagemann/turbo/tree/3bc6b4436d96be22497109e16e68fe4dfa323531/claude)

*作者 tobihagemann* · 人工把关的 agent 软件工厂：你决定做什么并验收，技能负责构建与发布。

**权限:** 调用模型, 读写文件

`/plugin install turbo@best-claude-code-mods`

[![mazyos](docs/assets/MazyOS.png)](https://github.com/Mazzeo-Marketing/MazyOS/tree/d2b65b392f1ee230afb088d155fc734def5f105d)

#### [`mazyos`](https://github.com/Mazzeo-Marketing/MazyOS/tree/d2b65b392f1ee230afb088d155fc734def5f105d)

*作者 Mazzeo-Marketing* · 葡语商业操作插件：每次会话带入公司记忆、输出带品牌形象，并提供 17 个营销/SEO 技能。

**权限:** 读写文件

`/plugin install mazyos@best-claude-code-mods`

[![engineer](docs/assets/engineer.png)](https://github.com/swingerman/engineer/tree/ae4cb5fe32007dd6a3d717c9998dcfb12b1f348e/engineer)

#### [`engineer`](https://github.com/swingerman/engineer/tree/ae4cb5fe32007dd6a3d717c9998dcfb12b1f348e/engineer)

*作者 swingerman* · 严谨的 agent 工程方法套件：需求受理、验收标准探索、规格、计划、实现、验证与加固。

**权限:** 运行命令, 调用模型

`/plugin install engineer@best-claude-code-mods`

## 推荐 mod

开一个 issue，附上 mod 仓库的链接。也可以自己添加：在 `community.json` 里加一条（仓库、目录、审核过的 commit、分类、许可证），在 `readme/summaries.json` 里写上各语言的一句话简介，运行 `python3 scripts/build-catalog.py`，然后提交 pull request。

## 致谢

每个 mod 归其作者所有，沿用各自的许可证；本仓库只做收录。作者如需修改或下架收录信息，请开 issue。

非官方项目，与 Anthropic 无关。
