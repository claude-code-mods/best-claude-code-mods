# Best Claude Code Mods · 精選 Claude Code 模組

{{languages}}

**逐一挑選、驗證、固定版本。新增一次，{{count}} 個 mod 隨裝隨用。**

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

{{catalog}}

## 推薦 mod

開一個 issue，附上 mod 儲存庫的連結。也可以自己新增：在 `community.json` 加一筆（儲存庫、目錄、審核過的 commit、分類、授權），在 `readme/summaries.json` 寫上各語言的一句話簡介，執行 `python3 scripts/build-catalog.py`，再送出 pull request。

## 致謝

每個 mod 歸其作者所有，沿用各自的授權；本儲存庫只負責收錄。作者如需修改或下架收錄資訊，請開 issue。

非官方專案，與 Anthropic 無關。
