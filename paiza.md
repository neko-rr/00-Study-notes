# paizaのゲーム関連情報  
ライブラリ使用する系ではなくて、基礎クイズみたいな謎々みたいな問題。

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
