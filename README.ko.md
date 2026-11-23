# Best Claude Code Mods

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · **한국어** · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

**엄선하고, 검증하고, 버전을 고정했습니다. 한 번 추가하면 41개의 mod를 바로 설치할 수 있습니다.**

Mod는 함수 훅으로 만든 Claude Code 플러그인입니다. Claude Code의 동작을 관찰하고, 바꾸거나 대신 처리할 수 있으며, 자체 UI도 그릴 수 있습니다. 이 마켓플레이스는 커뮤니티의 뛰어난 mod를 모았습니다. 모두 `claude plugin validate`로 검증했고 검증한 커밋에 고정했기 때문에, 작성자의 이후 변경 사항이 검토 없이 전달되지 않습니다.

Claude Code 2.1.287 이상이 필요합니다.

## 설치

Claude Code 터미널 세션에서:

```
/plugin marketplace add claude-code-mods/best-claude-code-mods
/plugin install <mod 이름>@best-claude-code-mods
```

예: `/plugin install terminal-browser@best-claude-code-mods`. 새 mod와 업데이트를 받으려면 `/plugin marketplace update best-claude-code-mods`를 실행하세요.

## 카탈로그

각 카드의 **접근 범위**는 UI를 그리는 것 외에 mod 코드가 할 수 있다고 검증 도구가 보고한 내용입니다. 설치 전에 소스를 확인하세요. 검증은 코드를 실행하지 않고 읽기만 하며, 보안 감사가 아닙니다.

### 대시보드와 사용량

