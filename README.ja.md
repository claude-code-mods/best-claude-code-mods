# Best Claude Code Mods

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · **日本語** · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

**厳選、検証済み、バージョン固定。一度追加すれば 43 個の mod がすぐ使える。**

Mod は関数フックで作られた Claude Code のプラグインです。Claude Code の動作を観察・変更・代行でき、独自の UI も描けます。このマーケットプレイスはコミュニティの優れた mod を集めたものです。どれも `claude plugin validate` で検証し、検証したコミットに固定しているので、作者のその後の変更がレビューなしで届くことはありません。

Claude Code 2.1.287 以降が必要です。

## インストール

Claude Code のターミナルセッションで：

```
/plugin marketplace add claude-code-mods/best-claude-code-mods
/plugin install <mod 名>@best-claude-code-mods
```

例：`/plugin install terminal-browser@best-claude-code-mods`。新しい mod や更新を取り込むには `/plugin marketplace update best-claude-code-mods` を実行します。

## カタログ

**アクセス**列は、UI の描画以外に mod のコードができることとして検証ツールが報告した内容です。インストール前にソースを確認してください。検証はコードを実行せずに読むだけで、セキュリティ監査ではありません。

### ダッシュボードと使用量

| Mod | できること | アクセス |
| --- | --- | --- |
| [`cache-clock`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/cache-clock)<br><sub>作者 hamzafer</sub> | ステータスラインの下に 1 行：キャッシュが温かい残り分数と、冷えた後に次のメッセージで再キャッシュされるトークン数 | ファイル, コマンド実行 |
| [`context-bar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/context-bar)<br><sub>作者 hamzafer</sub> | コンテキストをカテゴリ別に色分けした積み上げバー。トークン数と圧縮ポイント付き（/context-bar で切り替え） | — |
| [`openai-balance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/openai-balance)<br><sub>作者 hamzafer</sub> | OpenAI API の残高見積もり、今日の支出、主な使い道（/openai-balance） | ネットワーク, コマンド実行 |
| [`token-weather`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/token-weather)<br><sub>作者 hamzafer</sub> | コンテキストの使用量を天気予報で表示。プロンプトキャッシュのカウントダウン付き | ファイル, コマンド実行 |
| [`usage-meter`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/usage-meter)<br><sub>作者 hamzafer</sub> | 5 時間と 7 日間の使用量を小さなバーで表示。リセットまでの残り時間とセッションのコスト付き | — |
| [`usage-band`](https://github.com/JetsonChan/CC-Usage-Band/tree/60cd60949b1f52c96ddba3ea24ed0848ff302196/usage-band)<br><sub>作者 JetsonChan</sub> | 5 時間／7 日の上限、コンテキスト、キャッシュ率をプロンプト上に表示。ターミナルとデスクトップ版の両方に対応 | — |
| [`context-view`](https://github.com/kongyo2/context-view/tree/137e4e3db754684144ec953c5e66085bc2959766)<br><sub>作者 kongyo2</sub> | コンテキスト使用量を 1 行で表示。Claude Code 標準のメーターと同じ見た目で、自動圧縮までの残りも分かる | — |
| [`flightdeck`](https://github.com/scasella/claude-flightdeck/tree/f31daca523d36c501cd0df23a737a44c7dc56ad6)<br><sub>作者 scasella</sub> | エージェントのダッシュボード：モデルの状態、権限判定の一覧、サブエージェントのカードとスイムレーン、ターンのレシート、セッションログ | — |
| [`cctop`](https://github.com/tomstagl/cctop/tree/6ceafc34a972f4e58d5e53b1c69f80e2a9759d41/plugin)<br><sub>作者 tomstagl</sub> | btop 風のライブダッシュボード：コンテキスト、トークン、コスト、キャッシュ率、上限、ツール別の所要時間（/cctop） | ファイル, コマンド実行 |
| [`statuspane`](https://github.com/xuanji86/claude-statuspane/tree/13bd8e46edefdf282f117941b886cb529c7d79c3)<br><sub>作者 xuanji86</sub> | プロンプト上のフローティング状態カード：モデル、effort、コンテキスト、5 時間／週の上限、コスト、ブランチ、CI | ファイル, コマンド実行 |
| [`plan-progress`](https://github.com/zycck/claude-mods/tree/3539d02d7435397d293e3120ebad22c23214f6c0/plugins/plan-progress)<br><sub>作者 zycck</sub> | プロンプト上の計画進捗バー：段階、ステップ、ピクセル塗り。判断・エラー・完了時に控えめな効果音 | ファイル, コマンド実行 |

### エージェントとサブエージェント

| Mod | できること | アクセス |
| --- | --- | --- |
| [`agent-flow`](https://github.com/Charlie0113-T/claude-agent-flow/tree/d87b2559dec03979e088026e8f48aee5f9d2cab5)<br><sub>作者 Charlie0113-T</sub> | /flow で会話の横にサブエージェントとチームメイトのライブツリーを表示 | — |
| [`agent-radar`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/agent-radar)<br><sub>作者 hamzafer</sub> | 実行中のサブエージェントごとに 1 行：経過時間、ツール回数、作業内容（/radar で全体表示） | — |
| [`browser-lanes`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/browser-lanes)<br><sub>作者 hamzafer</sub> | Playwright ブラウザを誰が使っているか表示。サブエージェントは順番待ち、/browser clean で残骸を掃除 | コマンド実行 |
| [`mission-control`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/mission-control)<br><sub>作者 hamzafer</sub> | /mission でメインエージェント、サブエージェント、全ツール呼び出しのライブマップと、触れたファイルのコードマップを表示 | ファイル, モデル呼び出し, コマンド実行 |
| [`review-watch`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/review-watch)<br><sub>作者 hamzafer</sub> | 進行中のコードレビュー（Codex またはレビュー用サブエージェント）ごとに 1 行。終了時に指摘をトースト表示 | コマンド実行 |
| [`switchboard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/switchboard)<br><sub>作者 hamzafer</sub> | モデル未指定のサブエージェントにモデルを自動選択（OpenAI Decisions API または Jev）。/route で選択とコストを確認 | ネットワーク |
| [`agentpane`](https://github.com/xuanji86/claude-agentpane/tree/17be88979e5782591a2a184959df1c4168600066)<br><sub>作者 xuanji86</sub> | サブエージェントを一覧するサイドペイン：それぞれの作業内容とトークン消費、クリックで会話を表示 | — |

### 生産性とコンテキスト

| Mod | できること | アクセス |
| --- | --- | --- |
| [`glance`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/glance)<br><sub>作者 hamzafer</sub> | あなた待ちのことを 1 行で：次の会議、PR、Linear の課題、Slack の DM（接続済みの MCP 経由） | MCP, コマンド実行 |
| [`next-steps`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/next-steps)<br><sub>作者 hamzafer</sub> | ターン終了ごとに次のプロンプト候補を 2〜3 個表示。空のプロンプトで 1/2/3 を押して下書き | モデル呼び出し |
| [`session-saver`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/session-saver)<br><sub>作者 hamzafer</sub> | 無題のセッションに名前を付け、/park で中断地点を保存。再開時に表示 | モデル呼び出し, コマンド実行 |
| [`where-am-i`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/where-am-i)<br><sub>作者 hamzafer</sub> | プロンプト上にライブ要約：目標、今やっていること、あなた待ちのこと、次の一手（/where で詳細） | モデル呼び出し |
| [`aside`](https://github.com/JayDoubleu/aside/tree/cf2b7562ae7b376cdcf9e2436a926aba77dc759f)<br><sub>作者 JayDoubleu</sub> | 読み取り専用のサイドチャット：/aside で現在のセッションについて横で質問。本線には書き戻さない | モデル呼び出し |
| [`lcm`](https://github.com/lossless-claude/lcm/tree/0c17dbffda452cf7fae46929af427dff355aeaa3)<br><sub>作者 lossless-claude</sub> | ロスレスなコンテキスト管理：DAG ベースの要約で、すべてのメッセージに後から辿り着ける | ファイル, ネットワーク, モデル呼び出し, コマンド実行 |

### 表示とプレビュー

| Mod | できること | アクセス |
| --- | --- | --- |
| [`gfm-render`](https://github.com/briangtn/claude-gfm-render/tree/a209ad5a0ec35c0813d2d80ab62b596140b0c807)<br><sub>作者 briangtn</sub> | 会話内で GitHub 形式の Markdown を描画：アラート、タスクリスト、取り消し線、Mermaid 図 | コマンド実行 |
| [`md-preview`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/md-preview)<br><sub>作者 hamzafer</sub> | Claude が編集した Markdown を GitHub 風にサイドペインで表示し、変更前後を並べて比較（/md） | ファイル, コマンド実行 |
| [`replay-theater`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/replay-theater)<br><sub>作者 hamzafer</sub> | 直前のターンのファイル編集を diff ごとに再生 | ファイル |
| [`skins`](https://github.com/hellosverre/claude-skins/tree/342fbc0dd49ec44c824ed9c8eb95cd4927d7f81a)<br><sub>作者 hellosverre</sub> | 会話ログのスキン：ツール行、返信の余白、スピナーの文言をテーマ化。/skin でその場で切り替え | — |
| [`mdview`](https://github.com/xuanji86/claude-mdview/tree/da646556714507acf5d41610605b9911eb9aa42a)<br><sub>作者 xuanji86</sub> | 会話中の .md パスをクリックすると横に整形表示（画像付き）。段落を指して Claude に編集させられる | ファイル, コマンド実行 |
| [`terminal-browser`](https://github.com/zenbu-labs/terminal-browser/tree/2165ae76c9639e3996829ab0e6d54ddbd4f06ad8/claude-code-plugin)<br><sub>作者 zenbu-labs</sub> | 会話の横にブラウザを開く。Web サイトやローカル HTML をプレビューでき、エージェントにも操作させられる | ファイル, ネットワーク, コマンド実行 |

### 安全とガード

| Mod | できること | アクセス |
| --- | --- | --- |
| [`blast-radius`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/blast-radius)<br><sub>作者 hamzafer</sub> | 危険な Bash コマンドを止め、何が変わるかを見せてから確認を求める | コマンド実行 |
| [`merge-gate`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/merge-gate)<br><sub>作者 hamzafer</sub> | CI が通り Codex のレビューが 1 回走るまで `gh pr merge` を保留 | ファイル, コマンド実行 |
| [`rulebook-guard`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/rulebook-guard)<br><sub>作者 hamzafer</sub> | 文章と git のルール：本文のダッシュを置換し、amend、未整形の push、個人情報を含むコミットの前に確認 | ファイル, コマンド実行 |
| [`secret-redactor`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/secret-redactor)<br><sub>作者 ray-amjad</sub> | 秘密鍵、メール、IP を会話に入る前に固定のプレースホルダーへ置換し、ツール呼び出し時に元に戻す | — |

### Git・PR・デプロイ

| Mod | できること | アクセス |
| --- | --- | --- |
| [`vercel-deploy-status`](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/12b5fea27a4bd1b88cd9c9b6abc1efc0756c6625/plugins/vercel-deploy-status)<br><sub>作者 ray-amjad</sub> | リンク中のプロジェクトの Vercel デプロイキューと進行状況をプロンプト下に固定表示 | ファイル, コマンド実行 |
| [`cc-pr-tracker`](https://github.com/sezaakgun/cc-pr-tracker/tree/2d96fc7ed6bcca44a350700ac4c37e9066d58b46)<br><sub>作者 sezaakgun</sub> | ウォッチ中の GitHub PR のマージ状態、レビュー、必須チェック。変化があれば通知 | ファイル, コマンド実行 |

### 待ち時間に

| Mod | できること | アクセス |
| --- | --- | --- |
| [`tw-stock-mod`](https://github.com/darrell-tw/darrelltw-mods/tree/649efd272da992051c48d25f30a393e0e0ce45b8/mods/tw-stock-mod)<br><sub>作者 darrell-tw</sub> | 台湾株・米国株のウォッチリスト。取引時間帯で切り替わり、保有銘柄の損益モード付き | ファイル, ネットワーク, コマンド実行 |
| [`mindful-claude`](https://github.com/halluton/Mindful-Claude/tree/411c9c4f4f1c3d128159be7315823341ae7d9e2d)<br><sub>作者 halluton</sub> | Claude が作業中、プロンプト上で呼吸法をガイド。スピナーが呼吸を数える | — |
| [`now-playing`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/now-playing)<br><sub>作者 hamzafer</sub> | Spotify の再生中の曲、進行状況、今の歌詞を 1 行で表示。操作ボタン付き（macOS のみ） | ネットワーク, コマンド実行 |
| [`prayer-times`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/prayer-times)<br><sub>作者 hamzafer</sub> | 現在と次の礼拝時刻と残り時間を、位置情報からローカルで計算。外部送信なし | — |
| [`reels`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/reels)<br><sub>作者 hamzafer</sub> | ターミナルのペインで YouTube Shorts を再生。Claude の作業中は再生、終わると一時停止 | ファイル, ネットワーク, コマンド実行 |
| [`snake`](https://github.com/hamzafer/claude-code-mods/tree/e687416b0f2df0f3ad7f4dfc2065eefe6bc17ea9/mods/snake)<br><sub>作者 hamzafer</sub> | Claude の作業中にペインでスネークゲーム。/snake で開くまで何も出ない | — |
| [`cc-arcade`](https://github.com/sezaakgun/cc-arcade/tree/0baff06d31295850283c2eebe052f39bbc35473f)<br><sub>作者 sezaakgun</sub> | プロンプト上で 9 種のミニゲーム（スネーク、テトリス風、2048 など）と、テストやコミットで育つペット | — |

## mod を推薦する

mod のリポジトリへのリンクを添えて issue を開いてください。自分で追加する場合は、`community.json` にエントリ（リポジトリ、フォルダ、確認したコミット、カテゴリ、ライセンス）を足し、`readme/summaries.json` に各言語の一行紹介を書き、`python3 scripts/build-catalog.py` を実行してプルリクエストを送ってください。

## クレジット

各 mod の権利は作者にあり、それぞれのライセンスに従います。このリポジトリは紹介しているだけです。多くは [awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods) で見つけました。掲載内容の変更や削除を希望する作者は issue を開いてください。

非公式プロジェクトであり、Anthropic の製品ではありません。
