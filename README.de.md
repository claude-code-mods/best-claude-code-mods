# Best Claude Code Mods

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · **Deutsch** · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

**Handverlesen, geprüft, festgepinnt. Einmal hinzufügen, 41 Mods.**

Mods sind Claude-Code-Plugins aus Funktions-Hooks: Sie beobachten, ändern oder übernehmen, was Claude Code tut, und zeichnen ihre eigene Oberfläche. Dieser Marketplace sammelt die besten Mods der Community. Jeder ist mit `claude plugin validate` geprüft und auf den geprüften Commit festgelegt, sodass spätere Änderungen des Autors dich nie ungeprüft erreichen.

Erfordert Claude Code 2.1.287 oder neuer.

## Installation

In einer Claude-Code-Sitzung im Terminal:

```
/plugin marketplace add claude-code-mods/best-claude-code-mods
/plugin install <mod>@best-claude-code-mods
```

Zum Beispiel `/plugin install terminal-browser@best-claude-code-mods`. Mit `/plugin marketplace update best-claude-code-mods` holst du neue Mods und Updates.

## Katalog

Die Spalte **Zugriff** zeigt, was der Code eines Mods laut Validator über das Zeichnen der Oberfläche hinaus tun kann. Lies den Quellcode eines Mods, bevor du ihn installierst: Die Prüfung liest den Code, ohne ihn auszuführen, und ist kein Sicherheitsaudit.

