# claude-code-mods — a Claude Code mods marketplace

A Claude Code plugin marketplace of **mods**: plugins made of function hooks
that watch, rewrite or answer what Claude Code does, and draw their own UI.
Needs a Claude Code version with mods support (2.1.287 or later).

[中文说明](#中文说明)

| Mod | What it does |
| --- | --- |
| [`env-guard`](env-guard) | Refuses `Read` / `Edit` / `Write` on `.env` files (`.env`, `.env.local`, `.env.production`, …). |
| [`turn-band`](turn-band) | A row above the prompt with the last turn's time and number of tool calls, plus a **Hide** button. |
| [`template`](template) | A starter mod (not listed in the marketplace): one slash command and its test. |

## Install

In a Claude Code terminal session:

```
/plugin marketplace add claude-code-mods/marketplace
/plugin install env-guard@claude-code-mods
/plugin install turn-band@claude-code-mods
```

Or install a mod in one line; answer `y` to add the marketplace, then pick a scope:

```
/plugin install env-guard --marketplace claude-code-mods/marketplace
```

Update later with `/plugin marketplace update claude-code-mods`.

## Write a mod

```bash
scripts/new-mod.sh my-mod "One line about what it does"
claude --plugin-dir "$PWD/my-mod"     # reloads on every save
```

A mod is a folder:

```
my-mod/
├── .claude-plugin/plugin.json   name, version, description (+ "types" if it keeps state)
├── hooks/hooks.json             { "modules": ["./register.ts"] }
├── hooks/register.ts(x)         export const register: Register = on => { ... }
├── types/index.d.ts             optional: the $.state contract
└── tests/my-mod.test.ts         run with: claude plugin test my-mod
```

Every hook is `($, e, next)`: call `next(e)` to pass the event on, `next({ ...e, x })`
to rewrite it, or return without calling `next` to answer it yourself. Keep values
in `$.state`; module variables reset on every reload.

## Check before you push

```bash
scripts/check.sh    # claude plugin validate + claude plugin test for every mod
```

---

## 中文说明

这是一个 Claude Code 插件市场，里面的插件是 **mods**：用函数钩子写成，能观察、
改写或接管 Claude Code 的行为，也能画自己的界面。需要支持 mods 的 Claude Code（2.1.287 及以上）。

安装（在 Claude Code 终端会话里输入）：

```
/plugin marketplace add claude-code-mods/marketplace
/plugin install env-guard@claude-code-mods
/plugin install turn-band@claude-code-mods
```

写一个新 mod：运行 `scripts/new-mod.sh my-mod "一句话说明"`，它会复制 `template/`
并把新 mod 登记到 `.claude-plugin/marketplace.json`；提交前运行 `scripts/check.sh`。

Unofficial; not an Anthropic product. MIT licensed.
