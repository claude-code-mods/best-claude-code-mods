# Best Claude Code Mods

{{languages}}

**엄선하고, 검증하고, 버전을 고정했습니다. 한 번 추가하면 {{count}}개의 mod를 바로 설치할 수 있습니다.**

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

{{catalog}}

## mod 추천하기

mod 저장소 링크와 함께 이슈를 열어 주세요. 직접 추가하려면 `community.json`에 항목(저장소, 폴더, 확인한 커밋, 분류, 라이선스)을 넣고, `readme/summaries.json`에 언어별 한 줄 소개를 쓴 뒤 `python3 scripts/build-catalog.py`를 실행하고 풀 리퀘스트를 보내 주세요.

## 크레딧

각 mod는 작성자의 것이며 각자의 라이선스를 따릅니다. 이 저장소는 목록만 제공합니다. 상당수는 [awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods)를 통해 찾았습니다. 게재 내용의 수정이나 삭제를 원하는 작성자는 이슈를 열어 주세요.

비공식 프로젝트이며 Anthropic 제품이 아닙니다.
