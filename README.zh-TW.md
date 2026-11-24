# Best Claude Code Mods · 精選 Claude Code 模組

[English](README.md) · [简体中文](README.zh-CN.md) · **繁體中文** · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

**逐一挑選、驗證、固定版本。新增一次，40 個 mod 隨裝隨用。**

Mod 是以函式鉤子寫成的 Claude Code 外掛：可以觀察、修改或接管 Claude Code 的行為，也能繪製自己的介面。這個市集收錄了社群中最好的 mod。每一個都以 `claude plugin validate` 驗證過，並固定在驗證時的 commit，作者之後的修改不會未經審核就到你這裡。

需要 Claude Code 2.1.287 或更新版本。

## 安裝

在 Claude Code 終端機工作階段中輸入：

```
/plugin marketplace add claude-code-mods/best-claude-code-mods
/plugin install <mod 名稱>@best-claude-code-mods
```

例如 `/plugin install terminal-browser@best-claude-code-mods`。執行 `/plugin marketplace update best-claude-code-mods` 取得新 mod 與更新。

## 目錄

每張卡片的**權限**是驗證工具回報的、該 mod 除了繪製介面以外還能做的事。安裝前請先看看它的原始碼：驗證只是靜態讀取程式碼，並不執行它，也不等於安全稽核。

### 儀表板與用量

