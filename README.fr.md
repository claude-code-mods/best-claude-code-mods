# Best Claude Code Mods

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · **Français** · [Deutsch](README.de.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

**Choisis à la main, validés, épinglés. Un seul ajout, 41 mods.**

Les mods sont des plugins Claude Code faits de hooks de fonctions : ils observent, modifient ou prennent en charge ce que fait Claude Code, et dessinent leur propre interface. Ce marketplace rassemble les meilleurs mods de la communauté. Chacun est vérifié avec `claude plugin validate` et épinglé au commit vérifié : les modifications ultérieures de son auteur ne vous parviennent jamais sans relecture.

Nécessite Claude Code 2.1.287 ou plus récent.

## Installation

Dans une session Claude Code au terminal :

```
/plugin marketplace add claude-code-mods/best-claude-code-mods
/plugin install <mod>@best-claude-code-mods
```

Par exemple `/plugin install terminal-browser@best-claude-code-mods`. Lancez `/plugin marketplace update best-claude-code-mods` pour recevoir les nouveaux mods et les mises à jour.

## Catalogue

La colonne **Accès** indique ce que, selon le validateur, le code du mod peut faire en plus de dessiner son interface. Lisez le code d'un mod avant de l'installer : la validation le lit sans l'exécuter et ne constitue pas un audit de sécurité.

### Tableaux de bord et usage

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Ce qu'il fait | Accès |
| --- | --- | --- |
| [`token-optimizer`](https://github.com/alexgreensh/token-optimizer/tree/e3f1a2dcad8d8999096b8a881c4d98cdba4ef1a5/desktop/token-optimizer-desktop)<br><sub>par alexgreensh · [🖼 preview](https://github.com/alexgreensh/token-optimizer)</sub> | A token-optimizer status bar that shows where tokens go and how to spend less. | lance des commandes, appelle un modèle, fichiers |
| [`claude-council`](https://github.com/hex/claude-council/tree/f2f7f42122b288599cef8cea97dcc490acea98a5)<br><sub>par hex · [🖼 preview](https://github.com/hex/claude-council)</sub> | Consult several AI agents at once for diverse perspectives, with a streaming pane and an optional heads-up side check. | lance des commandes, appelle un modèle, fichiers |
| [`codex-attachment-manager`](https://github.com/chipfighter/context-attachment-manager/tree/d68a721b7432059c9056d546ff2a26b11b3c0e0c)<br><sub>par chipfighter · [🖼 preview](https://github.com/chipfighter/context-attachment-manager)</sub> | Sends earlier images as short placeholders and fetches originals back by ID, so long image sessions keep the prompt cache. | réseau, MCP |
| [`cache-tax`](https://github.com/karanb192/cache-tax/tree/535ff33225e666e605e731d78f5ac5efe243c7c3)<br><sub>par karanb192 · [🖼 preview](https://github.com/karanb192/cache-tax)</sub> | Keeps the one-hour prompt cache warm during breaks, asking before a cold send and showing the rewrite cost. | appelle un modèle |
| [`agent-standup-band`](https://github.com/Atoll92/agent-standup/tree/846d5324f7c00f06d598c86e87ed8b51d774b3ac/plugin-band)<br><sub>par Atoll92 · [🖼 preview](https://github.com/Atoll92/agent-standup)</sub> | A line above the prompt when another local session needs you, and a toast when one finishes. | lance des commandes, fichiers |
| [`shunt`](https://github.com/pleaseai/shunt/tree/57182b328e92d3c70bc9ca5a1fd1ee9104cfbabb/plugins/shunt)<br><sub>par pleaseai · [🖼 preview](https://github.com/pleaseai/shunt)</sub> | A usage band for the shunt gateway: each window's spend and reset time, plus a full /shunt:usage breakdown. | réseau, lance des commandes |
| [`tokendoctor`](https://github.com/localixai/tokendoctor/tree/051fa9598f0a50ed30974b618f2911381b7dcf90)<br><sub>par localixai · [🖼 preview](https://github.com/localixai/tokendoctor)</sub> | Replays your past sessions to show what each change would have saved, then applies only what you pick. | lance des commandes, appelle un modèle |
| [`skins`](https://github.com/hellosverre/claude-skins/tree/cf0d39f3785d5c5a4b6189ecc487b1ac479efea0)<br><sub>par hellosverre · [🖼 preview](https://github.com/hellosverre/claude-skins)</sub> | Skins and fifteen themes for the transcript, with rich cards and a usage band; /skin swaps them live. | réseau, lance des commandes, appelle un modèle, fichiers |
| [`ctx-handoff`](https://github.com/cablate/ctx-handoff-mod/tree/a416713a0495be799a31f3650e18458e242270c7)<br><sub>par cablate · [🖼 preview](https://github.com/cablate/ctx-handoff-mod)</sub> | Turns what you teach Claude into project notes, catches common slips, keeps the cache warm and resumes long sessions. | appelle un modèle, fichiers |
| [`great-cto`](https://github.com/avelikiy/great_cto/tree/12dfd86e99627cd6dd1ed394de4786f4ba08499b)<br><sub>par avelikiy · [🖼 preview](https://github.com/avelikiy/great_cto)</sub> | Runs Claude Code as a pipeline of 73 specialist agents, with an independent model checking each stage. | réseau |
| [`ripple`](https://github.com/PBJ-2/clauderipple/tree/c1c6b76a9e4e7a51df2ec5907d6e41d6bf8591e3/packages/mod)<br><sub>par PBJ-2 · [🖼 preview](https://github.com/PBJ-2/clauderipple)</sub> | Picks reasoning effort per prompt and a worker per delegated task, keeps the cache warm and shows where each request went. | réseau, lance des commandes, appelle un modèle, MCP, fichiers |
| [`tavernweave-agent-skills`](https://github.com/LiarMTTT/TavernWeave/tree/f9863d2b05305457fe9ed8b0c5688d52aca400a5)<br><sub>par LiarMTTT · [🖼 preview](https://github.com/LiarMTTT/TavernWeave)</sub> | 23 shared skills for rolecards, software work and bounded cloud tasks, plus a Soul mode switch above the prompt. | — |
| [`agent-usage-guard`](https://github.com/rbartoli/agent-usage-guard/tree/02594c2620be9eb60c32e2f77d9d512d9f61b205)<br><sub>par rbartoli · [🖼 preview](https://github.com/rbartoli/agent-usage-guard)</sub> | Holds subagent fan-out, heavy-context prompts and retry loops before they spend your usage window. | appelle un modèle, fichiers |

### Agents et sous-agents

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Ce qu'il fait | Accès |
| --- | --- | --- |
| [`shared-session`](https://github.com/Paradigm-Study/claude-share/tree/9d88f996ac4245c756a89b34e98cfde375028950/plugin)<br><sub>par Paradigm-Study · [🖼 preview](https://github.com/Paradigm-Study/claude-share)</sub> | Share a session with a link or your team; teammates join from their own Claude Code and watch every turn live. | — |
| [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/626cc0b46d417f81bbff9f5ba3b49abaf8912a85)<br><sub>par scasella · [🖼 preview](https://github.com/scasella/claude-flightdeck)</sub> | A live agent dashboard: model vitals, an on-call architect, permission checks, subagent cards and a session log. | — |
| [`start`](https://github.com/rsmdt/the-startup/tree/e803d51fdb423271d3dde189f5416f3ec51386a9/plugins/start)<br><sub>par rsmdt · [🖼 preview](https://github.com/rsmdt/the-startup)</sub> | Workflow orchestration commands for agentic software development. | fichiers |
| [`lane-stack`](https://github.com/VKirill/claude-lane-stack/tree/8bac2b876b72053aa445bb9d1c7c6079bfc4ba8c/plugins/lane-stack)<br><sub>par VKirill · [🖼 preview](https://github.com/VKirill/claude-lane-stack)</sub> | A solo PM conveyor: orchestrator agents, lane playbooks, onboard and resume commands. | réseau, appelle un modèle |

### Productivité et contexte

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Ce qu'il fait | Accès |
| --- | --- | --- |
| [`pebrel-prompt-suggestions`](https://github.com/Kuddev/pebrel/tree/ed9b2331340877ba3d775e38c4df6bd1a2abb1fe/pebrel_app/res/prompt-suggestions/claude)<br><sub>par Kuddev · [🖼 preview](https://github.com/Kuddev/pebrel)</sub> | Native empty-composer prompt predictions through the Pebrel session bridge. | réseau |
| [`fast-jev-compaction`](https://github.com/tamaratran/fast-jev-compaction/tree/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0)<br><sub>par tamaratran · [🖼 preview](https://github.com/tamaratran/fast-jev-compaction)</sub> | Verbatim Jev-guided compaction for Claude Code sessions. | réseau, appelle un modèle |
| [`lot-map`](https://github.com/alexeyw/lot-map/tree/ad60f057902765d778eedde770d337be45fac3af)<br><sub>par alexeyw · [🖼 preview](https://github.com/alexeyw/lot-map)</sub> | A live map beside the chat: memory, files, shell, web, model, agents, skills and hooks light up as they are used. | — |
| [`storybloq`](https://github.com/Storybloq/storybloq/tree/f0b4c08e3a15ffb9841e5a3058c6b1ca57607154/plugins/storybloq)<br><sub>par Storybloq · [🖼 preview](https://github.com/Storybloq/storybloq)</sub> | Project memory: tickets, issues, handovers and lessons kept in a .story/ folder in your repo. | fichiers |
| [`just-do-it`](https://github.com/Lifecycle-Innovations-Limited/claude-ops/tree/e434ef7e612f2ff5769def6101fc9d984888d377/claude-ops/skills/ops-jdi/plugin)<br><sub>par Lifecycle-Innovations-Limited · [🖼 preview](https://github.com/Lifecycle-Innovations-Limited/claude-ops)</sub> | Continues authorized work through verification and delivery, and surfaces setup issues to repair. | lance des commandes, appelle un modèle |
| [`filetree`](https://github.com/data-goblin/claude-code-filetree/tree/1fdc3a963f2dc22a939f661ff0ff5a76646c9112)<br><sub>par data-goblin · [🖼 preview](https://github.com/data-goblin/claude-code-filetree)</sub> | An IDE-style file tree that shows what Claude is doing and where in your files. | lance des commandes, appelle un modèle, fichiers |
| [`jev-auto-compact`](https://github.com/notque/vexjoy-agent/tree/c68ac1fea2a03e437ccc95112d1e56e467a9bd00/plugins/jev-auto-compact)<br><sub>par notque · [🖼 preview](https://github.com/notque/vexjoy-agent)</sub> | At 60% context, prunes stale tool calls with zero generation; skips instead of falling back to an LLM summary. | réseau, appelle un modèle |
| [`caliber-jev-compaction`](https://github.com/caliber-ai-org/ai-setup/tree/f5dbc002022a8a10acad25c1cce23ddefdc19d0d/plugin/caliber-jev-compaction)<br><sub>par caliber-ai-org · [🖼 preview](https://github.com/caliber-ai-org/ai-setup)</sub> | Verbatim Jev-guided compaction for Claude Code sessions. | réseau, appelle un modèle |
| [`operator`](https://github.com/aerovato/operator-memory/tree/93c3fce64f0a72adeb89fa868600eb418548ec07/packages/claude-code)<br><sub>par aerovato · [🖼 preview](https://github.com/aerovato/operator-memory)</sub> | Durable project and user memory for agent-driven development. | — |
| [`claude-carbon`](https://github.com/gwittebolle/claude-carbon/tree/9ad53f1dd07fb0e11fcdb94d294ed794d660cf4b)<br><sub>par gwittebolle · [🖼 preview](https://github.com/gwittebolle/claude-carbon)</sub> | Tracks the carbon footprint of your Claude Code sessions in the terminal and desktop app. | fichiers |
| [`work-mode`](https://github.com/danyuchn/claude-work-mode/tree/e19eda1e8465308bd79a74fad295cf9b6d9cdf71/plugins/work-mode)<br><sub>par danyuchn · [🖼 preview](https://github.com/danyuchn/claude-work-mode)</sub> | Session modes: auto (no mid-task questions), out (delegate batch work) and wrap (converge and finish). | lance des commandes, fichiers |
| [`show-your-work`](https://github.com/iamumeransari/claude-show-your-work/tree/71e546044e3ba61b98a6938a03270da791f9ca2e)<br><sub>par iamumeransari · [🖼 preview](https://github.com/iamumeransari/claude-show-your-work)</sub> | Shows finished work in the terminal: screenshots, click-through videos and synced before/after QA. | réseau, lance des commandes, appelle un modèle, fichiers |
| [`inbox`](https://github.com/petekp/inbox/tree/02e441cd447edf86fc30fbd03e9117a8ead9da7a)<br><sub>par petekp · [🖼 preview](https://github.com/petekp/inbox)</sub> | Gathers the questions, tasks, findings and PRs waiting on you in a session. | — |
| [`compact-adviser`](https://github.com/kunchenguid/compact-adviser/tree/37fa1a665b8933de68c90014312060e862cf121a/packages/claude-mod)<br><sub>par kunchenguid · [🖼 preview](https://github.com/kunchenguid/compact-adviser)</sub> | Suggests or runs /compact at a completed checkpoint, judged by TypeSafe Jev. | réseau, appelle un modèle, fichiers |

### Rendu et aperçus

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Ce qu'il fait | Accès |
| --- | --- | --- |
| [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/fa9e5eb053d2a1da11f7ccba720a0d3d389c05a6/claude-code-plugin)<br><sub>par zenbu-labs · [🖼 preview](https://github.com/zenbu-labs/terminal-browser)</sub> | A browser inside Claude Code: preview sites and HTML, and let the agent drive the built-in browser. | réseau, lance des commandes, appelle un modèle, fichiers |
| [`prismantis`](https://github.com/NahumLitvin/prismantis/tree/3718a40abc57b836108a65bd9f01d06d3237e52d/plugin)<br><sub>par NahumLitvin · [🖼 preview](https://github.com/NahumLitvin/prismantis)</sub> | Colorful, themeable rendering for replies: tables, headings, code, numbers, paths and links. | lance des commandes, fichiers |

### Sécurité et garde-fous

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Ce qu'il fait | Accès |
| --- | --- | --- |
| [`lcu-approve`](https://github.com/amontlabs/lcu/tree/1bd45b304295c7665b559fcc32f7b3a8f1b1d859/adapters/claude-mod/lcu-approve)<br><sub>par amontlabs · [🖼 preview](https://github.com/amontlabs/lcu)</sub> | Per-app approval for computer use: allow this conversation, always allow, or deny, plus a panel of approved apps. | lance des commandes, MCP, fichiers |
| [`agentctl`](https://github.com/sd0xdev/sd0x-harness/tree/b0206637edd2e44c993da12b6b30858f96bc3cdc/mods/agentctl)<br><sub>par sd0xdev · [🖼 preview](https://github.com/sd0xdev/sd0x-harness)</sub> | An agent control plane for a session: task scope, evidence and hand-over. | lance des commandes, appelle un modèle, fichiers |
| [`multi-core`](https://github.com/greenpolo/cc-multi-cli-plugin/tree/66d9b0a6b06b25fd648ecd53311a647bb57e2fb4/plugins/multi-core)<br><sub>par greenpolo · [🖼 preview](https://github.com/greenpolo/cc-multi-cli-plugin)</sub> | Use ChatGPT, Cursor, OpenCode and Antigravity models inside one session, switching with /model. | réseau, appelle un modèle |
| [`jevmem-pane`](https://github.com/Avinash-jetwani/jevmem/tree/c29753ccb2c9706e417fda25efa422682358955b/pane)<br><sub>par Avinash-jetwani · [🖼 preview](https://github.com/Avinash-jetwani/jevmem)</sub> | A side pane showing what jevmem recalled, what its guard decided and what the last turn saved. | lance des commandes, fichiers |

### Git, PR et déploiements

| Mod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Ce qu'il fait | Accès |
| --- | --- | --- |
| [`fm`](https://github.com/kunchenguid/firstmate/tree/427056c4181c41074ad24f051f79919330df0fa5/.claude/mods/firstmate-calm)<br><sub>par kunchenguid · [🖼 preview](https://github.com/kunchenguid/firstmate)</sub> | The sailboat working animation and a conversation-only transcript, sharing a calm-mode preference across sessions. | fichiers |
| [`turbo`](https://github.com/tobihagemann/turbo/tree/3bc6b4436d96be22497109e16e68fe4dfa323531/claude)<br><sub>par tobihagemann · [🖼 preview](https://github.com/tobihagemann/turbo)</sub> | A human-gated agentic software factory: you decide what to build and judge the result, skills build and ship it. | appelle un modèle, fichiers |
| [`mazyos`](https://github.com/Mazzeo-Marketing/MazyOS/tree/d2b65b392f1ee230afb088d155fc734def5f105d)<br><sub>par Mazzeo-Marketing · [🖼 preview](https://github.com/Mazzeo-Marketing/MazyOS)</sub> | A Portuguese business OS plugin: your company memory in every session, brand identity on outputs, and 17 marketing/SEO skills. | fichiers |
| [`engineer`](https://github.com/swingerman/engineer/tree/ae4cb5fe32007dd6a3d717c9998dcfb12b1f348e/engineer)<br><sub>par swingerman · [🖼 preview](https://github.com/swingerman/engineer)</sub> | A disciplined agentic-engineering methodology kit: intake, AC discovery, spec, planning, implementation, verification, hardening. | lance des commandes, appelle un modèle |

## Proposer un mod

Ouvrez une issue avec le lien vers le dépôt du mod. Pour l'ajouter vous-même, ajoutez une entrée dans `community.json` (dépôt, dossier, commit relu, catégorie, licence), écrivez ses résumés d'une ligne dans `readme/summaries.json`, lancez `python3 scripts/build-catalog.py` et ouvrez une pull request.

## Remerciements

Chaque mod appartient à son auteur et garde sa propre licence ; ce dépôt ne fait que les répertorier. Les auteurs qui souhaitent modifier ou retirer une fiche peuvent ouvrir une issue.

Projet non officiel ; ce n'est pas un produit Anthropic.
