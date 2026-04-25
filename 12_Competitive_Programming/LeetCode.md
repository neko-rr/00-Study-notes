# 入力
LeetCodeのPython入力は、標準入力（input()）ではなく、クラスのメソッド引数として値が渡されます。Solutionクラス内の関数定義に従い、引数を直接利用して処理を記述し、結果をreturnで返します。標準入力を使うとEOFエラーになるため注意が必要です。 
- 入力の受け取り方のポイント:
  - 引数で完結: テンプレート（例: def twoSum(self, nums: List[int], target: int) -> List[int]:）の引数をそのまま利用します。
  - 返り値: 結果を return します。
  - データ型: 配列はList[]、文字列はstr、整数はintとして扱われます。
# テスト
- プレイグラウンドでテストしたい場合は、Redditのディスカッションにあるように、引数に値を直接渡すテストコードを書くか、Qiitaの記事を参考にしてください。
# 出力
- 出力内容を良く確認する事。
  - 例：文字のTrue・falseではなくて、「bool」で回答だった
    - テストが黒色で、確実に正解がprint出来ているならば、疑う事
# 方法例
## リストの中に文字が入っていて、それを結合してひとつの文字列にしたい
```Python
ans_list = ['a', 'b', 'c']
return "".join(ans_list)  # 'abc' を返す
```
# 問題回答参考URL
- 【Python】LeetCodeでハマったアンパック演算子の話[https://note.com/wise_quoll8794/n/nb1a7493183a8](https://note.com/wise_quoll8794/n/nb1a7493183a8)
- Pythonで文字列の長さ（文字数）を取得[https://note.nkmk.me/python-str-len/](https://note.nkmk.me/python-str-len/)
# 利用方法のコツURL
- [LeetCodeとは？コーディングのスキルアップから外資系面接対策まで](https://qiita.com/deafengineers/items/0cd9d09ad9655c03363b)
# 生成AI参考URL
- 普段の問題は、AI使用して良い？のかも。明示的に禁止してなさそう。
- コンペは、アウト
- [LeetCodeコーチングに最適なAI：全レベル対応の適応型面接対策、弱点パターンの検出、模擬シミュレーション](https://www.jenova.ai/ja/resources/best-ai-for-leetcode-coaching)
- [LeetCodeはコードを書く前に方針をAIと壁打ちすると学習効率が上がる🧠(気がする)](https://zenn.dev/yuki_f_saka/articles/6e1e8eb0e9705a)

