# 便利URL
## 公式：Cursorルール設定
[https://docs.cursor.com/ja/context/rules](https://docs.cursor.com/ja/context/rules)
## 【上級者向け】Cursor を使いこなすための実践テクニック
[https://zenn.dev/renue/articles/0416f05e4055f9](https://zenn.dev/renue/articles/0416f05e4055f9)
## Cursor Rules完全ガイド｜AI開発を加速する設計と運用術
[https://fullfront.co.jp/blog/technology-development/ai-development/cursor-rules-design-operation-guide/](https://fullfront.co.jp/blog/technology-development/ai-development/cursor-rules-design-operation-guide/)
# ルール設定
適用されると、ルールの内容はモデルのコンテキストの先頭に含まれる。これにより、AIはコード生成、編集内容の解釈、ワークフロー支援において一貫した指針を得られる。
- ルールは Chat と Inline Edit に適用される。アクティブなルールは Agent サイドバーに表示される。
## User Rules
Cursor 環境全体で有効。設定で定義され、常に適用される。
- User Rules は、すべてのプロジェクトに適用される Cursor Settings → Rules で定義するグローバルな設定。プレーンテキストで記述できて、好みのコミュニケーションスタイルやコーディング規約を設定するのに最適だよ
## Project Rules
.cursor/rules に保存され、バージョン管理され、コードベースにスコープされる。
- 各ルールは単一ファイルで、バージョン管理の対象。パスパターンで適用範囲を絞ったり、手動で実行したり、関連性に基づいて自動的に取り込める。サブディレクトリには、そのフォルダにスコープされた独自の .cursor/rules ディレクトリを含められる。
- ルールが発動する条件を細かく指定できます
  - Always / Auto Attached / Agent Requested / Manual の 4 つの発動条件のうち、いずれかを選択できます
  - Always: 常にコンテキストとして参照されます
  - Auto Attached: glob で指定されたパターンにマッチした場合に参照されます
  - Agent Requested: description に記載された内容を元に、エージェントが参照するかを決定します
  - Manual: プロンプトにルールを明確に指定した場合にのみ参照されます
- ルール自体は .cursor/rules/ 以下に保存されます。 .mdc という拡張子です。
### プロジェクトルールの使いどころ:
- コードベースに関するドメイン固有知識を記述する
- プロジェクト固有のワークフローやテンプレートを自動化する
- スタイルやアーキテクチャの方針を標準化する
### フォルダ配置
ディレクトリ内のファイルが参照されると、そのディレクトリにあるネストされたルールが自動的に適用される。
```md
project/
  .cursor/rules/        # プロジェクト全体のルール
  backend/
    server/
      .cursor/rules/    # バックエンド用ルール
  frontend/
    .cursor/rules/      # フロントエンド用ルール
```
### 設定方法
New Cursor Rule コマンドを使うか、Cursor Settings > Rules に進んでルールを作成しよう。これで .cursor/rules に新しいルールファイルが作成される。Settings では、すべてのルールとそのステータスを確認できる。
### ベストプラクティス（公式）
- 良いルールは、焦点が明確で、実行可能で、スコープが適切。
- ルールは500行以内に収める
- 大きなルールは、複数の組み合わせ可能なルールに分割する
- 具体的な例や参照ファイルを示す
- あいまいな指示は避ける。社内ドキュメントのように明確に書く
- チャットで同じプロンプトを繰り返す場合は、ルールを再利用する
## AGENTS.md
Markdown 形式の Agent 向け指示。.cursor/rules のシンプルな代替。
- AGENTS.md は、エージェント向けの指示を定義するためのシンプルな Markdown ファイル。プロジェクトのルートに配置すれば、簡単なユースケースでは .cursor/rules の代替として使える。
- Project Rules と違い、AGENTS.md はメタデータや複雑な設定を持たないプレーンな Markdown ファイル。構造化ルールのオーバーヘッドなしで、シンプルで読みやすい指示がほしいプロジェクトに最適。

# 設定（公式）
Cursor は、ignore files（例: .gitignore, .cursorignore）に含まれるものを除き、すべてのファイルをインデックスするよ。
- Show Settings をクリックして、次を行える:
  - 新規リポジトリの自動インデックスを有効化
  - 無視するファイルを設定
- **大容量コンテンツファイルを無視すると、回答の精度が上がるよ。**
# 自分用のルール設定
## User Rules
```md
```
## Project Rules
```md
```
