# Langfuse Night #5 COO & CTO 来日+ 特別アナウンスメント！
- [https://langfuse.connpass.com/event/387257/](https://langfuse.connpass.com/event/387257/)
- 参加日：2026年4月24日（金）
- 19:00～21:00
- 参加形態：個人参加（プライベート）
- 東京都港区高輪2丁目21番1号 THE LINKPILLAR 1 NORTH 13階
- ハッシュタグ ：#LangfuseNightJP
# 目次
- 19:05	 Claude Codeの動きをLangfuseで見てみよう！	大坪 (KDDIアジャイル開発センター株式会社)
- 19:25	freeeにおける評価駆動開発の取り組みとLangfuseの活用	Kengo Nakamura, Kenta Ono (フリー株式会社)
- 19:40	 The Data Engine Behind AI: Powering Language Models at Scale	Alexey Milovidov (ClickHouse Co-founder & CTO)
- 20:00 - 20:30	Langfuse Announcement & Roadmap	Max Deichmann (Langfuse Co-Founder & CTO), Clemens Rawert (Co-Founder & COO)　
# Claude Codeの動きをLangfuseで見てみよう！	大坪 (KDDIアジャイル開発センター株式会社)
- Langfuse
  - LLMOpsツール
  - OTELに対応している
  - 3層構造
    - Session：複数のTrace
      - Observationの5タイプ
- Claude CodeもOTELに対応している
- LangfugeのOTELで受け取れる事とClaude Codeで取れるOTELが違う
  - Hooksで取っていこう
    - でも、LLMの出力が見れない
    - イベントデータには、ツールのI/Oが含まれるがLLMのテキスト自体は含まれない
- 対応
  - Session = Session
  - ユーザープロンプト。。。
- ブログに詳細書いています
- デモ
  - LLMテキスト
  - 動き
  - どういう思考経路かをチャート化
- 結果
  - サブエージェントが優れている
  - 更に、この出力をLLM a ジャッジしている
# freeeにおける評価駆動開発の取り組みとLangfuseの活用	Kengo Nakamura, Kenta Ono (フリー株式会社)
- freeeは、ニックネーム文化
  - 本名分からないくらい
- AI機能開発の民主化
  - AI専門チームだけでなく、各ドメインチームがそれぞれ作る
- AI機能における評価の重要性
  - AIの評価は、難しい
  - 「ものさし」が無いと、改善策の良し悪しを判断できない
- 評価駆動開発とオブザーバビリティ
  - オブザーバビリティ基盤が不可欠
  - 共通オブザーバビリティ基盤のメリット
    - どのチームでもすぐ接続できる
    - LLMの入出力のトレーシングや評価スコア蓄積を簡単に行える
    - 本番環境で自チームのAI機能の動きが可視化
- Langfugeの活用とTrace設計
  - 安全管理
    - プロジェクトごとに申請フローを用いた権限管理を実施
    - 保持すべきでない情報が入るリスクのある個所
- ai-log-evaluatorによるルールベース評価
  - ルールベース評価の有効性
    - LLM-as-a-hudgeの機能はあるが、決定的なロジックでの評価がユースケースに合うケースがある
      - 例：経理のOCR
  - Freeeは、Goを使用している
- 導入の効果
  - セキュリティ管理された環境でのログ分析により、エラー調査が効率化
  - trace/observationの検索機能でログ検索が容易に
# The Data Engine Behind AI: Powering Language Models at Scale	Alexey Milovidov (ClickHouse Co-founder & CTO)
- 英語版ウィキペディアは、高品質データ
- 4chanは、低品質。私は使ってない
- 中間的なのは、Raddit
- Common Crawは約25億のウェブページがある
  - 全体のサイズは、500テラバイト
- 1時間12分　46テラバイト
- トークン統計
  - テキストを取り、次に小文字にする
  - ベクトルはの各次元に該当するトークンの数を合計
- Click Houseに大量で複雑なデータセットをロードしてください
  - データを扱うのが楽になります
# Langfuse Announcement & Roadmap	Max Deichmann (Langfuse Co-Founder & CTO), Clemens Rawert (Co-Founder & COO)　
- Langfuseチームは、11人加わって、合計18人
  - 今東京行きの飛行機乗っている人合わせれば、全員が東京に来る予定
- Clickerシステム
- Langfuseの最近の大きな出来事
- Langfuse V3・V4の流れ
- アップグレード
  - V4：Python
  - V5：
- なぜCLIを作ったか
  - エンジニアが使用しやすいように
  - 次にエージェントが使用できるように
- 別の外国人だが、日本語で下記発表
- CLI使用のデモ
  - ジョークを作るエージェント
  - フレームワークは、LangChain
    - でも、何でも使っていいよ
- Langfuseのskillを作りました!
  - [https://langfuse.com/docs/observability/get-started](https://langfuse.com/docs/observability/get-started)
# プロローグ
- 新しいロゴが出来ました！
  - 新グッズは、日本が世界で一番先です！！
  - 日本市場に力を入れています。



