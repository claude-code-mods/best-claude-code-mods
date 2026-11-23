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

**权限**一列是校验器报告的、该 mod 除绘制界面以外还能做的事。安装前请先看看它的源码：校验只是静态读取代码，并不运行它，也不等于安全审计。

### 仪表盘与用量

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 功能 | 权限 |
| --- | --- | --- |
| [`token-optimizer`](https://github.com/alexgreensh/token-optimizer/tree/e3f1a2dcad8d8999096b8a881c4d98cdba4ef1a5/desktop/token-optimizer-desktop)<br><sub>作者 alexgreensh · [🖼 preview](https://github.com/alexgreensh/token-optimizer)</sub> | token 优化状态栏，显示 token 去向并给出更省钱的调整。 | 运行命令, 调用模型, 读写文件 |
| [`claude-council`](https://github.com/hex/claude-council/tree/f2f7f42122b288599cef8cea97dcc490acea98a5)<br><sub>作者 hex · [🖼 preview](https://github.com/hex/claude-council)</sub> | 同时咨询多个 AI agent 获取多种视角，带流式面板和可选的额外复查提示。 | 运行命令, 调用模型, 读写文件 |
| [`codex-attachment-manager`](https://github.com/chipfighter/context-attachment-manager/tree/d68a721b7432059c9056d546ff2a26b11b3c0e0c)<br><sub>作者 chipfighter · [🖼 preview](https://github.com/chipfighter/context-attachment-manager)</sub> | 较早的图片以占位符发送、按 ID 取回原图，让长图片会话保住 prompt 缓存。 | 联网, MCP |
| [`cache-tax`](https://github.com/karanb192/cache-tax/tree/535ff33225e666e605e731d78f5ac5efe243c7c3)<br><sub>作者 karanb192 · [🖼 preview](https://github.com/karanb192/cache-tax)</sub> | 在休息时保持一小时 prompt 缓存温热，冷启动前先询问并显示重写成本。 | 调用模型 |
| [`agent-standup-band`](https://github.com/Atoll92/agent-standup/tree/846d5324f7c00f06d598c86e87ed8b51d774b3ac/plugin-band)<br><sub>作者 Atoll92 · [🖼 preview](https://github.com/Atoll92/agent-standup)</sub> | 本机其他会话需要你时在提示上方显示一行，结束时给一个提醒。 | 运行命令, 读写文件 |
| [`shunt`](https://github.com/pleaseai/shunt/tree/57182b328e92d3c70bc9ca5a1fd1ee9104cfbabb/plugins/shunt)<br><sub>作者 pleaseai · [🖼 preview](https://github.com/pleaseai/shunt)</sub> | shunt 网关的用量条：各窗口花费与重置时间，以及完整的 /shunt:usage 明细。 | 联网, 运行命令 |
| [`tokendoctor`](https://github.com/localixai/tokendoctor/tree/051fa9598f0a50ed30974b618f2911381b7dcf90)<br><sub>作者 localixai · [🖼 preview](https://github.com/localixai/tokendoctor)</sub> | 回放你过去的会话，展示每项改动能省多少，然后只应用你选择的改动。 | 运行命令, 调用模型 |
| [`skins`](https://github.com/hellosverre/claude-skins/tree/cf0d39f3785d5c5a4b6189ecc487b1ac479efea0)<br><sub>作者 hellosverre · [🖼 preview](https://github.com/hellosverre/claude-skins)</sub> | 转录皮肤的十五种主题、丰富卡片与用量条；/skin 实时切换。 | 联网, 运行命令, 调用模型, 读写文件 |
| [`ctx-handoff`](https://github.com/cablate/ctx-handoff-mod/tree/a416713a0495be799a31f3650e18458e242270c7)<br><sub>作者 cablate · [🖼 preview](https://github.com/cablate/ctx-handoff-mod)</sub> | 把你教给 Claude 的内容沉淀为项目笔记，捕捉常见疏漏，保温缓存并续接长会话。 | 调用模型, 读写文件 |
| [`great-cto`](https://github.com/avelikiy/great_cto/tree/12dfd86e99627cd6dd1ed394de4786f4ba08499b)<br><sub>作者 avelikiy · [🖼 preview](https://github.com/avelikiy/great_cto)</sub> | 把 Claude Code 当作 73 个专家 agent 的流水线运行，每个阶段由独立模型复核。 | 联网 |
| [`ripple`](https://github.com/PBJ-2/clauderipple/tree/c1c6b76a9e4e7a51df2ec5907d6e41d6bf8591e3/packages/mod)<br><sub>作者 PBJ-2 · [🖼 preview](https://github.com/PBJ-2/clauderipple)</sub> | 为每条提示选择推理强度、为每个委派任务选择执行者，保温缓存并显示请求去向。 | 联网, 运行命令, 调用模型, MCP, 读写文件 |
| [`tavernweave-agent-skills`](https://github.com/LiarMTTT/TavernWeave/tree/f9863d2b05305457fe9ed8b0c5688d52aca400a5)<br><sub>作者 LiarMTTT · [🖼 preview](https://github.com/LiarMTTT/TavernWeave)</sub> | 23 个共享技能用于角色卡、软件工作和有界云任务，提示上方有 Soul 模式开关。 | — |
| [`agent-usage-guard`](https://github.com/rbartoli/agent-usage-guard/tree/02594c2620be9eb60c32e2f77d9d512d9f61b205)<br><sub>作者 rbartoli · [🖼 preview](https://github.com/rbartoli/agent-usage-guard)</sub> | 在子 agent 扩散、重上下文提示和重试循环消耗你的用量窗口之前将其拦下。 | 调用模型, 读写文件 |

### Agent 与子 agent

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 功能 | 权限 |
| --- | --- | --- |
| [`shared-session`](https://github.com/Paradigm-Study/claude-share/tree/9d88f996ac4245c756a89b34e98cfde375028950/plugin)<br><sub>作者 Paradigm-Study · [🖼 preview](https://github.com/Paradigm-Study/claude-share)</sub> | 用链接或团队共享会话；队友用自己的 Claude Code 加入并实时看到每一轮。 | — |
| [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/626cc0b46d417f81bbff9f5ba3b49abaf8912a85)<br><sub>作者 scasella · [🖼 preview](https://github.com/scasella/claude-flightdeck)</sub> | 实时 agent 仪表盘：模型体征、值班架构师、权限检查、子 agent 卡片与会话日志。 | — |
| [`start`](https://github.com/rsmdt/the-startup/tree/e803d51fdb423271d3dde189f5416f3ec51386a9/plugins/start)<br><sub>作者 rsmdt · [🖼 preview](https://github.com/rsmdt/the-startup)</sub> | 面向 agent 软件开发的流程编排命令。 | 读写文件 |
| [`lane-stack`](https://github.com/VKirill/claude-lane-stack/tree/8bac2b876b72053aa445bb9d1c7c6079bfc4ba8c/plugins/lane-stack)<br><sub>作者 VKirill · [🖼 preview](https://github.com/VKirill/claude-lane-stack)</sub> | 单人 PM 流水线：编排 agent、泳道手册、入职与续接命令。 | 联网, 调用模型 |

### 效率与上下文

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 功能 | 权限 |
| --- | --- | --- |
| [`pebrel-prompt-suggestions`](https://github.com/Kuddev/pebrel/tree/ed9b2331340877ba3d775e38c4df6bd1a2abb1fe/pebrel_app/res/prompt-suggestions/claude)<br><sub>作者 Kuddev · [🖼 preview](https://github.com/Kuddev/pebrel)</sub> | 通过 Pebrel 会话桥在空输入框里给出原生提示预测。 | 联网 |
| [`fast-jev-compaction`](https://github.com/tamaratran/fast-jev-compaction/tree/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0)<br><sub>作者 tamaratran · [🖼 preview](https://github.com/tamaratran/fast-jev-compaction)</sub> | 为 Claude Code 会话提供逐字保留的 Jev 压缩。 | 联网, 调用模型 |
| [`lot-map`](https://github.com/alexeyw/lot-map/tree/ad60f057902765d778eedde770d337be45fac3af)<br><sub>作者 alexeyw · [🖼 preview](https://github.com/alexeyw/lot-map)</sub> | 聊天旁的实时地图：记忆、文件、Shell、网络、模型、agent、技能与 hooks 被使用时点亮。 | — |
| [`storybloq`](https://github.com/Storybloq/storybloq/tree/f0b4c08e3a15ffb9841e5a3058c6b1ca57607154/plugins/storybloq)<br><sub>作者 Storybloq · [🖼 preview](https://github.com/Storybloq/storybloq)</sub> | 项目记忆：把工单、问题、交接和经验存进仓库里的 .story/ 目录。 | 读写文件 |
| [`just-do-it`](https://github.com/Lifecycle-Innovations-Limited/claude-ops/tree/e434ef7e612f2ff5769def6101fc9d984888d377/claude-ops/skills/ops-jdi/plugin)<br><sub>作者 Lifecycle-Innovations-Limited · [🖼 preview](https://github.com/Lifecycle-Innovations-Limited/claude-ops)</sub> | 把已授权的工作推进到验证与交付，并暴露需要修复的配置问题。 | 运行命令, 调用模型 |
| [`filetree`](https://github.com/data-goblin/claude-code-filetree/tree/1fdc3a963f2dc22a939f661ff0ff5a76646c9112)<br><sub>作者 data-goblin · [🖼 preview](https://github.com/data-goblin/claude-code-filetree)</sub> | IDE 风格的目录树，显示 Claude 正在做什么、改到哪个文件。 | 运行命令, 调用模型, 读写文件 |
| [`jev-auto-compact`](https://github.com/notque/vexjoy-agent/tree/c68ac1fea2a03e437ccc95112d1e56e467a9bd00/plugins/jev-auto-compact)<br><sub>作者 notque · [🖼 preview](https://github.com/notque/vexjoy-agent)</sub> | 上下文到 60% 时以零生成裁剪陈旧工具调用；无可裁剪时跳过而非退化为 LLM 摘要。 | 联网, 调用模型 |
| [`caliber-jev-compaction`](https://github.com/caliber-ai-org/ai-setup/tree/f5dbc002022a8a10acad25c1cce23ddefdc19d0d/plugin/caliber-jev-compaction)<br><sub>作者 caliber-ai-org · [🖼 preview](https://github.com/caliber-ai-org/ai-setup)</sub> | 为 Claude Code 会话提供逐字保留的 Jev 压缩。 | 联网, 调用模型 |
| [`operator`](https://github.com/aerovato/operator-memory/tree/93c3fce64f0a72adeb89fa868600eb418548ec07/packages/claude-code)<br><sub>作者 aerovato · [🖼 preview](https://github.com/aerovato/operator-memory)</sub> | 面向 agent 开发的持久项目与用户记忆。 | — |
| [`claude-carbon`](https://github.com/gwittebolle/claude-carbon/tree/9ad53f1dd07fb0e11fcdb94d294ed794d660cf4b)<br><sub>作者 gwittebolle · [🖼 preview](https://github.com/gwittebolle/claude-carbon)</sub> | 在终端和桌面应用中追踪 Claude Code 会话的碳足迹。 | 读写文件 |
| [`work-mode`](https://github.com/danyuchn/claude-work-mode/tree/e19eda1e8465308bd79a74fad295cf9b6d9cdf71/plugins/work-mode)<br><sub>作者 danyuchn · [🖼 preview](https://github.com/danyuchn/claude-work-mode)</sub> | 会话模式：auto（不中途提问）、out（委派批量工作）、wrap（收敛并收尾）。 | 运行命令, 读写文件 |
| [`show-your-work`](https://github.com/iamumeransari/claude-show-your-work/tree/71e546044e3ba61b98a6938a03270da791f9ca2e)<br><sub>作者 iamumeransari · [🖼 preview](https://github.com/iamumeransari/claude-show-your-work)</sub> | 在终端里展示成品：截图、操作录屏和前后对比的 QA。 | 联网, 运行命令, 调用模型, 读写文件 |
| [`inbox`](https://github.com/petekp/inbox/tree/02e441cd447edf86fc30fbd03e9117a8ead9da7a)<br><sub>作者 petekp · [🖼 preview](https://github.com/petekp/inbox)</sub> | 汇总会话中等待你处理的问题、任务、发现与 PR。 | — |
| [`compact-adviser`](https://github.com/kunchenguid/compact-adviser/tree/37fa1a665b8933de68c90014312060e862cf121a/packages/claude-mod)<br><sub>作者 kunchenguid · [🖼 preview](https://github.com/kunchenguid/compact-adviser)</sub> | 在完成的检查点建议或执行 /compact，由 TypeSafe Jev 判定。 | 联网, 调用模型, 读写文件 |

### 渲染与预览

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 功能 | 权限 |
| --- | --- | --- |
| [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/fa9e5eb053d2a1da11f7ccba720a0d3d389c05a6/claude-code-plugin)<br><sub>作者 zenbu-labs · [🖼 preview](https://github.com/zenbu-labs/terminal-browser)</sub> | 内置在 Claude Code 里的浏览器：预览网站和 HTML，并可让 agent 操作这个浏览器。 | 联网, 运行命令, 调用模型, 读写文件 |
| [`prismantis`](https://github.com/NahumLitvin/prismantis/tree/3718a40abc57b836108a65bd9f01d06d3237e52d/plugin)<br><sub>作者 NahumLitvin · [🖼 preview](https://github.com/NahumLitvin/prismantis)</sub> | 为回复提供可换主题的彩色渲染：表格、标题、代码、数字、路径与链接。 | 运行命令, 读写文件 |

### 安全与守卫

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 功能 | 权限 |
| --- | --- | --- |
| [`lcu-approve`](https://github.com/amontlabs/lcu/tree/1bd45b304295c7665b559fcc32f7b3a8f1b1d859/adapters/claude-mod/lcu-approve)<br><sub>作者 amontlabs · [🖼 preview](https://github.com/amontlabs/lcu)</sub> | 电脑使用的按应用授权：本次允许、始终允许或拒绝，并有已授权应用面板。 | 运行命令, MCP, 读写文件 |
| [`agentctl`](https://github.com/sd0xdev/sd0x-harness/tree/b0206637edd2e44c993da12b6b30858f96bc3cdc/mods/agentctl)<br><sub>作者 sd0xdev · [🖼 preview](https://github.com/sd0xdev/sd0x-harness)</sub> | 会话级 agent 控制面板：任务范围、证据与交接。 | 运行命令, 调用模型, 读写文件 |
| [`multi-core`](https://github.com/greenpolo/cc-multi-cli-plugin/tree/66d9b0a6b06b25fd648ecd53311a647bb57e2fb4/plugins/multi-core)<br><sub>作者 greenpolo · [🖼 preview](https://github.com/greenpolo/cc-multi-cli-plugin)</sub> | 在单个会话里使用 ChatGPT、Cursor、OpenCode 与 Antigravity 模型，用 /model 切换。 | 联网, 调用模型 |
| [`jevmem-pane`](https://github.com/Avinash-jetwani/jevmem/tree/c29753ccb2c9706e417fda25efa422682358955b/pane)<br><sub>作者 Avinash-jetwani · [🖼 preview](https://github.com/Avinash-jetwani/jevmem)</sub> | 侧栏显示 jevmem 召回了什么、守卫判定什么、上一轮保存了什么。 | 运行命令, 读写文件 |

### Git、PR 与部署

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 功能 | 权限 |
| --- | --- | --- |
| [`fm`](https://github.com/kunchenguid/firstmate/tree/427056c4181c41074ad24f051f79919330df0fa5/.claude/mods/firstmate-calm)<br><sub>作者 kunchenguid · [🖼 preview](https://github.com/kunchenguid/firstmate)</sub> | 帆船工作动画与会话专用转录显示，跨会话共享 calm 模式偏好。 | 读写文件 |
| [`turbo`](https://github.com/tobihagemann/turbo/tree/3bc6b4436d96be22497109e16e68fe4dfa323531/claude)<br><sub>作者 tobihagemann · [🖼 preview](https://github.com/tobihagemann/turbo)</sub> | 人工把关的 agent 软件工厂：你决定做什么并验收，技能负责构建与发布。 | 调用模型, 读写文件 |
| [`mazyos`](https://github.com/Mazzeo-Marketing/MazyOS/tree/d2b65b392f1ee230afb088d155fc734def5f105d)<br><sub>作者 Mazzeo-Marketing · [🖼 preview](https://github.com/Mazzeo-Marketing/MazyOS)</sub> | 葡语商业操作插件：每次会话带入公司记忆、输出带品牌形象，并提供 17 个营销/SEO 技能。 | 读写文件 |
| [`engineer`](https://github.com/swingerman/engineer/tree/ae4cb5fe32007dd6a3d717c9998dcfb12b1f348e/engineer)<br><sub>作者 swingerman · [🖼 preview](https://github.com/swingerman/engineer)</sub> | 严谨的 agent 工程方法套件：需求受理、验收标准探索、规格、计划、实现、验证与加固。 | 运行命令, 调用模型 |

## 推荐 mod

开一个 issue，附上 mod 仓库的链接。也可以自己添加：在 `community.json` 里加一条（仓库、目录、审核过的 commit、分类、许可证），在 `readme/summaries.json` 里写上各语言的一句话简介，运行 `python3 scripts/build-catalog.py`，然后提交 pull request。

## 致谢

每个 mod 归其作者所有，沿用各自的许可证；本仓库只做收录。作者如需修改或下架收录信息，请开 issue。

非官方项目，与 Anthropic 无关。
