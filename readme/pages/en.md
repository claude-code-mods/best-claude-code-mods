# Best Claude Code Mods

{{languages}}

**Hand-picked, validated, pinned. One add, {{count}} mods.**

Mods are Claude Code plugins made of function hooks: they watch, change or answer what Claude Code does, and draw their own UI. This marketplace collects the best community mods. Each one is checked with `claude plugin validate` and pinned to the commit we checked, so later changes by its author never reach you unreviewed.

Needs Claude Code 2.1.287 or later.

## Install

In a Claude Code terminal session:

```
/plugin marketplace add claude-code-mods/best-claude-code-mods
/plugin install <mod>@best-claude-code-mods
```

For example `/plugin install terminal-browser@best-claude-code-mods`. Run `/plugin marketplace update best-claude-code-mods` to get new mods and updates.

## Catalogue

**Reaches** lists what the validator reports a mod's code can do beyond drawing UI. Read a mod's source before installing it: validation reads the code without running it, and is not a security audit.

{{catalog}}

## Suggest a mod

Open an issue with the link to the mod's repository. To add one yourself, add an entry to `community.json` (repository, folder, reviewed commit, category, license), add its one-line summaries to `readme/summaries.json`, run `python3 scripts/build-catalog.py`, and open a pull request.

## Credits

Every mod belongs to its author and keeps its own license; this repository only lists them. Many were found through [awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods). Authors who want a listing changed or removed can open an issue.

Unofficial; not an Anthropic product.
