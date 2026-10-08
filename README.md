# Best Claude Code Mods

**English** · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

**Hand-picked, validated, pinned. One add, 43 mods.**

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

### Dashboards and usage

| Mod | What it does | Reaches |
| --- | --- | --- |
| [`cache-clock`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/cache-clock)<br><sub>by hamzafer</sub> | A prompt-cache line under your status line: minutes left while warm, and how many tokens the next message re-caches once cold. /cache-clock setup adds it. | files, runs commands |
| [`context-bar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/context-bar)<br><sub>by hamzafer</sub> | Your context window as a stacked bar above the prompt, a color per category, with token counts and the compaction point. /context-bar shows or hides it. | — |
| [`openai-balance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/openai-balance)<br><sub>by hamzafer</sub> | Your OpenAI API credit above the prompt: an estimated balance with a gauge, today's spend, where the money mostly went, and the last call. /openai-balance shows the breakdown. | network, runs commands |
| [`token-weather`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/token-weather)<br><sub>by hamzafer</sub> | A live forecast of the context window, with a prompt-cache countdown, drawn above the prompt. | files, runs commands |
| [`usage-meter`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/usage-meter)<br><sub>by hamzafer</sub> | Your plan's 5-hour and 7-day usage as small bars above the prompt, with the reset countdown and the session's cost. | — |
| [`usage-band`](https://github.com/JetsonChan/CC-Usage-Band/tree/60cd60949b1f52c96ddba3ea24ed0848ff302196/usage-band)<br><sub>by JetsonChan</sub> | A band above the prompt showing your 5-hour and 7-day limits, context window and prompt-cache hit rate, styled for the terminal and the desktop app | — |
| [`context-view`](https://github.com/kongyo2/context-view/tree/137e4e3db754684144ec953c5e66085bc2959766)<br><sub>by kongyo2</sub> | The context window as one row above the prompt, drawn the way Claude Code draws its own meters: the context's cells, the percentage used, the tokens over the window, and the tokens left before auto-compact. /context-view hides and shows it. | — |
| [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/f31daca523d36c501cd0df23a737a44c7dc56ad6)<br><sub>by scasella</sub> | Flightdeck: a live agent dashboard for Claude Code. Main model vitals, an on-call architect, every permission check, subagent cards and swimlanes, a turn receipt and a session log, all from real session events | — |
| [`cctop`](https://github.com/tomstagl/cctop/tree/6ceafc34a972f4e58d5e53b1c69f80e2a9759d41/plugin)<br><sub>by tomstagl</sub> | btop-style live dashboard for Claude Code internals: /cctop opens it in a side pane, cctop-insights lets the session answer questions from its numbers | files, runs commands |
| [`statuspane`](https://github.com/xuanji86/claude-statuspane/tree/13bd8e46edefdf282f117941b886cb529c7d79c3)<br><sub>by xuanji86</sub> | A floating status card above the Claude Code prompt — model, effort, context, 5h/week limits, cost, directory and branch, GitHub CI and deploys — with clickable settings and a progress-row API any script or mod can feed. | files, runs commands |
| [`plan-progress`](https://github.com/zycck/claude-mods/tree/3539d02d7435397d293e3120ebad22c23214f6c0/plugins/plan-progress)<br><sub>by zycck</sub> | Live plan progress bars above the Claude Code prompt: stages, steps, a pixel fill and soft sounds for decision, error and done | files, runs commands |

### Agents and subagents

| Mod | What it does | Reaches |
| --- | --- | --- |
| [`agent-flow`](https://github.com/Charlie0113-T/claude-agent-flow/tree/d87b2559dec03979e088026e8f48aee5f9d2cab5)<br><sub>by Charlie0113-T</sub> | The agent flow pane: /flow opens a live tree of the session's subagents and teammates beside the transcript, fed by engine events, with a text fallback where no pane can be drawn. | — |
| [`agent-radar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/agent-radar)<br><sub>by hamzafer</sub> | One live line above the prompt per running subagent: time, tool count and what it's doing. /radar shows every agent and its messages. | — |
| [`browser-lanes`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/browser-lanes)<br><sub>by hamzafer</sub> | Shows if this session has a Playwright browser and who holds it. /browser clean closes leftover browsers. A subagent that wants the browser waits until the one using it is done. | runs commands |
| [`mission-control`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/mission-control)<br><sub>by hamzafer</sub> | /mission opens a live map of the main agent, its subagents and every tool call, plus a code map of the files they touch. | files, model calls, runs commands |
| [`review-watch`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/review-watch)<br><sub>by hamzafer</sub> | A live line above the prompt for each running code review: Codex or a review subagent, its model, what it reviews, time, and Codex's latest output. A toast with the findings when it ends. | runs commands |
| [`switchboard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/switchboard)<br><sub>by hamzafer</sub> | Picks the model for each subagent that names none, with OpenAI's Decisions API or Jev, from its short label only. One line per spawn above the prompt; /route shows each pick and what each subagent cost. | network |
| [`agentpane`](https://github.com/xuanji86/claude-agentpane/tree/17be88979e5782591a2a184959df1c4168600066)<br><sub>by xuanji86</sub> | A side pane for Claude Code that lists the subagents a session runs, what each is doing and what it costs in tokens, with each one's conversation a click away. | — |

### Productivity and context

| Mod | What it does | Reaches |
| --- | --- | --- |
| [`glance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/glance)<br><sub>by hamzafer</sub> | One line above the prompt with what needs you: next meeting, PRs, Linear issues and Slack DMs. /glance lists them all. | MCP, runs commands |
| [`next-steps`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/next-steps)<br><sub>by hamzafer</sub> | After each turn, 2 or 3 likely next prompts above the prompt. Press 1, 2 or 3 in an empty prompt to draft one, 0 to dismiss. | model calls |
| [`session-saver`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/session-saver)<br><sub>by hamzafer</sub> | Names untitled sessions through unpause. /park saves where you left off, and a resumed session shows it. | model calls, runs commands |
| [`where-am-i`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/where-am-i)<br><sub>by hamzafer</sub> | A live recap above the prompt: goal, doing now, waiting on you, next. /where for a longer one. | model calls |
| [`aside`](https://github.com/JayDoubleu/aside/tree/cf2b7562ae7b376cdcf9e2436a926aba77dc759f)<br><sub>by JayDoubleu</sub> | Read-only side chat: /aside opens a pane beside the transcript where you ask about the session so far; answers come from a tool-less fork of the session's own transcript and nothing is written back into the main thread. | model calls |
| [`lcm`](https://github.com/lossless-claude/lcm/tree/0c17dbffda452cf7fae46929af427dff355aeaa3)<br><sub>by lossless-claude</sub> | Lossless context management — DAG-based summarization that preserves every message | files, network, model calls, runs commands |

### Rendering and previews

| Mod | What it does | Reaches |
| --- | --- | --- |
| [`gfm-render`](https://github.com/briangtn/claude-gfm-render/tree/a209ad5a0ec35c0813d2d80ab62b596140b0c807)<br><sub>by briangtn</sub> | GitHub Flavored Markdown in the transcript: alerts (> [!NOTE]), task lists, strikethrough and Mermaid diagrams | runs commands |
| [`md-preview`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/md-preview)<br><sub>by hamzafer</sub> | Shows the Markdown files Claude edits, rendered like GitHub, in a pane next to the chat. Before and after side by side. /md opens it. | files, runs commands |
| [`replay-theater`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/replay-theater)<br><sub>by hamzafer</sub> | Step through the last turn's file edits, one diff at a time. | files |
| [`skins`](https://github.com/hellosverre/claude-skins/tree/342fbc0dd49ec44c824ed9c8eb95cd4927d7f81a)<br><sub>by hellosverre</sub> | Skins for Claude Code's transcript: themed tool rows, reply gutters and spinner words. /skin swaps them live. | — |
| [`mdview`](https://github.com/xuanji86/claude-mdview/tree/da646556714507acf5d41610605b9911eb9aa42a)<br><sub>by xuanji86</sub> | Click a .md path in the Claude Code conversation to read it rendered as markdown beside the session, pictures included, and point at any block to have Claude edit it. | files, runs commands |
| [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/2165ae76c9639e3996829ab0e6d54ddbd4f06ad8/claude-code-plugin)<br><sub>by zenbu-labs</sub> | A browser running directly inside claude code. Preview websites, view HTML documents, and let your agent control the built in browser. | files, network, runs commands |

### Safety and guards

| Mod | What it does | Reaches |
| --- | --- | --- |
| [`blast-radius`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/blast-radius)<br><sub>by hamzafer</sub> | Holds risky Bash commands and shows what they would change before they run. | runs commands |
| [`merge-gate`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/merge-gate)<br><sub>by hamzafer</sub> | Holds `gh pr merge` until CI passes and one Codex review (OpenAI's luna model) has run. A PR line above the prompt, and /gate shows the PR's status. | files, runs commands |
| [`rulebook-guard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/rulebook-guard)<br><sub>by hamzafer</sub> | Writing and git rules: replaces em dashes in prose, and asks before git commit --amend, an unformatted push, or personal info in notes and commits. | files, runs commands |
| [`secret-redactor`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/secret-redactor)<br><sub>by ray-amjad</sub> | Keeps secrets, email addresses and IP addresses out of the session transcript: swaps each one for a stable placeholder on the way in, and puts the real value back on the way into a tool call | — |

### Git, PRs and deploys

| Mod | What it does | Reaches |
| --- | --- | --- |
| [`vercel-deploy-status`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/vercel-deploy-status)<br><sub>by ray-amjad</sub> | Pins the Vercel deploy queue of the linked project under the prompt: every deploy queued, building or just finished, with its phase and elapsed time | files, runs commands |
| [`cc-pr-tracker`](https://github.com/sezaakgun/cc-pr-tracker/tree/2d96fc7ed6bcca44a350700ac4c37e9066d58b46)<br><sub>by sezaakgun</sub> | Watch GitHub PRs from a Claude Code session: merge state, review and required checks above the prompt, with alerts when they change | files, runs commands |

### While you wait

| Mod | What it does | Reaches |
| --- | --- | --- |
| [`tw-stock-mod`](https://github.com/darrell-tw/darrelltw-mods/tree/649efd272da992051c48d25f30a393e0e0ce45b8/mods/tw-stock-mod)<br><sub>by darrell-tw</sub> | Taiwan and US stock watchlist above the prompt, switching with market hours, in a broker-style table, plus a profit-and-loss view of your holdings | files, network, runs commands |
| [`mindful-claude`](https://github.com/halluton/Mindful-Claude/tree/411c9c4f4f1c3d128159be7315823341ae7d9e2d)<br><sub>by halluton</sub> | Guided breathing exercises above the prompt while Claude works: coherent, box, 4-7-8 and the physiological sigh, four animation styles, and the spinner reads the breath. Appears when Claude starts, disappears when Claude answers. Needs function hooks (early access) and an interactive terminal. | — |
| [`now-playing`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/now-playing)<br><sub>by hamzafer</sub> | What Spotify is playing, one line above the prompt: track, progress and the lyric being sung, with ⏮ ⏸ ⏭ buttons. /music controls it too. macOS. | network, runs commands |
| [`prayer-times`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/prayer-times)<br><sub>by hamzafer</sub> | The current prayer and how long is left, the next prayer, and zawal, above the prompt. Computed on your computer from your location; nothing is sent anywhere. | — |
| [`reels`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/reels)<br><sub>by hamzafer</sub> | YouTube Shorts in a terminal pane: plays while Claude works, pauses when Claude is done. | files, network, runs commands |
| [`snake`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/snake)<br><sub>by hamzafer</sub> | Snake in a pane while Claude works, paused when it's done. Opt-in, so nothing opens until /snake. | — |
| [`cc-arcade`](https://github.com/sezaakgun/cc-arcade/tree/0baff06d31295850283c2eebe052f39bbc35473f)<br><sub>by sezaakgun</sub> | Games above the Claude Code prompt (snake, Tetris, 2048, Minesweeper, Flappy, Pong, typing test, Space Invaders, Doom) plus a pet that grows as Claude tests, commits and edits. Clones of the genre, not affiliated with or endorsed by Tetris Holding, Taito, Atari or id Software. Needs function hooks (early access) and an interactive terminal. | — |

## Suggest a mod

Open an issue with the link to the mod's repository. To add one yourself, add an entry to `community.json` (repository, folder, reviewed commit, category, license), add its one-line summaries to `readme/summaries.json`, run `python3 scripts/build-catalog.py`, and open a pull request.

## Credits

Every mod belongs to its author and keeps its own license; this repository only lists them. Many were found through [awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods). Authors who want a listing changed or removed can open an issue.

Unofficial; not an Anthropic product.
