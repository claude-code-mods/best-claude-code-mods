# Best Claude Code Mods

{{languages}}

**厳選、検証済み、バージョン固定。一度追加すれば {{count}} 個の mod がすぐ使える。**

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

{{catalog}}

## mod を推薦する

mod のリポジトリへのリンクを添えて issue を開いてください。自分で追加する場合は、`community.json` にエントリ（リポジトリ、フォルダ、確認したコミット、カテゴリ、ライセンス）を足し、`readme/summaries.json` に各言語の一行紹介を書き、`python3 scripts/build-catalog.py` を実行してプルリクエストを送ってください。

## クレジット

各 mod の権利は作者にあり、それぞれのライセンスに従います。このリポジトリは紹介しているだけです。掲載内容の変更や削除を希望する作者は issue を開いてください。

非公式プロジェクトであり、Anthropic の製品ではありません。
