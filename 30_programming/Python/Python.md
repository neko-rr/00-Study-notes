# 基本
# データや文字列を画面に出力：print
```Python
print(値)
```
##  テキスト
ダブルクォーテーション（"）またはシングルクォーテーション（'）で囲まれたテキストは文字列として認識されます。どちらを使用しても問題ありませんが、プログラムの中で統一して書くようにしてください。
- 一貫性: プログラム内でどちらか一方を選び、統一して使うことが大切です。
- エスケープ: 文字列内に同じ種類のクォーテーションが含まれる場合、もう一方を使うか、エスケープ（\）する必要があります。
  - 例: print("It's a sunny day!") または print('He said, "Hello!"')
```Python
print(出力する文字列 "Hello, World!")
print(出力する文字列 'Hello, World!')
```
## 複数の値の出力
print関数では、カンマ,を使って複数の値を同時に出力することができます。
これにより、異なるデータタイプの値を一度に出力することが可能です。
```Python
name = "Alice"
age = 25
print(name, "さんは", age, "歳です。")
```
Alice さんは 25 歳です。
## 区切り文字と改行の制御
printでは、出力する要素の区切り文字や末尾の改行を制御できます。
```Python
print("Hello", "world", sep="-", end="!")
print("I love you")
```
Hello-world!I love you
## 使用可能なデータ型
文字列（str）、整数（int）、浮動小数点数（float）、リスト（list）、タプル（tuple）、辞書（dict）、ブール値（bool）など
# コメント
## 1行
```Python
# これはコメントです
print("Hello, World!") # この後ろもコメントです
```
## 複数行
```Python
"""
これは複数行の
コメントです。
プログラムの実行には影響しません。
"""

'''
これも複数行の
コメントです。
プログラムの実行には影響しません。
'''
print("Hello, World!")
```
複数行の文字列としての使用する
```Python
message = """
これは複数行の
文字列です。
プログラムの実行に影響します。
"""
print(message)
```
# 変数
変数名 = 値
```Python
number1 = 5
print(number1)
```
## 変数の更新
```Python
variable = 100
variable = "Hello, World!"
print(variable)
```
Hello, World!