[![token-optimizer](https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/docs-site/public/media/token-optimizer-desktop-status-bar.gif)](https://github.com/alexgreensh/token-optimizer/tree/e3f1a2dcad8d8999096b8a881c4d98cdba4ef1a5/desktop/token-optimizer-desktop)

#### [`token-optimizer`](https://github.com/alexgreensh/token-optimizer/tree/e3f1a2dcad8d8999096b8a881c4d98cdba4ef1a5/desktop/token-optimizer-desktop)

*제작 alexgreensh* · A token-optimizer status bar that shows where tokens go and how to spend less.

**접근 범위:** 명령 실행, 모델 호출, 파일

`/plugin install token-optimizer@best-claude-code-mods`

[![claude-council](https://github.com/hex/claude-council/raw/main/assets/desktop-code-tab.png)](https://github.com/hex/claude-council/tree/f2f7f42122b288599cef8cea97dcc490acea98a5)

#### [`claude-council`](https://github.com/hex/claude-council/tree/f2f7f42122b288599cef8cea97dcc490acea98a5)

*제작 hex* · Consult several AI agents at once for diverse perspectives, with a streaming pane and an optional heads-up side check.

**접근 범위:** 명령 실행, 모델 호출, 파일

`/plugin install claude-council@best-claude-code-mods`

[![codex-attachment-manager](https://github.com/chipfighter/context-attachment-manager/raw/main/docs/images/hero.gif)](https://github.com/chipfighter/context-attachment-manager/tree/d68a721b7432059c9056d546ff2a26b11b3c0e0c)

#### [`codex-attachment-manager`](https://github.com/chipfighter/context-attachment-manager/tree/d68a721b7432059c9056d546ff2a26b11b3c0e0c)

*제작 chipfighter* · Sends earlier images as short placeholders and fetches originals back by ID, so long image sessions keep the prompt cache.

**접근 범위:** 네트워크, MCP

`/plugin install codex-attachment-manager@best-claude-code-mods`

[![cache-tax](https://github.com/karanb192/cache-tax/raw/main/site/assets/refusal.gif)](https://github.com/karanb192/cache-tax/tree/535ff33225e666e605e731d78f5ac5efe243c7c3)

#### [`cache-tax`](https://github.com/karanb192/cache-tax/tree/535ff33225e666e605e731d78f5ac5efe243c7c3)

*제작 karanb192* · Keeps the one-hour prompt cache warm during breaks, asking before a cold send and showing the rewrite cost.

**접근 범위:** 모델 호출

`/plugin install cache-tax@best-claude-code-mods`

[![agent-standup-band](https://atoll92.github.io/agent-standup/media/banner.png)](https://github.com/Atoll92/agent-standup/tree/846d5324f7c00f06d598c86e87ed8b51d774b3ac/plugin-band)

#### [`agent-standup-band`](https://github.com/Atoll92/agent-standup/tree/846d5324f7c00f06d598c86e87ed8b51d774b3ac/plugin-band)

*제작 Atoll92* · A line above the prompt when another local session needs you, and a toast when one finishes.

**접근 범위:** 명령 실행, 파일

`/plugin install agent-standup-band@best-claude-code-mods`

[![shunt](docs/assets/shunt.png)](https://github.com/pleaseai/shunt/tree/57182b328e92d3c70bc9ca5a1fd1ee9104cfbabb/plugins/shunt)

#### [`shunt`](https://github.com/pleaseai/shunt/tree/57182b328e92d3c70bc9ca5a1fd1ee9104cfbabb/plugins/shunt)

*제작 pleaseai* · A usage band for the shunt gateway: each window's spend and reset time, plus a full /shunt:usage breakdown.

**접근 범위:** 네트워크, 명령 실행

`/plugin install shunt@best-claude-code-mods`

[![tokendoctor](https://github.com/localixai/tokendoctor/raw/main/docs/demo.gif)](https://github.com/localixai/tokendoctor/tree/051fa9598f0a50ed30974b618f2911381b7dcf90)

#### [`tokendoctor`](https://github.com/localixai/tokendoctor/tree/051fa9598f0a50ed30974b618f2911381b7dcf90)

*제작 localixai* · Replays your past sessions to show what each change would have saved, then applies only what you pick.

**접근 범위:** 명령 실행, 모델 호출

`/plugin install tokendoctor@best-claude-code-mods`

[![skins](https://github.com/hellosverre/claude-skins/raw/main/docs/demo.gif)](https://github.com/hellosverre/claude-skins/tree/cf0d39f3785d5c5a4b6189ecc487b1ac479efea0)

#### [`skins`](https://github.com/hellosverre/claude-skins/tree/cf0d39f3785d5c5a4b6189ecc487b1ac479efea0)

*제작 hellosverre* · Skins and fifteen themes for the transcript, with rich cards and a usage band; /skin swaps them live.

**접근 범위:** 네트워크, 명령 실행, 모델 호출, 파일

`/plugin install skins@best-claude-code-mods`

[![ctx-handoff](docs/assets/ctx-handoff-mod.png)](https://github.com/cablate/ctx-handoff-mod/tree/a416713a0495be799a31f3650e18458e242270c7)

#### [`ctx-handoff`](https://github.com/cablate/ctx-handoff-mod/tree/a416713a0495be799a31f3650e18458e242270c7)

*제작 cablate* · Turns what you teach Claude into project notes, catches common slips, keeps the cache warm and resumes long sessions.

**접근 범위:** 모델 호출, 파일

`/plugin install ctx-handoff@best-claude-code-mods`

[![great-cto](docs/assets/great_cto.png)](https://github.com/avelikiy/great_cto/tree/12dfd86e99627cd6dd1ed394de4786f4ba08499b)

#### [`great-cto`](https://github.com/avelikiy/great_cto/tree/12dfd86e99627cd6dd1ed394de4786f4ba08499b)

*제작 avelikiy* · Runs Claude Code as a pipeline of 73 specialist agents, with an independent model checking each stage.

**접근 범위:** 네트워크

`/plugin install great-cto@best-claude-code-mods`

[![ripple](https://github.com/PBJ-2/clauderipple/raw/main/docs/media/demo.webp)](https://github.com/PBJ-2/clauderipple/tree/c1c6b76a9e4e7a51df2ec5907d6e41d6bf8591e3/packages/mod)

#### [`ripple`](https://github.com/PBJ-2/clauderipple/tree/c1c6b76a9e4e7a51df2ec5907d6e41d6bf8591e3/packages/mod)

*제작 PBJ-2* · Picks reasoning effort per prompt and a worker per delegated task, keeps the cache warm and shows where each request went.

**접근 범위:** 네트워크, 명령 실행, 모델 호출, MCP, 파일

`/plugin install ripple@best-claude-code-mods`

[![tavernweave-agent-skills](https://github.com/LiarMTTT/TavernWeave/raw/main/docs/assets/tavernweave-v1-cover.png)](https://github.com/LiarMTTT/TavernWeave/tree/f9863d2b05305457fe9ed8b0c5688d52aca400a5)

#### [`tavernweave-agent-skills`](https://github.com/LiarMTTT/TavernWeave/tree/f9863d2b05305457fe9ed8b0c5688d52aca400a5)

*제작 LiarMTTT* · 23 shared skills for rolecards, software work and bounded cloud tasks, plus a Soul mode switch above the prompt.

**접근 범위:** —

`/plugin install tavernweave-agent-skills@best-claude-code-mods`

[![agent-usage-guard](https://github.com/rbartoli/agent-usage-guard/releases/download/agent-usage-guard--v1.0.0/agent-usage-guard.gif)](https://github.com/rbartoli/agent-usage-guard/tree/02594c2620be9eb60c32e2f77d9d512d9f61b205)

#### [`agent-usage-guard`](https://github.com/rbartoli/agent-usage-guard/tree/02594c2620be9eb60c32e2f77d9d512d9f61b205)

*제작 rbartoli* · Holds subagent fan-out, heavy-context prompts and retry loops before they spend your usage window.

**접근 범위:** 모델 호출, 파일

`/plugin install agent-usage-guard@best-claude-code-mods`


### 에이전트와 서브에이전트

[![shared-session](https://github.com/Paradigm-Study/claude-share/raw/main/docs/assets/invitation-demo.png)](https://github.com/Paradigm-Study/claude-share/tree/9d88f996ac4245c756a89b34e98cfde375028950/plugin)

#### [`shared-session`](https://github.com/Paradigm-Study/claude-share/tree/9d88f996ac4245c756a89b34e98cfde375028950/plugin)

*제작 Paradigm-Study* · Share a session with a link or your team; teammates join from their own Claude Code and watch every turn live.

**접근 범위:** —

`/plugin install shared-session@best-claude-code-mods`

[![flightdeck](https://github.com/scasella/claude-flightdeck/raw/main/docs/media/demo.gif)](https://github.com/scasella/claude-flightdeck/tree/626cc0b46d417f81bbff9f5ba3b49abaf8912a85)

#### [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/626cc0b46d417f81bbff9f5ba3b49abaf8912a85)

*제작 scasella* · A live agent dashboard: model vitals, an on-call architect, permission checks, subagent cards and a session log.

**접근 범위:** —

`/plugin install flightdeck@best-claude-code-mods`

[![start](https://github.com/rsmdt/the-startup/raw/main/logo.png)](https://github.com/rsmdt/the-startup/tree/e803d51fdb423271d3dde189f5416f3ec51386a9/plugins/start)

#### [`start`](https://github.com/rsmdt/the-startup/tree/e803d51fdb423271d3dde189f5416f3ec51386a9/plugins/start)

*제작 rsmdt* · Workflow orchestration commands for agentic software development.

**접근 범위:** 파일

`/plugin install start@best-claude-code-mods`

[![lane-stack](docs/assets/claude-lane-stack.png)](https://github.com/VKirill/claude-lane-stack/tree/8bac2b876b72053aa445bb9d1c7c6079bfc4ba8c/plugins/lane-stack)

#### [`lane-stack`](https://github.com/VKirill/claude-lane-stack/tree/8bac2b876b72053aa445bb9d1c7c6079bfc4ba8c/plugins/lane-stack)

*제작 VKirill* · A solo PM conveyor: orchestrator agents, lane playbooks, onboard and resume commands.

**접근 범위:** 네트워크, 모델 호출

`/plugin install lane-stack@best-claude-code-mods`


### 생산성과 컨텍스트

[![pebrel-prompt-suggestions](https://github.com/Kuddev/pebrel/raw/main/docs/screenshots/nebula-claude-session.png)](https://github.com/Kuddev/pebrel/tree/ed9b2331340877ba3d775e38c4df6bd1a2abb1fe/pebrel_app/res/prompt-suggestions/claude)

#### [`pebrel-prompt-suggestions`](https://github.com/Kuddev/pebrel/tree/ed9b2331340877ba3d775e38c4df6bd1a2abb1fe/pebrel_app/res/prompt-suggestions/claude)

*제작 Kuddev* · Native empty-composer prompt predictions through the Pebrel session bridge.

**접근 범위:** 네트워크

`/plugin install pebrel-prompt-suggestions@best-claude-code-mods`

[![fast-jev-compaction](docs/assets/fast-jev-compaction.png)](https://github.com/tamaratran/fast-jev-compaction/tree/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0)

#### [`fast-jev-compaction`](https://github.com/tamaratran/fast-jev-compaction/tree/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0)

*제작 tamaratran* · Verbatim Jev-guided compaction for Claude Code sessions.

**접근 범위:** 네트워크, 모델 호출

`/plugin install fast-jev-compaction@best-claude-code-mods`

[![lot-map](https://github.com/alexeyw/lot-map/raw/main/docs/demo.gif)](https://github.com/alexeyw/lot-map/tree/ad60f057902765d778eedde770d337be45fac3af)

#### [`lot-map`](https://github.com/alexeyw/lot-map/tree/ad60f057902765d778eedde770d337be45fac3af)

*제작 alexeyw* · A live map beside the chat: memory, files, shell, web, model, agents, skills and hooks light up as they are used.

**접근 범위:** —

`/plugin install lot-map@best-claude-code-mods`

[![storybloq](https://raw.githubusercontent.com/Storybloq/storybloq/main/assets/board.png)](https://github.com/Storybloq/storybloq/tree/f0b4c08e3a15ffb9841e5a3058c6b1ca57607154/plugins/storybloq)

#### [`storybloq`](https://github.com/Storybloq/storybloq/tree/f0b4c08e3a15ffb9841e5a3058c6b1ca57607154/plugins/storybloq)

*제작 Storybloq* · Project memory: tickets, issues, handovers and lessons kept in a .story/ folder in your repo.

**접근 범위:** 파일

`/plugin install storybloq@best-claude-code-mods`

[![just-do-it](docs/assets/claude-ops.png)](https://github.com/Lifecycle-Innovations-Limited/claude-ops/tree/e434ef7e612f2ff5769def6101fc9d984888d377/claude-ops/skills/ops-jdi/plugin)

#### [`just-do-it`](https://github.com/Lifecycle-Innovations-Limited/claude-ops/tree/e434ef7e612f2ff5769def6101fc9d984888d377/claude-ops/skills/ops-jdi/plugin)

*제작 Lifecycle-Innovations-Limited* · Continues authorized work through verification and delivery, and surfaces setup issues to repair.

**접근 범위:** 명령 실행, 모델 호출

`/plugin install just-do-it@best-claude-code-mods`

[![filetree](https://github.com/data-goblin/claude-code-filetree/raw/main/media/filetree-shimmer.gif)](https://github.com/data-goblin/claude-code-filetree/tree/1fdc3a963f2dc22a939f661ff0ff5a76646c9112)

#### [`filetree`](https://github.com/data-goblin/claude-code-filetree/tree/1fdc3a963f2dc22a939f661ff0ff5a76646c9112)

*제작 data-goblin* · An IDE-style file tree that shows what Claude is doing and where in your files.

**접근 범위:** 명령 실행, 모델 호출, 파일

`/plugin install filetree@best-claude-code-mods`

[![jev-auto-compact](https://github.com/notque/vexjoy-agent/raw/main/docs/repo-hero.png)](https://github.com/notque/vexjoy-agent/tree/c68ac1fea2a03e437ccc95112d1e56e467a9bd00/plugins/jev-auto-compact)

#### [`jev-auto-compact`](https://github.com/notque/vexjoy-agent/tree/c68ac1fea2a03e437ccc95112d1e56e467a9bd00/plugins/jev-auto-compact)

*제작 notque* · At 60% context, prunes stale tool calls with zero generation; skips instead of falling back to an LLM summary.

**접근 범위:** 네트워크, 모델 호출

`/plugin install jev-auto-compact@best-claude-code-mods`

[![caliber-jev-compaction](https://github.com/caliber-ai-org/ai-setup/raw/master/assets/readme/pillars.png)](https://github.com/caliber-ai-org/ai-setup/tree/f5dbc002022a8a10acad25c1cce23ddefdc19d0d/plugin/caliber-jev-compaction)

#### [`caliber-jev-compaction`](https://github.com/caliber-ai-org/ai-setup/tree/f5dbc002022a8a10acad25c1cce23ddefdc19d0d/plugin/caliber-jev-compaction)

*제작 caliber-ai-org* · Verbatim Jev-guided compaction for Claude Code sessions.

**접근 범위:** 네트워크, 모델 호출

`/plugin install caliber-jev-compaction@best-claude-code-mods`

[![operator](https://github.com/aerovato/operator-memory/raw/main/docs/assets/change-the-loop.png)](https://github.com/aerovato/operator-memory/tree/93c3fce64f0a72adeb89fa868600eb418548ec07/packages/claude-code)

#### [`operator`](https://github.com/aerovato/operator-memory/tree/93c3fce64f0a72adeb89fa868600eb418548ec07/packages/claude-code)

*제작 aerovato* · Durable project and user memory for agent-driven development.

**접근 범위:** —

`/plugin install operator@best-claude-code-mods`

[![claude-carbon](https://github.com/gwittebolle/claude-carbon/raw/main/docs/desktop-pane.png)](https://github.com/gwittebolle/claude-carbon/tree/9ad53f1dd07fb0e11fcdb94d294ed794d660cf4b)

#### [`claude-carbon`](https://github.com/gwittebolle/claude-carbon/tree/9ad53f1dd07fb0e11fcdb94d294ed794d660cf4b)

*제작 gwittebolle* · Tracks the carbon footprint of your Claude Code sessions in the terminal and desktop app.

**접근 범위:** 파일

`/plugin install claude-carbon@best-claude-code-mods`

[![work-mode](https://github.com/danyuchn/claude-work-mode/raw/main/promo/demo-poster-en.png)](https://github.com/danyuchn/claude-work-mode/tree/e19eda1e8465308bd79a74fad295cf9b6d9cdf71/plugins/work-mode)

#### [`work-mode`](https://github.com/danyuchn/claude-work-mode/tree/e19eda1e8465308bd79a74fad295cf9b6d9cdf71/plugins/work-mode)

*제작 danyuchn* · Session modes: auto (no mid-task questions), out (delegate batch work) and wrap (converge and finish).

**접근 범위:** 명령 실행, 파일

`/plugin install work-mode@best-claude-code-mods`

[![show-your-work](https://github.com/iamumeransari/claude-show-your-work/raw/main/docs/homepage.jpg)](https://github.com/iamumeransari/claude-show-your-work/tree/71e546044e3ba61b98a6938a03270da791f9ca2e)

#### [`show-your-work`](https://github.com/iamumeransari/claude-show-your-work/tree/71e546044e3ba61b98a6938a03270da791f9ca2e)

*제작 iamumeransari* · Shows finished work in the terminal: screenshots, click-through videos and synced before/after QA.

**접근 범위:** 네트워크, 명령 실행, 모델 호출, 파일

`/plugin install show-your-work@best-claude-code-mods`

[![inbox](docs/assets/inbox.png)](https://github.com/petekp/inbox/tree/02e441cd447edf86fc30fbd03e9117a8ead9da7a)

#### [`inbox`](https://github.com/petekp/inbox/tree/02e441cd447edf86fc30fbd03e9117a8ead9da7a)

*제작 petekp* · Gathers the questions, tasks, findings and PRs waiting on you in a session.

**접근 범위:** —

`/plugin install inbox@best-claude-code-mods`

[![compact-adviser](https://github.com/kunchenguid/compact-adviser/raw/main/docs/hint-status-line.png)](https://github.com/kunchenguid/compact-adviser/tree/37fa1a665b8933de68c90014312060e862cf121a/packages/claude-mod)

#### [`compact-adviser`](https://github.com/kunchenguid/compact-adviser/tree/37fa1a665b8933de68c90014312060e862cf121a/packages/claude-mod)

*제작 kunchenguid* · Suggests or runs /compact at a completed checkpoint, judged by TypeSafe Jev.

**접근 범위:** 네트워크, 모델 호출, 파일

`/plugin install compact-adviser@best-claude-code-mods`


### 렌더링과 미리보기

[![terminal-browser](docs/assets/terminal-browser.webp)](https://github.com/zenbu-labs/terminal-browser/tree/fa9e5eb053d2a1da11f7ccba720a0d3d389c05a6/claude-code-plugin)

#### [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/fa9e5eb053d2a1da11f7ccba720a0d3d389c05a6/claude-code-plugin)

*제작 zenbu-labs* · A browser inside Claude Code: preview sites and HTML, and let the agent drive the built-in browser.

**접근 범위:** 네트워크, 명령 실행, 모델 호출, 파일

`/plugin install terminal-browser@best-claude-code-mods`

[![prismantis](https://github.com/NahumLitvin/prismantis/raw/main/docs/tour.gif)](https://github.com/NahumLitvin/prismantis/tree/3718a40abc57b836108a65bd9f01d06d3237e52d/plugin)

#### [`prismantis`](https://github.com/NahumLitvin/prismantis/tree/3718a40abc57b836108a65bd9f01d06d3237e52d/plugin)

*제작 NahumLitvin* · Colorful, themeable rendering for replies: tables, headings, code, numbers, paths and links.

**접근 범위:** 명령 실행, 파일

`/plugin install prismantis@best-claude-code-mods`


### 안전과 가드

[![lcu-approve](https://github.com/amontlabs/lcu/raw/main/docs/assets/approval-demo.gif)](https://github.com/amontlabs/lcu/tree/1bd45b304295c7665b559fcc32f7b3a8f1b1d859/adapters/claude-mod/lcu-approve)

#### [`lcu-approve`](https://github.com/amontlabs/lcu/tree/1bd45b304295c7665b559fcc32f7b3a8f1b1d859/adapters/claude-mod/lcu-approve)

*제작 amontlabs* · Per-app approval for computer use: allow this conversation, always allow, or deny, plus a panel of approved apps.

**접근 범위:** 명령 실행, MCP, 파일

`/plugin install lcu-approve@best-claude-code-mods`

[![agentctl](https://raw.githubusercontent.com/sd0xdev/sd0x-harness/main/banner.jpg)](https://github.com/sd0xdev/sd0x-harness/tree/b0206637edd2e44c993da12b6b30858f96bc3cdc/mods/agentctl)

#### [`agentctl`](https://github.com/sd0xdev/sd0x-harness/tree/b0206637edd2e44c993da12b6b30858f96bc3cdc/mods/agentctl)

*제작 sd0xdev* · An agent control plane for a session: task scope, evidence and hand-over.

**접근 범위:** 명령 실행, 모델 호출, 파일

`/plugin install agentctl@best-claude-code-mods`

[![multi-core](docs/assets/cc-multi-cli-plugin.png)](https://github.com/greenpolo/cc-multi-cli-plugin/tree/66d9b0a6b06b25fd648ecd53311a647bb57e2fb4/plugins/multi-core)

#### [`multi-core`](https://github.com/greenpolo/cc-multi-cli-plugin/tree/66d9b0a6b06b25fd648ecd53311a647bb57e2fb4/plugins/multi-core)

*제작 greenpolo* · Use ChatGPT, Cursor, OpenCode and Antigravity models inside one session, switching with /model.

**접근 범위:** 네트워크, 모델 호출

`/plugin install multi-core@best-claude-code-mods`

[![jevmem-pane](docs/assets/jevmem.png)](https://github.com/Avinash-jetwani/jevmem/tree/c29753ccb2c9706e417fda25efa422682358955b/pane)

#### [`jevmem-pane`](https://github.com/Avinash-jetwani/jevmem/tree/c29753ccb2c9706e417fda25efa422682358955b/pane)

*제작 Avinash-jetwani* · A side pane showing what jevmem recalled, what its guard decided and what the last turn saved.

**접근 범위:** 명령 실행, 파일

`/plugin install jevmem-pane@best-claude-code-mods`


### Git, PR, 배포

[![fm](https://github.com/kunchenguid/firstmate/raw/main/assets/banner.png)](https://github.com/kunchenguid/firstmate/tree/427056c4181c41074ad24f051f79919330df0fa5/.claude/mods/firstmate-calm)

#### [`fm`](https://github.com/kunchenguid/firstmate/tree/427056c4181c41074ad24f051f79919330df0fa5/.claude/mods/firstmate-calm)

*제작 kunchenguid* · The sailboat working animation and a conversation-only transcript, sharing a calm-mode preference across sessions.

**접근 범위:** 파일

`/plugin install fm@best-claude-code-mods`

[![turbo](https://github.com/tobihagemann/turbo/raw/main/assets/logo/thunderbolt-icon-256.png)](https://github.com/tobihagemann/turbo/tree/3bc6b4436d96be22497109e16e68fe4dfa323531/claude)

#### [`turbo`](https://github.com/tobihagemann/turbo/tree/3bc6b4436d96be22497109e16e68fe4dfa323531/claude)

*제작 tobihagemann* · A human-gated agentic software factory: you decide what to build and judge the result, skills build and ship it.

**접근 범위:** 모델 호출, 파일

`/plugin install turbo@best-claude-code-mods`

[![mazyos](docs/assets/MazyOS.png)](https://github.com/Mazzeo-Marketing/MazyOS/tree/d2b65b392f1ee230afb088d155fc734def5f105d)

#### [`mazyos`](https://github.com/Mazzeo-Marketing/MazyOS/tree/d2b65b392f1ee230afb088d155fc734def5f105d)

*제작 Mazzeo-Marketing* · A Portuguese business OS plugin: your company memory in every session, brand identity on outputs, and 17 marketing/SEO skills.

**접근 범위:** 파일

`/plugin install mazyos@best-claude-code-mods`

[![engineer](docs/assets/engineer.png)](https://github.com/swingerman/engineer/tree/ae4cb5fe32007dd6a3d717c9998dcfb12b1f348e/engineer)

#### [`engineer`](https://github.com/swingerman/engineer/tree/ae4cb5fe32007dd6a3d717c9998dcfb12b1f348e/engineer)

*제작 swingerman* · A disciplined agentic-engineering methodology kit: intake, AC discovery, spec, planning, implementation, verification, hardening.

**접근 범위:** 명령 실행, 모델 호출

`/plugin install engineer@best-claude-code-mods`

## mod 추천하기

mod 저장소 링크와 함께 이슈를 열어 주세요. 직접 추가하려면 `community.json`에 항목(저장소, 폴더, 확인한 커밋, 분류, 라이선스)을 넣고, `readme/summaries.json`에 언어별 한 줄 소개를 쓴 뒤 `python3 scripts/build-catalog.py`를 실행하고 풀 리퀘스트를 보내 주세요.

## 크레딧

각 mod는 작성자의 것이며 각자의 라이선스를 따릅니다. 이 저장소는 목록만 제공합니다. 게재 내용의 수정이나 삭제를 원하는 작성자는 이슈를 열어 주세요.

비공식 프로젝트이며 Anthropic 제품이 아닙니다.
