# Best Claude Code Mods · 精选 Claude Code 模组

{{languages}}

**逐个挑选、校验、固定版本。添加一次，{{count}} 个 mod 随装随用。**

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

{{catalog}}

## 推荐 mod

开一个 issue，附上 mod 仓库的链接。也可以自己添加：在 `community.json` 里加一条（仓库、目录、审核过的 commit、分类、许可证），在 `readme/summaries.json` 里写上各语言的一句话简介，运行 `python3 scripts/build-catalog.py`，然后提交 pull request。

## 致谢

每个 mod 归其作者所有，沿用各自的许可证；本仓库只做收录。作者如需修改或下架收录信息，请开 issue。

非官方项目，与 Anthropic 无关。