### Dashboards und Verbrauch

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Was er tut | Zugriff |
| --- | --- | --- |
| [`token-optimizer`](https://github.com/alexgreensh/token-optimizer/tree/e3f1a2dcad8d8999096b8a881c4d98cdba4ef1a5/desktop/token-optimizer-desktop)<br><sub>von alexgreensh</sub> | A token-optimizer status bar that shows where tokens go and how to spend less. | führt Befehle aus, ruft Modelle auf, Dateien |
| [`claude-council`](https://github.com/hex/claude-council/tree/f2f7f42122b288599cef8cea97dcc490acea98a5)<br><sub>von hex</sub> | Consult several AI agents at once for diverse perspectives, with a streaming pane and an optional heads-up side check. | führt Befehle aus, ruft Modelle auf, Dateien |
| [`codex-attachment-manager`](https://github.com/chipfighter/context-attachment-manager/tree/d68a721b7432059c9056d546ff2a26b11b3c0e0c)<br><sub>von chipfighter</sub> | Sends earlier images as short placeholders and fetches originals back by ID, so long image sessions keep the prompt cache. | Netzwerk, MCP |
| [`cache-tax`](https://github.com/karanb192/cache-tax/tree/535ff33225e666e605e731d78f5ac5efe243c7c3)<br><sub>von karanb192</sub> | Keeps the one-hour prompt cache warm during breaks, asking before a cold send and showing the rewrite cost. | ruft Modelle auf |
| [`agent-standup-band`](https://github.com/Atoll92/agent-standup/tree/846d5324f7c00f06d598c86e87ed8b51d774b3ac/plugin-band)<br><sub>von Atoll92</sub> | A line above the prompt when another local session needs you, and a toast when one finishes. | führt Befehle aus, Dateien |
| [`shunt`](https://github.com/pleaseai/shunt/tree/57182b328e92d3c70bc9ca5a1fd1ee9104cfbabb/plugins/shunt)<br><sub>von pleaseai</sub> | A usage band for the shunt gateway: each window's spend and reset time, plus a full /shunt:usage breakdown. | Netzwerk, führt Befehle aus |
| [`tokendoctor`](https://github.com/localixai/tokendoctor/tree/051fa9598f0a50ed30974b618f2911381b7dcf90)<br><sub>von localixai</sub> | Replays your past sessions to show what each change would have saved, then applies only what you pick. | führt Befehle aus, ruft Modelle auf |
| [`skins`](https://github.com/hellosverre/claude-skins/tree/cf0d39f3785d5c5a4b6189ecc487b1ac479efea0)<br><sub>von hellosverre</sub> | Skins and fifteen themes for the transcript, with rich cards and a usage band; /skin swaps them live. | Netzwerk, führt Befehle aus, ruft Modelle auf, Dateien |
| [`ctx-handoff`](https://github.com/cablate/ctx-handoff-mod/tree/a416713a0495be799a31f3650e18458e242270c7)<br><sub>von cablate</sub> | Turns what you teach Claude into project notes, catches common slips, keeps the cache warm and resumes long sessions. | ruft Modelle auf, Dateien |
| [`great-cto`](https://github.com/avelikiy/great_cto/tree/12dfd86e99627cd6dd1ed394de4786f4ba08499b)<br><sub>von avelikiy</sub> | Runs Claude Code as a pipeline of 73 specialist agents, with an independent model checking each stage. | Netzwerk |
| [`ripple`](https://github.com/PBJ-2/clauderipple/tree/c1c6b76a9e4e7a51df2ec5907d6e41d6bf8591e3/packages/mod)<br><sub>von PBJ-2</sub> | Picks reasoning effort per prompt and a worker per delegated task, keeps the cache warm and shows where each request went. | Netzwerk, führt Befehle aus, ruft Modelle auf, MCP, Dateien |
| [`tavernweave-agent-skills`](https://github.com/LiarMTTT/TavernWeave/tree/f9863d2b05305457fe9ed8b0c5688d52aca400a5)<br><sub>von LiarMTTT</sub> | 23 shared skills for rolecards, software work and bounded cloud tasks, plus a Soul mode switch above the prompt. | — |
| [`agent-usage-guard`](https://github.com/rbartoli/agent-usage-guard/tree/02594c2620be9eb60c32e2f77d9d512d9f61b205)<br><sub>von rbartoli</sub> | Holds subagent fan-out, heavy-context prompts and retry loops before they spend your usage window. | ruft Modelle auf, Dateien |

### Agenten und Subagenten

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Was er tut | Zugriff |
| --- | --- | --- |
| [`shared-session`](https://github.com/Paradigm-Study/claude-share/tree/9d88f996ac4245c756a89b34e98cfde375028950/plugin)<br><sub>von Paradigm-Study</sub> | Share a session with a link or your team; teammates join from their own Claude Code and watch every turn live. | — |
| [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/626cc0b46d417f81bbff9f5ba3b49abaf8912a85)<br><sub>von scasella</sub> | A live agent dashboard: model vitals, an on-call architect, permission checks, subagent cards and a session log. | — |
| [`start`](https://github.com/rsmdt/the-startup/tree/e803d51fdb423271d3dde189f5416f3ec51386a9/plugins/start)<br><sub>von rsmdt</sub> | Workflow orchestration commands for agentic software development. | Dateien |
| [`lane-stack`](https://github.com/VKirill/claude-lane-stack/tree/8bac2b876b72053aa445bb9d1c7c6079bfc4ba8c/plugins/lane-stack)<br><sub>von VKirill</sub> | A solo PM conveyor: orchestrator agents, lane playbooks, onboard and resume commands. | Netzwerk, ruft Modelle auf |

### Produktivität und Kontext

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Was er tut | Zugriff |
| --- | --- | --- |
| [`pebrel-prompt-suggestions`](https://github.com/Kuddev/pebrel/tree/ed9b2331340877ba3d775e38c4df6bd1a2abb1fe/pebrel_app/res/prompt-suggestions/claude)<br><sub>von Kuddev</sub> | Native empty-composer prompt predictions through the Pebrel session bridge. | Netzwerk |
| [`fast-jev-compaction`](https://github.com/tamaratran/fast-jev-compaction/tree/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0)<br><sub>von tamaratran</sub> | Verbatim Jev-guided compaction for Claude Code sessions. | Netzwerk, ruft Modelle auf |
| [`lot-map`](https://github.com/alexeyw/lot-map/tree/ad60f057902765d778eedde770d337be45fac3af)<br><sub>von alexeyw</sub> | A live map beside the chat: memory, files, shell, web, model, agents, skills and hooks light up as they are used. | — |
| [`storybloq`](https://github.com/Storybloq/storybloq/tree/f0b4c08e3a15ffb9841e5a3058c6b1ca57607154/plugins/storybloq)<br><sub>von Storybloq</sub> | Project memory: tickets, issues, handovers and lessons kept in a .story/ folder in your repo. | Dateien |
| [`just-do-it`](https://github.com/Lifecycle-Innovations-Limited/claude-ops/tree/e434ef7e612f2ff5769def6101fc9d984888d377/claude-ops/skills/ops-jdi/plugin)<br><sub>von Lifecycle-Innovations-Limited</sub> | Continues authorized work through verification and delivery, and surfaces setup issues to repair. | führt Befehle aus, ruft Modelle auf |
| [`filetree`](https://github.com/data-goblin/claude-code-filetree/tree/1fdc3a963f2dc22a939f661ff0ff5a76646c9112)<br><sub>von data-goblin</sub> | An IDE-style file tree that shows what Claude is doing and where in your files. | führt Befehle aus, ruft Modelle auf, Dateien |
| [`jev-auto-compact`](https://github.com/notque/vexjoy-agent/tree/c68ac1fea2a03e437ccc95112d1e56e467a9bd00/plugins/jev-auto-compact)<br><sub>von notque</sub> | At 60% context, prunes stale tool calls with zero generation; skips instead of falling back to an LLM summary. | Netzwerk, ruft Modelle auf |
| [`caliber-jev-compaction`](https://github.com/caliber-ai-org/ai-setup/tree/f5dbc002022a8a10acad25c1cce23ddefdc19d0d/plugin/caliber-jev-compaction)<br><sub>von caliber-ai-org</sub> | Verbatim Jev-guided compaction for Claude Code sessions. | Netzwerk, ruft Modelle auf |
| [`operator`](https://github.com/aerovato/operator-memory/tree/93c3fce64f0a72adeb89fa868600eb418548ec07/packages/claude-code)<br><sub>von aerovato</sub> | Durable project and user memory for agent-driven development. | — |
| [`claude-carbon`](https://github.com/gwittebolle/claude-carbon/tree/9ad53f1dd07fb0e11fcdb94d294ed794d660cf4b)<br><sub>von gwittebolle</sub> | Tracks the carbon footprint of your Claude Code sessions in the terminal and desktop app. | Dateien |
| [`work-mode`](https://github.com/danyuchn/claude-work-mode/tree/e19eda1e8465308bd79a74fad295cf9b6d9cdf71/plugins/work-mode)<br><sub>von danyuchn</sub> | Session modes: auto (no mid-task questions), out (delegate batch work) and wrap (converge and finish). | führt Befehle aus, Dateien |
| [`show-your-work`](https://github.com/iamumeransari/claude-show-your-work/tree/71e546044e3ba61b98a6938a03270da791f9ca2e)<br><sub>von iamumeransari</sub> | Shows finished work in the terminal: screenshots, click-through videos and synced before/after QA. | Netzwerk, führt Befehle aus, ruft Modelle auf, Dateien |
| [`inbox`](https://github.com/petekp/inbox/tree/02e441cd447edf86fc30fbd03e9117a8ead9da7a)<br><sub>von petekp</sub> | Gathers the questions, tasks, findings and PRs waiting on you in a session. | — |
| [`compact-adviser`](https://github.com/kunchenguid/compact-adviser/tree/37fa1a665b8933de68c90014312060e862cf121a/packages/claude-mod)<br><sub>von kunchenguid</sub> | Suggests or runs /compact at a completed checkpoint, judged by TypeSafe Jev. | Netzwerk, ruft Modelle auf, Dateien |

### Darstellung und Vorschau

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Was er tut | Zugriff |
| --- | --- | --- |
| [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/fa9e5eb053d2a1da11f7ccba720a0d3d389c05a6/claude-code-plugin)<br><sub>von zenbu-labs</sub> | A browser inside Claude Code: preview sites and HTML, and let the agent drive the built-in browser. | Netzwerk, führt Befehle aus, ruft Modelle auf, Dateien |
| [`prismantis`](https://github.com/NahumLitvin/prismantis/tree/3718a40abc57b836108a65bd9f01d06d3237e52d/plugin)<br><sub>von NahumLitvin</sub> | Colorful, themeable rendering for replies: tables, headings, code, numbers, paths and links. | führt Befehle aus, Dateien |

### Sicherheit und Schutz

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Was er tut | Zugriff |
| --- | --- | --- |
| [`lcu-approve`](https://github.com/amontlabs/lcu/tree/1bd45b304295c7665b559fcc32f7b3a8f1b1d859/adapters/claude-mod/lcu-approve)<br><sub>von amontlabs</sub> | Per-app approval for computer use: allow this conversation, always allow, or deny, plus a panel of approved apps. | führt Befehle aus, MCP, Dateien |
| [`agentctl`](https://github.com/sd0xdev/sd0x-harness/tree/b0206637edd2e44c993da12b6b30858f96bc3cdc/mods/agentctl)<br><sub>von sd0xdev</sub> | An agent control plane for a session: task scope, evidence and hand-over. | führt Befehle aus, ruft Modelle auf, Dateien |
| [`multi-core`](https://github.com/greenpolo/cc-multi-cli-plugin/tree/66d9b0a6b06b25fd648ecd53311a647bb57e2fb4/plugins/multi-core)<br><sub>von greenpolo</sub> | Use ChatGPT, Cursor, OpenCode and Antigravity models inside one session, switching with /model. | Netzwerk, ruft Modelle auf |
| [`jevmem-pane`](https://github.com/Avinash-jetwani/jevmem/tree/c29753ccb2c9706e417fda25efa422682358955b/pane)<br><sub>von Avinash-jetwani</sub> | A side pane showing what jevmem recalled, what its guard decided and what the last turn saved. | führt Befehle aus, Dateien |

### Git, PRs und Deployments

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Was er tut | Zugriff |
| --- | --- | --- |
| [`fm`](https://github.com/kunchenguid/firstmate/tree/427056c4181c41074ad24f051f79919330df0fa5/.claude/mods/firstmate-calm)<br><sub>von kunchenguid</sub> | The sailboat working animation and a conversation-only transcript, sharing a calm-mode preference across sessions. | Dateien |
| [`turbo`](https://github.com/tobihagemann/turbo/tree/3bc6b4436d96be22497109e16e68fe4dfa323531/claude)<br><sub>von tobihagemann</sub> | A human-gated agentic software factory: you decide what to build and judge the result, skills build and ship it. | ruft Modelle auf, Dateien |
| [`mazyos`](https://github.com/Mazzeo-Marketing/MazyOS/tree/d2b65b392f1ee230afb088d155fc734def5f105d)<br><sub>von Mazzeo-Marketing</sub> | A Portuguese business OS plugin: your company memory in every session, brand identity on outputs, and 17 marketing/SEO skills. | Dateien |
| [`engineer`](https://github.com/swingerman/engineer/tree/ae4cb5fe32007dd6a3d717c9998dcfb12b1f348e/engineer)<br><sub>von swingerman</sub> | A disciplined agentic-engineering methodology kit: intake, AC discovery, spec, planning, implementation, verification, hardening. | führt Befehle aus, ruft Modelle auf |

## Einen Mod vorschlagen

Öffne ein Issue mit dem Link zum Repository des Mods. Um ihn selbst hinzuzufügen, ergänze einen Eintrag in `community.json` (Repository, Ordner, geprüfter Commit, Kategorie, Lizenz), schreibe seine Einzeiler in `readme/summaries.json`, führe `python3 scripts/build-catalog.py` aus und öffne einen Pull Request.

## Danksagung

Jeder Mod gehört seinem Autor und behält seine eigene Lizenz; dieses Repository listet sie nur auf. Autoren, die einen Eintrag ändern oder entfernen lassen möchten, können ein Issue öffnen.

Inoffiziell; kein Produkt von Anthropic.
