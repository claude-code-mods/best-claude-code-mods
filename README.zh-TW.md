# Best Claude Code Mods · 精選 Claude Code 模組

[English](README.md) · [简体中文](README.zh-CN.md) · **繁體中文** · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

**逐一挑選、驗證、固定版本。新增一次，43 個 mod 隨裝隨用。**

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

**權限**一欄是驗證工具回報的、該 mod 除了繪製介面以外還能做的事。安裝前請先看看它的原始碼：驗證只是靜態讀取程式碼，並不執行它，也不等於安全稽核。

### 儀表板與用量

| Mod | 功能 | 權限 |
| --- | --- | --- |
| [`cache-clock`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/cache-clock)<br><sub>作者 hamzafer</sub> | 狀態列下一行：提示快取還能保溫幾分鐘，冷掉後下一則要重新快取多少 token | 讀寫檔案, 執行指令 |
| [`context-bar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/context-bar)<br><sub>作者 hamzafer</sub> | 上下文視窗依類別分色的堆疊條，含 token 數與壓縮點（/context-bar 開關） | — |
| [`openai-balance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/openai-balance)<br><sub>作者 hamzafer</sub> | OpenAI API 餘額估算、今日花費與主要去向（/openai-balance） | 連網, 執行指令 |
| [`token-weather`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/token-weather)<br><sub>作者 hamzafer</sub> | 把上下文占用畫成天氣預報，附提示快取倒數 | 讀寫檔案, 執行指令 |
| [`usage-meter`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/usage-meter)<br><sub>作者 hamzafer</sub> | 5 小時與 7 天用量的小進度條，附重置倒數和本工作階段費用 | — |
| [`usage-band`](https://github.com/JetsonChan/CC-Usage-Band/tree/60cd60949b1f52c96ddba3ea24ed0848ff302196/usage-band)<br><sub>作者 JetsonChan</sub> | 輸入框上方顯示 5 小時／7 天額度、上下文和快取命中率，終端機與桌面版皆適用 | — |
| [`context-view`](https://github.com/kongyo2/context-view/tree/137e4e3db754684144ec953c5e66085bc2959766)<br><sub>作者 kongyo2</sub> | 一行顯示上下文占用，樣式與 Claude Code 內建儀表相同，含距離自動壓縮還剩多少 | — |
| [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/f31daca523d36c501cd0df23a737a44c7dc56ad6)<br><sub>作者 scasella</sub> | agent 儀表板：模型狀態、每次權限判定、子 agent 卡片與泳道、本輪收據、工作階段紀錄 | — |
| [`cctop`](https://github.com/tomstagl/cctop/tree/6ceafc34a972f4e58d5e53b1c69f80e2a9759d41/plugin)<br><sub>作者 tomstagl</sub> | btop 風格的即時面板：上下文、token、費用、快取命中、額度、各工具耗時（/cctop） | 讀寫檔案, 執行指令 |
| [`statuspane`](https://github.com/xuanji86/claude-statuspane/tree/13bd8e46edefdf282f117941b886cb529c7d79c3)<br><sub>作者 xuanji86</sub> | 輸入框上方的浮動狀態卡：模型、effort、上下文、5 小時／週額度、費用、分支、CI | 讀寫檔案, 執行指令 |
| [`plan-progress`](https://github.com/zycck/claude-mods/tree/3539d02d7435397d293e3120ebad22c23214f6c0/plugins/plan-progress)<br><sub>作者 zycck</sub> | 輸入框上方的計畫進度條：階段、步驟、像素填色，決策／出錯／完成時有提示音 | 讀寫檔案, 執行指令 |

### Agent 與子 agent

| Mod | 功能 | 權限 |
| --- | --- | --- |
| [`agent-flow`](https://github.com/Charlie0113-T/claude-agent-flow/tree/d87b2559dec03979e088026e8f48aee5f9d2cab5)<br><sub>作者 Charlie0113-T</sub> | /flow 在對話旁開啟子 agent 與隊友的即時樹狀圖 | — |
| [`agent-radar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/agent-radar)<br><sub>作者 hamzafer</sub> | 每個執行中的子 agent 一行：用時、工具次數、正在做什麼（/radar 看全部） | — |
| [`browser-lanes`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/browser-lanes)<br><sub>作者 hamzafer</sub> | 顯示 Playwright 瀏覽器被誰占用；子 agent 要用時排隊，/browser clean 清理殘留 | 執行指令 |
| [`mission-control`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/mission-control)<br><sub>作者 hamzafer</sub> | /mission 開啟主 agent、子 agent 與所有工具呼叫的即時地圖，外加檔案程式碼地圖 | 讀寫檔案, 呼叫模型, 執行指令 |
| [`review-watch`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/review-watch)<br><sub>作者 hamzafer</sub> | 每個進行中的程式碼審查（Codex 或審查子 agent）一行即時狀態，結束時跳出結論 | 執行指令 |
| [`switchboard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/switchboard)<br><sub>作者 hamzafer</sub> | 為沒指定模型的子 agent 自動選模型（呼叫 OpenAI Decisions API 或 Jev），/route 查看選擇與花費 | 連網 |
| [`agentpane`](https://github.com/xuanji86/claude-agentpane/tree/17be88979e5782591a2a184959df1c4168600066)<br><sub>作者 xuanji86</sub> | 側邊面板列出子 agent：各自在做什麼、花了多少 token，點開看它的對話 | — |

### 效率與上下文

| Mod | 功能 | 權限 |
| --- | --- | --- |
| [`glance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/glance)<br><sub>作者 hamzafer</sub> | 一行顯示需要你處理的事：下一場會議、PR、Linear 任務、Slack 私訊（透過已連線的 MCP） | MCP, 執行指令 |
| [`next-steps`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/next-steps)<br><sub>作者 hamzafer</sub> | 每輪結束後提供 2–3 個可能的下一則提示，在空白輸入框按 1/2/3 選用 | 呼叫模型 |
| [`session-saver`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/session-saver)<br><sub>作者 hamzafer</sub> | 替未命名的工作階段命名；/park 記下進度，恢復時顯示 | 呼叫模型, 執行指令 |
| [`where-am-i`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/where-am-i)<br><sub>作者 hamzafer</sub> | 輸入框上方即時摘要：目標、正在做、等你處理、下一步（/where 看詳細） | 呼叫模型 |
| [`aside`](https://github.com/JayDoubleu/aside/tree/cf2b7562ae7b376cdcf9e2436a926aba77dc759f)<br><sub>作者 JayDoubleu</sub> | 唯讀旁聊：/aside 在側邊詢問關於目前工作階段的問題，不寫回主對話 | 呼叫模型 |
| [`lcm`](https://github.com/lossless-claude/lcm/tree/0c17dbffda452cf7fae46929af427dff355aeaa3)<br><sub>作者 lossless-claude</sub> | 無損上下文管理：以 DAG 做分層摘要，每則訊息都還能找回 | 讀寫檔案, 連網, 呼叫模型, 執行指令 |

### 呈現與預覽

| Mod | 功能 | 權限 |
| --- | --- | --- |
| [`gfm-render`](https://github.com/briangtn/claude-gfm-render/tree/a209ad5a0ec35c0813d2d80ab62b596140b0c807)<br><sub>作者 briangtn</sub> | 在對話裡渲染 GitHub 風格 Markdown：提示區塊、任務清單、刪除線、Mermaid 圖 | 執行指令 |
| [`md-preview`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/md-preview)<br><sub>作者 hamzafer</sub> | Claude 編輯的 Markdown 檔案在側邊面板以 GitHub 樣式呈現，修改前後對照（/md） | 讀寫檔案, 執行指令 |
| [`replay-theater`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/replay-theater)<br><sub>作者 hamzafer</sub> | 逐一 diff 回放上一輪的檔案修改 | 讀寫檔案 |
| [`skins`](https://github.com/hellosverre/claude-skins/tree/342fbc0dd49ec44c824ed9c8eb95cd4927d7f81a)<br><sub>作者 hellosverre</sub> | 替對話紀錄換外觀：工具列、回覆邊欄和 spinner 文字，/skin 即時切換 | — |
| [`mdview`](https://github.com/xuanji86/claude-mdview/tree/da646556714507acf5d41610605b9911eb9aa42a)<br><sub>作者 xuanji86</sub> | 點擊對話裡的 .md 路徑，在旁邊渲染閱讀（含圖片），還能指著某段讓 Claude 修改 | 讀寫檔案, 執行指令 |
| [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/2165ae76c9639e3996829ab0e6d54ddbd4f06ad8/claude-code-plugin)<br><sub>作者 zenbu-labs</sub> | 在對話旁開一個瀏覽器：預覽網頁和本機 HTML，也能讓 agent 操作它 | 讀寫檔案, 連網, 執行指令 |

### 安全與防護

| Mod | 功能 | 權限 |
| --- | --- | --- |
| [`blast-radius`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/blast-radius)<br><sub>作者 hamzafer</sub> | 攔下有風險的 Bash 指令，先顯示會改動什麼再讓你確認 | 執行指令 |
| [`merge-gate`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/merge-gate)<br><sub>作者 hamzafer</sub> | `gh pr merge` 要等 CI 通過並跑過一次 Codex 審查才放行 | 讀寫檔案, 執行指令 |
| [`rulebook-guard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/rulebook-guard)<br><sub>作者 hamzafer</sub> | 寫作與 git 規則：替換內文的破折號；amend、未格式化的 push、提交含個人資訊時先問你 | 讀寫檔案, 執行指令 |
| [`secret-redactor`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/secret-redactor)<br><sub>作者 ray-amjad</sub> | 金鑰、電子郵件、IP 進入對話前換成固定佔位符，呼叫工具時再換回真實值 | — |

### Git、PR 與部署

| Mod | 功能 | 權限 |
| --- | --- | --- |
| [`vercel-deploy-status`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/vercel-deploy-status)<br><sub>作者 ray-amjad</sub> | 在輸入框下方固定顯示目前專案的 Vercel 部署佇列與進度 | 讀寫檔案, 執行指令 |
| [`cc-pr-tracker`](https://github.com/sezaakgun/cc-pr-tracker/tree/2d96fc7ed6bcca44a350700ac4c37e9066d58b46)<br><sub>作者 sezaakgun</sub> | 追蹤 GitHub PR 的合併狀態、審查與必要檢查，有變化時提醒 | 讀寫檔案, 執行指令 |

### 等待時的消遣

| Mod | 功能 | 權限 |
| --- | --- | --- |
| [`tw-stock-mod`](https://github.com/darrell-tw/darrelltw-mods/tree/649efd272da992051c48d25f30a393e0e0ce45b8/mods/tw-stock-mod)<br><sub>作者 darrell-tw</sub> | 台股／美股自選股看板，依交易時段切換，含持股損益模式 | 讀寫檔案, 連網, 執行指令 |
| [`mindful-claude`](https://github.com/halluton/Mindful-Claude/tree/411c9c4f4f1c3d128159be7315823341ae7d9e2d)<br><sub>作者 halluton</sub> | Claude 工作時在輸入框上方帶你做呼吸練習，spinner 跟著呼吸計數 | — |
| [`now-playing`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/now-playing)<br><sub>作者 hamzafer</sub> | 一行顯示 Spotify 正在播放的歌曲、進度與當前歌詞，附控制按鈕（僅 macOS） | 連網, 執行指令 |
| [`prayer-times`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/prayer-times)<br><sub>作者 hamzafer</sub> | 目前與下一次禮拜時間及剩餘時間，在本機依位置計算，不連網 | — |
| [`reels`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/reels)<br><sub>作者 hamzafer</sub> | 在終端機面板播放 YouTube Shorts，Claude 工作時播放、完成時暫停 | 讀寫檔案, 連網, 執行指令 |
| [`snake`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/snake)<br><sub>作者 hamzafer</sub> | Claude 工作時在面板裡玩貪食蛇，需先 /snake 開啟 | — |
| [`cc-arcade`](https://github.com/sezaakgun/cc-arcade/tree/0baff06d31295850283c2eebe052f39bbc35473f)<br><sub>作者 sezaakgun</sub> | 輸入框上方 9 款小遊戲（貪食蛇、俄羅斯方塊、2048 等），外加隨測試與提交成長的寵物 | — |

## 推薦 mod

開一個 issue，附上 mod 儲存庫的連結。也可以自己新增：在 `community.json` 加一筆（儲存庫、目錄、審核過的 commit、分類、授權），在 `readme/summaries.json` 寫上各語言的一句話簡介，執行 `python3 scripts/build-catalog.py`，再送出 pull request。

## 致謝

每個 mod 歸其作者所有，沿用各自的授權；本儲存庫只負責收錄。其中許多是透過 [awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods) 發現的。作者如需修改或下架收錄資訊，請開 issue。

非官方專案，與 Anthropic 無關。
