# paizaのゲーム関連情報  
ライブラリ使用する系ではなくて、基礎クイズみたいな謎々みたいな問題。

# paizaラーニング  
学習チケット消費(無料)
- 動画学習の演習課題で、「テストケース」や「模範解答」を閲覧するとき
- レベルアップ問題集で、「コードの提出」や「テストケースの閲覧」、「解答コード例の閲覧」、「解説の閲覧」をするとき

学習チケットは、以下のタイミングで付与されます。最大で6枚所持可能です。
- paizaラーニングのマイページにアクセスしたとき（1日1枚のみ増えます）
- スキルチェックのコードを提出したとき（1つの問題につき1枚まで増えます）

# Python基礎
## コンピュータが小数を正確に表現できないことによる誤差に注意
// 演算子は、演算結果が小数のとき、その数を小さい方の整数を解として得ることができる
⇒負の数字だとより低い方になる
-3.25が-4に。

## 累算代入演算子
```Python
num = 1
num += 2  # num = num + 2 と同じ意味
print(num)
```
※Python は再代入する際に型(テキスト・整数等)を変更することができる。
Javaとかは、出来ないらしい。
⇒エラーの原因になりやすく、分かりにくいので非推奨。

## インデックス抽出
```Python
s = "Hello, World!"
print(s[1:4])
```
※ell:後ろのインデックスは出力されない

```Python
s = "Hello, World!"
print(s[:5])
```
前側全部出力

```Python
s = "Hello, World!"
print(s[7:])
```
後ろ側全部出力

## 文字列の長さ取得
```Python
s = "Hello, World!"
print(len(s))
```

## テキストの反復
s * n のように文字列 s を n 回反復しても、文字列 s が変わるわけではない
```Python
s = "abc"
n = 2
t = s * n
print(s, n, t)
```
s *= n のように *= 演算子を使うと、文字列 s が n 回反復された新たな文字列が、変数 s に再代入される
```Python
s = "abc"
n = 2
s *= n
print(s)
```

## f
f'変数 x が示す値は {x} だ' のように f 文字列を使うと、文字列内の波括弧の箇所が変数 x の値で置換される
※f変数は、テキスト以外もテキストにしてくれる。
```Python
time = "10"
place = "会議室 A"
print(f"{time}時から{place}で会議がおこなわれる。")
```

# 標準文の複数行の読み込み  
.rstrip：データの行末の改行を削除する。改行が残っていると、その後の処理に悪影響を及ぼすことがあるので、ここで削除しています。
```Python
# coding: utf-8
# 標準入力とループ処理
count = int(input())
print("データ個数 " + str(count))
for i in range(count):
    line = input().rstrip()
    print("hello " + line)
```
