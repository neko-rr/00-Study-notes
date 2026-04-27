# クラウドエンジニアが語るAWS・Azure・GoogleCloud基礎（データベース編）
- [https://asiaquest.connpass.com/event/388038/](https://asiaquest.connpass.com/event/388038/)
- 参加日：2026年4月27日（月）
- 19:00～20:00
- 参加形態：個人参加（プライベート）
- オンライン
- ハッシュタグ ：#クラウド
# クラウドエンジニアが語るAWS・Azure・GoogleCloud基礎（データベース編）
- 初学者向けの話
## データベースとは
- 検索や蓄積が容易にできるようにしたデータ
- よくある区分3種類
- RDBとNoSQL
- RDBの構造・説明
- DBエンジンの特徴
## AWS・Azure・GoogleCloudのデータベース比較
- AWS Aurora
  - MySQLの最大5倍、PostgreSQLの最大3倍のスループットを実現
  - 3つのAZにデータを6個レプリケーション
- Azure SQL
  - 他クラウドのSQL Serverと比較して最大86％コストカット
    - あくまで最大で、唱っているだけだから確認要
    - 確かに3社で一番安い
- Google Cloud
- データ移行
  - AWS
    - 実績豊富で、移行中のダウンタイムを最小化
    - 異なるDBエンジン間の移行に強い
  - Azure
    - SQL Serverからの移行に最適化
    - 移行元を分析し、最適なAzureのスペックを推奨する機能がある
  - GoogleCloud
    - サーバーレスでシンプル
    - 設定が簡単だが、異種間に弱い
- NoSQLとは
  - AWS:4つ
    - 3種類個々に別サービス
  - Azure：1つ
    - 1つで全部対応
  - GoogleCloude：2つ
    - キーバリューストア専用サービスは提供されていない
## 実際にデモ画面を見てみよう
- 本当にデモ
- AWSとAzureの移行
