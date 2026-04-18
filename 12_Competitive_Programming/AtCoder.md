# 入力
- 下記を組み合わせて、各行異なる型で取得する事もある
- mapとかの組み込み系関数は、めっちゃ遅い場合があるので、調子に乗ってモリモリするとすぐTLE行く
## 1行1列の入力を受け取る場合
- 入力
  - N
```Python
# 文字列を受け取る場合
S = input() 

# 整数を受け取る場合
N = int(input()) 

# 小数を受け取る場合
F = float(input())
```
- input()で入力を受け取ると、str型として入力を受け取ることができます。
- さらに、整数で受け取りたい場合は int(input()) で受け取ります。
## 1行複数列の入力を受け取る場合
- ２つの入力
  - A B（２つの文字列）
- ３つの入力
  - X Y Z（３つの整数）
```Python
# 文字列を受け取る場合
A, B = input().split()

# 整数を受け取る場合
X, Y, Z = map(int, input().split())

# 小数を受け取る場合
H, M, S = map(float, input().split())
```
- 全ての入力の受け取りに出てくる.split()は()の中に文字を入れることでその文字区切りで入力を受け取ります。
- 何も設定していない今回のような場合はデフォルトで空白扱いになるので、A B と言ったように空白区切りで入力を受け取りたい場合に関しては.split()が必要なことを覚えておきましょう。
## 1行の配列を受け取る場合
A1 A2 ~An
```Python
# 文字列を受け取る場合
A = input().split()

# 整数列を受け取る場合
A = list(map(int, input().split()))

# 小数列を受け取る場合
A = list(map(float, input().split()))
```
- list型として、 【4-2. 1行複数列の入力を受け取る場合】 で紹介したコードを list()で囲むことで入力を受け取ることが可能となります。
```Python
# 入力例　1 3 4 5 6
# 出力
>>>print(l)
[1, 3, 4, 5, 6]
```
### 文字列と数字の複合
```Python
N, S = map(str, input().split())
```
## 複数行複数列の入力を受け取る場合
A1 A2 ~An
B1 B2 ~Bn
```Python
# 複数行の文字列を受け取る場合
A = [input().split() for _ in range(N)]

# 複数行の整数列を受け取る場合
A = [list(map(int, input().split())) for _ in range(N)]

# 複数行の小数列を受け取る場合
A = [list(map(float, input().split())) for _ in range(N)]
```
- 上記の３つの受け取り方のコードはいずれも内包表記と呼ばれる書き方をしています。
- これは、全体のリストの中に N 回 for 文を回したものを受け取ったものを入れています。
- Python ではこの内包表記をよく使うので必ず覚えておきましょう。
## (N,1)行列データ
入力例
3 4
2
3
3
1
```Python
N, M = map(int, input().split())
# リスト内包表記
A = [int(input()) for _ in range(M)]
```
```Python
# 出力
>>>print(A)
[2, 3, 3, 1]
```
## (N,M)行列データ
### 行に変数が並ぶとき
入力
N
x1 x2 x3 .. xN
y1 y2 y3 .. yN

入力例
3
1 2 3
4 5 6
```Python
N = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
```
```Python
# 出力
>>>print(x)
[1, 2, 3]
```
### 列に変数が並ぶとき
入力
N
x1 y1
x2 y2
:
xN yN

入力例
5
1 2
3 4
5 6
7 8
9 10
#### コード例1(x,yを独立に格納)
```Python
N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

# 出力
>>>print(x)
[1, 3, 5, 7, 9]
>>>print(x[1]+y[1])
7
```
# 出力_print文
## ゼロ埋め・幅寄せ
```Python
print("python".ljust(15,'-')) # 左詰め
# python---------
print("python".center(15,'-'))# 中央寄せ
# -----python----
print("python".rjust(15,'-')) # 右詰め
# ---------python

print(str(29).rjust(10,'0')) #10桁ゼロ埋め
# 0000000029
```
## 改行なしの出力
```Python
print(1,end=' ')
print(2,end=' ')

# 出力
1 2 
```

