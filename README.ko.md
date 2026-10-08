# Best Claude Code Mods

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · **한국어** · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

**엄선하고, 검증하고, 버전을 고정했습니다. 한 번 추가하면 43개의 mod를 바로 설치할 수 있습니다.**

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

**접근 범위** 열은 UI를 그리는 것 외에 mod 코드가 할 수 있다고 검증 도구가 보고한 내용입니다. 설치 전에 소스를 확인하세요. 검증은 코드를 실행하지 않고 읽기만 하며, 보안 감사가 아닙니다.

### 대시보드와 사용량

| Mod | 기능 | 접근 범위 |
| --- | --- | --- |
| [`cache-clock`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/cache-clock)<br><sub>제작 hamzafer</sub> | 상태 표시줄 아래 한 줄: 프롬프트 캐시가 유지되는 남은 분, 식은 뒤 다음 메시지가 다시 캐시할 토큰 수 | 파일, 명령 실행 |
| [`context-bar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/context-bar)<br><sub>제작 hamzafer</sub> | 컨텍스트 창을 카테고리별 색상의 누적 막대로 표시, 토큰 수와 압축 지점 포함(/context-bar로 켜고 끄기) | — |
| [`openai-balance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/openai-balance)<br><sub>제작 hamzafer</sub> | OpenAI API 잔액 추정, 오늘 지출, 주요 사용처(/openai-balance) | 네트워크, 명령 실행 |
| [`token-weather`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/token-weather)<br><sub>제작 hamzafer</sub> | 컨텍스트 사용량을 일기예보처럼 보여 주고, 프롬프트 캐시 카운트다운도 표시합니다 | 파일, 명령 실행 |
| [`usage-meter`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/usage-meter)<br><sub>제작 hamzafer</sub> | 5시간·7일 사용량을 작은 막대로 표시하고, 초기화까지 남은 시간과 세션 비용도 보여 줍니다 | — |
| [`usage-band`](https://github.com/JetsonChan/CC-Usage-Band/tree/60cd60949b1f52c96ddba3ea24ed0848ff302196/usage-band)<br><sub>제작 JetsonChan</sub> | 프롬프트 위에 5시간/7일 한도, 컨텍스트, 캐시 적중률 표시. 터미널과 데스크톱 앱 모두 지원 | — |
| [`context-view`](https://github.com/kongyo2/context-view/tree/137e4e3db754684144ec953c5e66085bc2959766)<br><sub>제작 kongyo2</sub> | 컨텍스트 사용량을 한 줄로, Claude Code 기본 미터와 같은 모양으로 표시하며 자동 압축까지 남은 양도 보여 줍니다 | — |
| [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/f31daca523d36c501cd0df23a737a44c7dc56ad6)<br><sub>제작 scasella</sub> | 에이전트 대시보드: 모델 상태, 모든 권한 판정, 서브에이전트 카드와 스윔레인, 턴 영수증, 세션 로그 | — |
| [`cctop`](https://github.com/tomstagl/cctop/tree/6ceafc34a972f4e58d5e53b1c69f80e2a9759d41/plugin)<br><sub>제작 tomstagl</sub> | btop 스타일 실시간 대시보드: 컨텍스트, 토큰, 비용, 캐시 적중률, 한도, 도구별 지연 시간(/cctop) | 파일, 명령 실행 |
| [`statuspane`](https://github.com/xuanji86/claude-statuspane/tree/13bd8e46edefdf282f117941b886cb529c7d79c3)<br><sub>제작 xuanji86</sub> | 프롬프트 위 플로팅 상태 카드: 모델, effort, 컨텍스트, 5시간/주간 한도, 비용, 브랜치, CI | 파일, 명령 실행 |
| [`plan-progress`](https://github.com/zycck/claude-mods/tree/3539d02d7435397d293e3120ebad22c23214f6c0/plugins/plan-progress)<br><sub>제작 zycck</sub> | 프롬프트 위 계획 진행 막대: 단계, 스텝, 픽셀 채우기, 결정·오류·완료 시 부드러운 알림음 | 파일, 명령 실행 |

### 에이전트와 서브에이전트

| Mod | 기능 | 접근 범위 |
| --- | --- | --- |
| [`agent-flow`](https://github.com/Charlie0113-T/claude-agent-flow/tree/d87b2559dec03979e088026e8f48aee5f9d2cab5)<br><sub>제작 Charlie0113-T</sub> | /flow로 대화 옆에 서브에이전트와 팀원의 실시간 트리를 엽니다 | — |
| [`agent-radar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/agent-radar)<br><sub>제작 hamzafer</sub> | 실행 중인 서브에이전트마다 한 줄: 경과 시간, 도구 호출 수, 하는 일(/radar로 전체 보기) | — |
| [`browser-lanes`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/browser-lanes)<br><sub>제작 hamzafer</sub> | Playwright 브라우저를 누가 쓰는지 표시, 서브에이전트는 차례를 기다리고 /browser clean으로 남은 브라우저 정리 | 명령 실행 |
| [`mission-control`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/mission-control)<br><sub>제작 hamzafer</sub> | /mission으로 메인 에이전트, 서브에이전트, 모든 도구 호출의 실시간 지도와 파일 코드 맵을 엽니다 | 파일, 모델 호출, 명령 실행 |
| [`review-watch`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/review-watch)<br><sub>제작 hamzafer</sub> | 진행 중인 코드 리뷰(Codex 또는 리뷰 서브에이전트)마다 실시간 한 줄, 끝나면 결과를 토스트로 표시 | 명령 실행 |
| [`switchboard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/switchboard)<br><sub>제작 hamzafer</sub> | 모델을 지정하지 않은 서브에이전트에 모델을 자동 선택(OpenAI Decisions API 또는 Jev), /route로 선택과 비용 확인 | 네트워크 |
| [`agentpane`](https://github.com/xuanji86/claude-agentpane/tree/17be88979e5782591a2a184959df1c4168600066)<br><sub>제작 xuanji86</sub> | 서브에이전트 목록 사이드 패널: 각자 하는 일과 토큰 비용, 클릭하면 대화 내용 확인 | — |

### 생산성과 컨텍스트

| Mod | 기능 | 접근 범위 |
| --- | --- | --- |
| [`glance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/glance)<br><sub>제작 hamzafer</sub> | 처리할 일을 한 줄로: 다음 회의, PR, Linear 이슈, Slack DM(연결된 MCP를 통해) | MCP, 명령 실행 |
| [`next-steps`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/next-steps)<br><sub>제작 hamzafer</sub> | 턴이 끝날 때마다 다음 프롬프트 후보 2~3개를 보여 주고, 빈 입력창에서 1/2/3으로 선택 | 모델 호출 |
| [`session-saver`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/session-saver)<br><sub>제작 hamzafer</sub> | 이름 없는 세션에 이름을 붙이고, /park로 진행 상황을 저장해 재개할 때 보여 줍니다 | 모델 호출, 명령 실행 |
| [`where-am-i`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/where-am-i)<br><sub>제작 hamzafer</sub> | 프롬프트 위 실시간 요약: 목표, 지금 하는 일, 당신을 기다리는 일, 다음 단계(/where로 자세히) | 모델 호출 |
| [`aside`](https://github.com/JayDoubleu/aside/tree/cf2b7562ae7b376cdcf9e2436a926aba77dc759f)<br><sub>제작 JayDoubleu</sub> | 읽기 전용 사이드 채팅: /aside로 현재 세션에 대해 옆에서 질문하고, 메인 대화에는 기록하지 않습니다 | 모델 호출 |
| [`lcm`](https://github.com/lossless-claude/lcm/tree/0c17dbffda452cf7fae46929af427dff355aeaa3)<br><sub>제작 lossless-claude</sub> | 무손실 컨텍스트 관리: DAG 기반 요약으로 모든 메시지를 다시 찾을 수 있습니다 | 파일, 네트워크, 모델 호출, 명령 실행 |

### 렌더링과 미리보기

| Mod | 기능 | 접근 범위 |
| --- | --- | --- |
| [`gfm-render`](https://github.com/briangtn/claude-gfm-render/tree/a209ad5a0ec35c0813d2d80ab62b596140b0c807)<br><sub>제작 briangtn</sub> | 대화에서 GitHub 스타일 Markdown 렌더링: 알림 블록, 작업 목록, 취소선, Mermaid 다이어그램 | 명령 실행 |
| [`md-preview`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/md-preview)<br><sub>제작 hamzafer</sub> | Claude가 편집한 Markdown 파일을 사이드 패널에 GitHub 스타일로 렌더링하고 변경 전후를 나란히 비교(/md) | 파일, 명령 실행 |
| [`replay-theater`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/replay-theater)<br><sub>제작 hamzafer</sub> | 직전 턴의 파일 수정을 diff 단위로 하나씩 되짚어 봅니다 | 파일 |
| [`skins`](https://github.com/hellosverre/claude-skins/tree/342fbc0dd49ec44c824ed9c8eb95cd4927d7f81a)<br><sub>제작 hellosverre</sub> | 대화 기록 스킨: 도구 행, 답변 여백, 스피너 문구에 테마 적용. /skin으로 즉시 전환 | — |
| [`mdview`](https://github.com/xuanji86/claude-mdview/tree/da646556714507acf5d41610605b9911eb9aa42a)<br><sub>제작 xuanji86</sub> | 대화 속 .md 경로를 클릭하면 옆에 렌더링해 보여 주고(이미지 포함), 특정 블록을 가리켜 Claude에게 수정을 맡길 수 있습니다 | 파일, 명령 실행 |
| [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/2165ae76c9639e3996829ab0e6d54ddbd4f06ad8/claude-code-plugin)<br><sub>제작 zenbu-labs</sub> | 대화 옆에 브라우저를 엽니다. 웹사이트와 로컬 HTML을 미리 보고, 에이전트가 조작할 수도 있습니다 | 파일, 네트워크, 명령 실행 |

### 안전과 가드

| Mod | 기능 | 접근 범위 |
| --- | --- | --- |
| [`blast-radius`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/blast-radius)<br><sub>제작 hamzafer</sub> | 위험한 Bash 명령을 멈추고, 무엇이 바뀌는지 보여 준 뒤 확인을 받습니다 | 명령 실행 |
| [`merge-gate`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/merge-gate)<br><sub>제작 hamzafer</sub> | CI가 통과하고 Codex 리뷰가 한 번 실행될 때까지 `gh pr merge`를 보류합니다 | 파일, 명령 실행 |
| [`rulebook-guard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/rulebook-guard)<br><sub>제작 hamzafer</sub> | 글쓰기·git 규칙: 본문의 대시를 바꾸고, amend·포맷 안 된 push·개인 정보가 담긴 커밋 전에 확인 | 파일, 명령 실행 |
| [`secret-redactor`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/secret-redactor)<br><sub>제작 ray-amjad</sub> | 비밀 키, 이메일, IP를 대화에 들어가기 전 고정 플레이스홀더로 바꾸고, 도구 호출 때 원래 값으로 되돌립니다 | — |

### Git, PR, 배포

| Mod | 기능 | 접근 범위 |
| --- | --- | --- |
| [`vercel-deploy-status`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/vercel-deploy-status)<br><sub>제작 ray-amjad</sub> | 연결된 프로젝트의 Vercel 배포 대기열과 진행 상황을 프롬프트 아래에 고정 표시 | 파일, 명령 실행 |
| [`cc-pr-tracker`](https://github.com/sezaakgun/cc-pr-tracker/tree/2d96fc7ed6bcca44a350700ac4c37e9066d58b46)<br><sub>제작 sezaakgun</sub> | 지켜보는 GitHub PR의 병합 상태, 리뷰, 필수 검사를 보여 주고 바뀌면 알려 줍니다 | 파일, 명령 실행 |

### 기다리는 동안

| Mod | 기능 | 접근 범위 |
| --- | --- | --- |
| [`tw-stock-mod`](https://github.com/darrell-tw/darrelltw-mods/tree/649efd272da992051c48d25f30a393e0e0ce45b8/mods/tw-stock-mod)<br><sub>제작 darrell-tw</sub> | 대만·미국 주식 관심 종목 보드, 거래 시간대에 따라 전환되며 보유 종목 손익 모드 포함 | 파일, 네트워크, 명령 실행 |
| [`mindful-claude`](https://github.com/halluton/Mindful-Claude/tree/411c9c4f4f1c3d128159be7315823341ae7d9e2d)<br><sub>제작 halluton</sub> | Claude가 일하는 동안 프롬프트 위에서 호흡 운동을 안내하고, 스피너가 호흡을 셉니다 | — |
| [`now-playing`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/now-playing)<br><sub>제작 hamzafer</sub> | Spotify에서 재생 중인 곡, 진행률, 현재 가사를 한 줄로 표시, 제어 버튼 포함(macOS 전용) | 네트워크, 명령 실행 |
| [`prayer-times`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/prayer-times)<br><sub>제작 hamzafer</sub> | 현재와 다음 기도 시간 및 남은 시간을 위치 기반으로 로컬에서 계산, 외부 전송 없음 | — |
| [`reels`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/reels)<br><sub>제작 hamzafer</sub> | 터미널 패널에서 YouTube Shorts 재생, Claude가 일할 때 재생하고 끝나면 일시정지 | 파일, 네트워크, 명령 실행 |
| [`snake`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/snake)<br><sub>제작 hamzafer</sub> | Claude가 일하는 동안 패널에서 스네이크 게임, /snake로 열어야 시작 | — |
| [`cc-arcade`](https://github.com/sezaakgun/cc-arcade/tree/0baff06d31295850283c2eebe052f39bbc35473f)<br><sub>제작 sezaakgun</sub> | 프롬프트 위 미니게임 9종(스네이크, 테트리스류, 2048 등)과 테스트·커밋으로 자라는 펫 | — |

## mod 추천하기

mod 저장소 링크와 함께 이슈를 열어 주세요. 직접 추가하려면 `community.json`에 항목(저장소, 폴더, 확인한 커밋, 분류, 라이선스)을 넣고, `readme/summaries.json`에 언어별 한 줄 소개를 쓴 뒤 `python3 scripts/build-catalog.py`를 실행하고 풀 리퀘스트를 보내 주세요.

## 크레딧

각 mod는 작성자의 것이며 각자의 라이선스를 따릅니다. 이 저장소는 목록만 제공합니다. 상당수는 [awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods)를 통해 찾았습니다. 게재 내용의 수정이나 삭제를 원하는 작성자는 이슈를 열어 주세요.

비공식 프로젝트이며 Anthropic 제품이 아닙니다.