[![token-optimizer](https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/docs-site/public/media/token-optimizer-desktop-status-bar.gif)](https://github.com/alexgreensh/token-optimizer/tree/e3f1a2dcad8d8999096b8a881c4d98cdba4ef1a5/desktop/token-optimizer-desktop)

#### [`token-optimizer`](https://github.com/alexgreensh/token-optimizer/tree/e3f1a2dcad8d8999096b8a881c4d98cdba4ef1a5/desktop/token-optimizer-desktop)

*作者 alexgreensh* · token 最佳化狀態列，顯示 token 去向並給出更省錢的調整。

**權限:** 執行指令, 呼叫模型, 讀寫檔案

`/plugin install token-optimizer@best-claude-code-mods`

---

[![council](https://github.com/hex/claude-council/raw/main/assets/desktop-code-tab.png)](https://github.com/hex/claude-council/tree/f2f7f42122b288599cef8cea97dcc490acea98a5)

#### [`council`](https://github.com/hex/claude-council/tree/f2f7f42122b288599cef8cea97dcc490acea98a5)

*作者 hex* · 同時諮詢多個 AI agent 獲取多種視角，帶流式面板和可選的額外複查提示。

**權限:** 執行指令, 呼叫模型, 讀寫檔案

`/plugin install council@best-claude-code-mods`

---

[![codex-attachment-manager](https://github.com/chipfighter/context-attachment-manager/raw/main/docs/images/hero.gif)](https://github.com/chipfighter/context-attachment-manager/tree/d68a721b7432059c9056d546ff2a26b11b3c0e0c)

#### [`codex-attachment-manager`](https://github.com/chipfighter/context-attachment-manager/tree/d68a721b7432059c9056d546ff2a26b11b3c0e0c)

*作者 chipfighter* · 較早的圖片以佔位符傳送、按 ID 取回原圖，讓長圖片會話保住 prompt 快取。

**權限:** 連網, MCP

`/plugin install codex-attachment-manager@best-claude-code-mods`

---

[![cache-tax](https://github.com/karanb192/cache-tax/raw/main/site/assets/refusal.gif)](https://github.com/karanb192/cache-tax/tree/535ff33225e666e605e731d78f5ac5efe243c7c3)

#### [`cache-tax`](https://github.com/karanb192/cache-tax/tree/535ff33225e666e605e731d78f5ac5efe243c7c3)

*作者 karanb192* · 在休息時保持一小時 prompt 快取溫熱，冷啟動前先詢問並顯示重寫成本。

**權限:** 呼叫模型

`/plugin install cache-tax@best-claude-code-mods`

---

[![agent-standup-band](https://atoll92.github.io/agent-standup/media/banner.png)](https://github.com/Atoll92/agent-standup/tree/846d5324f7c00f06d598c86e87ed8b51d774b3ac/plugin-band)

#### [`agent-standup-band`](https://github.com/Atoll92/agent-standup/tree/846d5324f7c00f06d598c86e87ed8b51d774b3ac/plugin-band)

*作者 Atoll92* · 本機其他會話需要你時在提示上方顯示一行，結束時給一個提醒。

**權限:** 執行指令, 讀寫檔案

`/plugin install agent-standup-band@best-claude-code-mods`

---

[![shunt](docs/assets/shunt.png)](https://github.com/pleaseai/shunt/tree/57182b328e92d3c70bc9ca5a1fd1ee9104cfbabb/plugins/shunt)

#### [`shunt`](https://github.com/pleaseai/shunt/tree/57182b328e92d3c70bc9ca5a1fd1ee9104cfbabb/plugins/shunt)

*作者 pleaseai* · shunt 閘道器的用量條：各視窗花費與重置時間，以及完整的 /shunt:usage 明細。

**權限:** 連網, 執行指令

`/plugin install shunt@best-claude-code-mods`

---

[![tokendoctor](https://github.com/localixai/tokendoctor/raw/main/docs/demo.gif)](https://github.com/localixai/tokendoctor/tree/051fa9598f0a50ed30974b618f2911381b7dcf90)

#### [`tokendoctor`](https://github.com/localixai/tokendoctor/tree/051fa9598f0a50ed30974b618f2911381b7dcf90)

*作者 localixai* · 回放你過去的會話，展示每項改動能省多少，然後只應用你選擇的改動。

**權限:** 執行指令, 呼叫模型

`/plugin install tokendoctor@best-claude-code-mods`

---

[![skins](https://github.com/hellosverre/claude-skins/raw/main/docs/demo.gif)](https://github.com/hellosverre/claude-skins/tree/cf0d39f3785d5c5a4b6189ecc487b1ac479efea0)

#### [`skins`](https://github.com/hellosverre/claude-skins/tree/cf0d39f3785d5c5a4b6189ecc487b1ac479efea0)

*作者 hellosverre* · 轉錄皮膚的十五種主題、豐富卡片與用量條；/skin 即時切換。

**權限:** 連網, 執行指令, 呼叫模型, 讀寫檔案

`/plugin install skins@best-claude-code-mods`

---

[![ctx-handoff](docs/assets/ctx-handoff-mod.png)](https://github.com/cablate/ctx-handoff-mod/tree/a416713a0495be799a31f3650e18458e242270c7)

#### [`ctx-handoff`](https://github.com/cablate/ctx-handoff-mod/tree/a416713a0495be799a31f3650e18458e242270c7)

*作者 cablate* · 把你教給 Claude 的內容沉澱為專案筆記，捕捉常見疏漏，保溫快取並續接長會話。

**權限:** 呼叫模型, 讀寫檔案

`/plugin install ctx-handoff@best-claude-code-mods`

---

[![ripple](https://github.com/PBJ-2/clauderipple/raw/main/docs/media/demo.webp)](https://github.com/PBJ-2/clauderipple/tree/c1c6b76a9e4e7a51df2ec5907d6e41d6bf8591e3/packages/mod)

#### [`ripple`](https://github.com/PBJ-2/clauderipple/tree/c1c6b76a9e4e7a51df2ec5907d6e41d6bf8591e3/packages/mod)

*作者 PBJ-2* · 為每條提示選擇推理強度、為每個委派任務選擇執行者，保溫快取並顯示請求去向。

**權限:** 連網, 執行指令, 呼叫模型, MCP, 讀寫檔案

`/plugin install ripple@best-claude-code-mods`

---

[![tavernweave-agent-skills](https://github.com/LiarMTTT/TavernWeave/raw/main/docs/assets/tavernweave-v1-cover.png)](https://github.com/LiarMTTT/TavernWeave/tree/f9863d2b05305457fe9ed8b0c5688d52aca400a5)

#### [`tavernweave-agent-skills`](https://github.com/LiarMTTT/TavernWeave/tree/f9863d2b05305457fe9ed8b0c5688d52aca400a5)

*作者 LiarMTTT* · 23 個共享技能用於角色卡、軟體工作和有界雲任務，提示上方有 Soul 模式開關。

**權限:** —

`/plugin install tavernweave-agent-skills@best-claude-code-mods`

---

[![agent-usage-guard](https://github.com/rbartoli/agent-usage-guard/releases/download/agent-usage-guard--v1.0.0/agent-usage-guard.gif)](https://github.com/rbartoli/agent-usage-guard/tree/02594c2620be9eb60c32e2f77d9d512d9f61b205)

#### [`agent-usage-guard`](https://github.com/rbartoli/agent-usage-guard/tree/02594c2620be9eb60c32e2f77d9d512d9f61b205)

*作者 rbartoli* · 在子 agent 擴散、重上下文提示和重試迴圈消耗你的用量視窗之前將其攔下。

**權限:** 呼叫模型, 讀寫檔案

`/plugin install agent-usage-guard@best-claude-code-mods`


### Agent 與子 agent

[![shared-session](https://github.com/Paradigm-Study/claude-share/raw/main/docs/assets/invitation-demo.png)](https://github.com/Paradigm-Study/claude-share/tree/9d88f996ac4245c756a89b34e98cfde375028950/plugin)

#### [`shared-session`](https://github.com/Paradigm-Study/claude-share/tree/9d88f996ac4245c756a89b34e98cfde375028950/plugin)

*作者 Paradigm-Study* · 用連結或團隊共享會話；隊友用自己的 Claude Code 加入並即時看到每一輪。

**權限:** —

`/plugin install shared-session@best-claude-code-mods`

---

[![flightdeck](https://github.com/scasella/claude-flightdeck/raw/main/docs/media/demo.gif)](https://github.com/scasella/claude-flightdeck/tree/626cc0b46d417f81bbff9f5ba3b49abaf8912a85)

#### [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/626cc0b46d417f81bbff9f5ba3b49abaf8912a85)

*作者 scasella* · 即時 agent 儀表盤：模型體徵、值班架構師、許可權檢查、子 agent 卡片與會話日誌。

**權限:** —

`/plugin install flightdeck@best-claude-code-mods`

---

[![start](https://github.com/rsmdt/the-startup/raw/main/logo.png)](https://github.com/rsmdt/the-startup/tree/e803d51fdb423271d3dde189f5416f3ec51386a9/plugins/start)

#### [`start`](https://github.com/rsmdt/the-startup/tree/e803d51fdb423271d3dde189f5416f3ec51386a9/plugins/start)

*作者 rsmdt* · 面向 agent 軟體開發的流程編排命令。

**權限:** 讀寫檔案

`/plugin install start@best-claude-code-mods`

---

[![lane-stack](docs/assets/claude-lane-stack.png)](https://github.com/VKirill/claude-lane-stack/tree/8bac2b876b72053aa445bb9d1c7c6079bfc4ba8c/plugins/lane-stack)

#### [`lane-stack`](https://github.com/VKirill/claude-lane-stack/tree/8bac2b876b72053aa445bb9d1c7c6079bfc4ba8c/plugins/lane-stack)

*作者 VKirill* · 單人 PM 流水線：編排 agent、泳道手冊、入職與續接命令。

**權限:** 連網, 呼叫模型

`/plugin install lane-stack@best-claude-code-mods`


### 效率與上下文

[![pebrel-prompt-suggestions](https://github.com/Kuddev/pebrel/raw/main/docs/screenshots/nebula-claude-session.png)](https://github.com/Kuddev/pebrel/tree/ed9b2331340877ba3d775e38c4df6bd1a2abb1fe/pebrel_app/res/prompt-suggestions/claude)

#### [`pebrel-prompt-suggestions`](https://github.com/Kuddev/pebrel/tree/ed9b2331340877ba3d775e38c4df6bd1a2abb1fe/pebrel_app/res/prompt-suggestions/claude)

*作者 Kuddev* · 透過 Pebrel 會話橋在空輸入框裡給出原生提示預測。

**權限:** 連網

`/plugin install pebrel-prompt-suggestions@best-claude-code-mods`

---

[![fast-jev-compaction](docs/assets/fast-jev-compaction.png)](https://github.com/tamaratran/fast-jev-compaction/tree/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0)

#### [`fast-jev-compaction`](https://github.com/tamaratran/fast-jev-compaction/tree/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0)

*作者 tamaratran* · 為 Claude Code 會話提供逐字保留的 Jev 壓縮。

**權限:** 連網, 呼叫模型

`/plugin install fast-jev-compaction@best-claude-code-mods`

---

[![lot-map](https://github.com/alexeyw/lot-map/raw/main/docs/demo.gif)](https://github.com/alexeyw/lot-map/tree/ad60f057902765d778eedde770d337be45fac3af)

#### [`lot-map`](https://github.com/alexeyw/lot-map/tree/ad60f057902765d778eedde770d337be45fac3af)

*作者 alexeyw* · 聊天旁的即時地圖：記憶、檔案、Shell、網路、模型、agent、技能與 hooks 被使用時點亮。

**權限:** —

`/plugin install lot-map@best-claude-code-mods`

---

[![storybloq](https://raw.githubusercontent.com/Storybloq/storybloq/main/assets/board.png)](https://github.com/Storybloq/storybloq/tree/f0b4c08e3a15ffb9841e5a3058c6b1ca57607154/plugins/storybloq)

#### [`storybloq`](https://github.com/Storybloq/storybloq/tree/f0b4c08e3a15ffb9841e5a3058c6b1ca57607154/plugins/storybloq)

*作者 Storybloq* · 專案記憶：把工單、問題、交接和經驗存進倉庫裡的 .story/ 目錄。

**權限:** 讀寫檔案

`/plugin install storybloq@best-claude-code-mods`

---

[![just-do-it](docs/assets/claude-ops.png)](https://github.com/Lifecycle-Innovations-Limited/claude-ops/tree/e434ef7e612f2ff5769def6101fc9d984888d377/claude-ops/skills/ops-jdi/plugin)

#### [`just-do-it`](https://github.com/Lifecycle-Innovations-Limited/claude-ops/tree/e434ef7e612f2ff5769def6101fc9d984888d377/claude-ops/skills/ops-jdi/plugin)

*作者 Lifecycle-Innovations-Limited* · 把已授權的工作推進到驗證與交付，並暴露需要修復的配置問題。

**權限:** 執行指令, 呼叫模型

`/plugin install just-do-it@best-claude-code-mods`

---

[![filetree](https://github.com/data-goblin/claude-code-filetree/raw/main/media/filetree-shimmer.gif)](https://github.com/data-goblin/claude-code-filetree/tree/1fdc3a963f2dc22a939f661ff0ff5a76646c9112)

#### [`filetree`](https://github.com/data-goblin/claude-code-filetree/tree/1fdc3a963f2dc22a939f661ff0ff5a76646c9112)

*作者 data-goblin* · IDE 風格的目錄樹，顯示 Claude 正在做什麼、改到哪個檔案。

**權限:** 執行指令, 呼叫模型, 讀寫檔案

`/plugin install filetree@best-claude-code-mods`

---

[![jev-auto-compact](https://github.com/notque/vexjoy-agent/raw/main/docs/repo-hero.png)](https://github.com/notque/vexjoy-agent/tree/c68ac1fea2a03e437ccc95112d1e56e467a9bd00/plugins/jev-auto-compact)

#### [`jev-auto-compact`](https://github.com/notque/vexjoy-agent/tree/c68ac1fea2a03e437ccc95112d1e56e467a9bd00/plugins/jev-auto-compact)

*作者 notque* · 上下文到 60% 時以零生成裁剪陳舊工具呼叫；無可裁剪時跳過而非退化為 LLM 摘要。

**權限:** 連網, 呼叫模型

`/plugin install jev-auto-compact@best-claude-code-mods`

---

[![caliber-jev-compaction](https://github.com/caliber-ai-org/ai-setup/raw/master/assets/readme/pillars.png)](https://github.com/caliber-ai-org/ai-setup/tree/f5dbc002022a8a10acad25c1cce23ddefdc19d0d/plugin/caliber-jev-compaction)

#### [`caliber-jev-compaction`](https://github.com/caliber-ai-org/ai-setup/tree/f5dbc002022a8a10acad25c1cce23ddefdc19d0d/plugin/caliber-jev-compaction)

*作者 caliber-ai-org* · 為 Claude Code 會話提供逐字保留的 Jev 壓縮。

**權限:** 連網, 呼叫模型

`/plugin install caliber-jev-compaction@best-claude-code-mods`

---

[![operator](https://github.com/aerovato/operator-memory/raw/main/docs/assets/change-the-loop.png)](https://github.com/aerovato/operator-memory/tree/93c3fce64f0a72adeb89fa868600eb418548ec07/packages/claude-code)

#### [`operator`](https://github.com/aerovato/operator-memory/tree/93c3fce64f0a72adeb89fa868600eb418548ec07/packages/claude-code)

*作者 aerovato* · 面向 agent 開發的持久專案與使用者記憶。

**權限:** —

`/plugin install operator@best-claude-code-mods`

---

[![carbon](https://github.com/gwittebolle/claude-carbon/raw/main/docs/desktop-pane.png)](https://github.com/gwittebolle/claude-carbon/tree/9ad53f1dd07fb0e11fcdb94d294ed794d660cf4b)

#### [`carbon`](https://github.com/gwittebolle/claude-carbon/tree/9ad53f1dd07fb0e11fcdb94d294ed794d660cf4b)

*作者 gwittebolle* · 在終端和桌面應用中追蹤 Claude Code 會話的碳足跡。

**權限:** 讀寫檔案

`/plugin install carbon@best-claude-code-mods`

---

[![work-mode](https://github.com/danyuchn/claude-work-mode/raw/main/promo/demo-poster-en.png)](https://github.com/danyuchn/claude-work-mode/tree/e19eda1e8465308bd79a74fad295cf9b6d9cdf71/plugins/work-mode)

#### [`work-mode`](https://github.com/danyuchn/claude-work-mode/tree/e19eda1e8465308bd79a74fad295cf9b6d9cdf71/plugins/work-mode)

*作者 danyuchn* · 會話模式：auto（不中途提問）、out（委派批次工作）、wrap（收斂並收尾）。

**權限:** 執行指令, 讀寫檔案

`/plugin install work-mode@best-claude-code-mods`

---

[![show-your-work](https://github.com/iamumeransari/claude-show-your-work/raw/main/docs/homepage.jpg)](https://github.com/iamumeransari/claude-show-your-work/tree/71e546044e3ba61b98a6938a03270da791f9ca2e)

#### [`show-your-work`](https://github.com/iamumeransari/claude-show-your-work/tree/71e546044e3ba61b98a6938a03270da791f9ca2e)

*作者 iamumeransari* · 在終端裡展示成品：截圖、操作錄屏和前後對比的 QA。

**權限:** 連網, 執行指令, 呼叫模型, 讀寫檔案

`/plugin install show-your-work@best-claude-code-mods`

---

[![inbox](docs/assets/inbox.png)](https://github.com/petekp/inbox/tree/02e441cd447edf86fc30fbd03e9117a8ead9da7a)

#### [`inbox`](https://github.com/petekp/inbox/tree/02e441cd447edf86fc30fbd03e9117a8ead9da7a)

*作者 petekp* · 彙總會話中等待你處理的問題、任務、發現與 PR。

**權限:** —

`/plugin install inbox@best-claude-code-mods`

---

[![compact-adviser](https://github.com/kunchenguid/compact-adviser/raw/main/docs/hint-status-line.png)](https://github.com/kunchenguid/compact-adviser/tree/37fa1a665b8933de68c90014312060e862cf121a/packages/claude-mod)

#### [`compact-adviser`](https://github.com/kunchenguid/compact-adviser/tree/37fa1a665b8933de68c90014312060e862cf121a/packages/claude-mod)

*作者 kunchenguid* · 在完成的檢查點建議或執行 /compact，由 TypeSafe Jev 判定。

**權限:** 連網, 呼叫模型, 讀寫檔案

`/plugin install compact-adviser@best-claude-code-mods`


### 呈現與預覽

[![terminal-browser](docs/assets/terminal-browser.webp)](https://github.com/zenbu-labs/terminal-browser/tree/fa9e5eb053d2a1da11f7ccba720a0d3d389c05a6/claude-code-plugin)

#### [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/fa9e5eb053d2a1da11f7ccba720a0d3d389c05a6/claude-code-plugin)

*作者 zenbu-labs* · 內建在 Claude Code 裡的瀏覽器：預覽網站和 HTML，並可讓 agent 操作這個瀏覽器。

**權限:** 連網, 執行指令, 呼叫模型, 讀寫檔案

`/plugin install terminal-browser@best-claude-code-mods`

---

[![prismantis](https://github.com/NahumLitvin/prismantis/raw/main/docs/tour.gif)](https://github.com/NahumLitvin/prismantis/tree/3718a40abc57b836108a65bd9f01d06d3237e52d/plugin)

#### [`prismantis`](https://github.com/NahumLitvin/prismantis/tree/3718a40abc57b836108a65bd9f01d06d3237e52d/plugin)

*作者 NahumLitvin* · 為回覆提供可換主題的彩色渲染：表格、標題、程式碼、數字、路徑與連結。

**權限:** 執行指令, 讀寫檔案

`/plugin install prismantis@best-claude-code-mods`


### 安全與防護

[![lcu-approve](https://github.com/amontlabs/lcu/raw/main/docs/assets/approval-demo.gif)](https://github.com/amontlabs/lcu/tree/1bd45b304295c7665b559fcc32f7b3a8f1b1d859/adapters/claude-mod/lcu-approve)

#### [`lcu-approve`](https://github.com/amontlabs/lcu/tree/1bd45b304295c7665b559fcc32f7b3a8f1b1d859/adapters/claude-mod/lcu-approve)

*作者 amontlabs* · 電腦使用的按應用授權：本次允許、始終允許或拒絕，並有已授權應用面板。

**權限:** 執行指令, MCP, 讀寫檔案

`/plugin install lcu-approve@best-claude-code-mods`

---

[![agentctl](https://raw.githubusercontent.com/sd0xdev/sd0x-harness/main/banner.jpg)](https://github.com/sd0xdev/sd0x-harness/tree/b0206637edd2e44c993da12b6b30858f96bc3cdc/mods/agentctl)

#### [`agentctl`](https://github.com/sd0xdev/sd0x-harness/tree/b0206637edd2e44c993da12b6b30858f96bc3cdc/mods/agentctl)

*作者 sd0xdev* · 會話級 agent 控制面板：任務範圍、證據與交接。

**權限:** 執行指令, 呼叫模型, 讀寫檔案

`/plugin install agentctl@best-claude-code-mods`

---

[![multi-core](docs/assets/cc-multi-cli-plugin.png)](https://github.com/greenpolo/cc-multi-cli-plugin/tree/66d9b0a6b06b25fd648ecd53311a647bb57e2fb4/plugins/multi-core)

#### [`multi-core`](https://github.com/greenpolo/cc-multi-cli-plugin/tree/66d9b0a6b06b25fd648ecd53311a647bb57e2fb4/plugins/multi-core)

*作者 greenpolo* · 在單個會話裡使用 ChatGPT、Cursor、OpenCode 與 Antigravity 模型，用 /model 切換。

**權限:** 連網, 呼叫模型

`/plugin install multi-core@best-claude-code-mods`

---

[![jevmem-pane](docs/assets/jevmem.png)](https://github.com/Avinash-jetwani/jevmem/tree/c29753ccb2c9706e417fda25efa422682358955b/pane)

#### [`jevmem-pane`](https://github.com/Avinash-jetwani/jevmem/tree/c29753ccb2c9706e417fda25efa422682358955b/pane)

*作者 Avinash-jetwani* · 側欄顯示 jevmem 召回了什麼、守衛判定什麼、上一輪儲存了什麼。

**權限:** 執行指令, 讀寫檔案

`/plugin install jevmem-pane@best-claude-code-mods`


### Git、PR 與部署

[![fm](https://github.com/kunchenguid/firstmate/raw/main/assets/banner.png)](https://github.com/kunchenguid/firstmate/tree/427056c4181c41074ad24f051f79919330df0fa5/.claude/mods/firstmate-calm)

#### [`fm`](https://github.com/kunchenguid/firstmate/tree/427056c4181c41074ad24f051f79919330df0fa5/.claude/mods/firstmate-calm)

*作者 kunchenguid* · 帆船工作動畫與會話專用轉錄顯示，跨會話共享 calm 模式偏好。

**權限:** 讀寫檔案

`/plugin install fm@best-claude-code-mods`

---

[![turbo](https://github.com/tobihagemann/turbo/raw/main/assets/logo/thunderbolt-icon-256.png)](https://github.com/tobihagemann/turbo/tree/3bc6b4436d96be22497109e16e68fe4dfa323531/claude)

#### [`turbo`](https://github.com/tobihagemann/turbo/tree/3bc6b4436d96be22497109e16e68fe4dfa323531/claude)

*作者 tobihagemann* · 人工把關的 agent 軟體工廠：你決定做什麼並驗收，技能負責構建與釋出。

**權限:** 呼叫模型, 讀寫檔案

`/plugin install turbo@best-claude-code-mods`

---

[![mazyos](docs/assets/MazyOS.png)](https://github.com/Mazzeo-Marketing/MazyOS/tree/d2b65b392f1ee230afb088d155fc734def5f105d)

#### [`mazyos`](https://github.com/Mazzeo-Marketing/MazyOS/tree/d2b65b392f1ee230afb088d155fc734def5f105d)

*作者 Mazzeo-Marketing* · 葡語商業操作外掛：每次會話帶入公司記憶、輸出帶品牌形象，並提供 17 個營銷/SEO 技能。

**權限:** 讀寫檔案

`/plugin install mazyos@best-claude-code-mods`

---

[![engineer](docs/assets/engineer.png)](https://github.com/swingerman/engineer/tree/ae4cb5fe32007dd6a3d717c9998dcfb12b1f348e/engineer)

#### [`engineer`](https://github.com/swingerman/engineer/tree/ae4cb5fe32007dd6a3d717c9998dcfb12b1f348e/engineer)

*作者 swingerman* · 嚴謹的 agent 工程方法套件：需求受理、驗收標準探索、規格、計劃、實現、驗證與加固。

**權限:** 執行指令, 呼叫模型

`/plugin install engineer@best-claude-code-mods`

## 推薦 mod

開一個 issue，附上 mod 儲存庫的連結。也可以自己新增：在 `community.json` 加一筆（儲存庫、目錄、審核過的 commit、分類、授權），在 `readme/summaries.json` 寫上各語言的一句話簡介，執行 `python3 scripts/build-catalog.py`，再送出 pull request。

## 致謝

每個 mod 歸其作者所有，沿用各自的授權；本儲存庫只負責收錄。作者如需修改或下架收錄資訊，請開 issue。

非官方專案，與 Anthropic 無關。
