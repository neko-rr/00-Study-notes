# 参考URL
## 個数数える
- [PythonのCounterでリストの各要素の出現個数をカウント](https://note.nkmk.me/python-collections-counter/#count)
## 含む・位置
- [Pythonで文字列を検索（〜を含むか判定、位置取得）](https://note.nkmk.me/python-str-search/)
- [Pythonで文字列を抽出（位置・文字数、正規表現）](https://note.nkmk.me/python-str-extract/)
- [Pythonのリスト（配列）の特定の要素を抽出、置換、変換](https://note.nkmk.me/python-list-select-replace/)
## 削除
- [Pythonでリスト（配列）の要素を削除するclear, pop, remove, del](https://note.nkmk.me/python-list-clear-pop-remove-del/)
## 辞書
- [Pythonの辞書（dict）のforループ処理（keys, values, items）](https://note.nkmk.me/python-dict-keys-values-items/#items-for)
## 集合
- [Pythonで階乗、順列・組み合わせを計算、生成](https://note.nkmk.me/python-math-factorial-permutations-combinations/)
- [Pythonで複数のリストの直積（デカルト積）を生成するitertools.product](https://note.nkmk.me/python-itertools-product/)
## 出力
- [Pythonの真偽値bool型（True, False）と他の型との変換・判定](https://note.nkmk.me/python-bool-true-false-usage/)
# リスト
## リストを出力する
```Python
a = [9, 9, 7, 3]

# a の要素を空白区切りで出力する
print(*a)

# a の要素を改行区切りで出力する
for x in a:
    print(x)

# 出力
9 9 7 3
9
9
7
3
```
## リスト: 後ろから値にアクセスする
```Python
a = [3, 1, 4, 1, 5]
 
# 負の添字で後ろから順番に要素を取得
print(a[-1])
print(a[-2])
print(a[-3])

# 出力
5
1
4

# 後ろからすべて取り出す。
for s in A[::-1]:
    print(s)
```
# 特定のものを特定
## リストの各要素の出現回数を得る
```Python
from collections import Counter
l = [0, 0, 1, 1, 3, 3, 3]

cnt = Counter(l)
# Counter({3: 3, 0: 2, 1: 2})が格納され、辞書型のように使える

print(cnt[0])
# 2
```
## リストのインデックスを単純に
リストで隣合う数字をビット処理するためにインデックスで指定
```Python
ans = []
n = len(nums)
  for i in range(n - 1):
    ans.append(nums[i] | nums[i + 1])
print(ans)
```
## インデックスにアクセスする
Pythonのループ内で特定の条件が満たされたときにアイテムのインデックス番号を出力するためには、enumerate関数を使うのが便利です。enumerate関数は、ループ中にインデックスとアイテムの両方を提供してくれます。
```Python
A = [[0, 1, 2], [3, 1, 4], [1, 5, 6]]  # 例としてのリスト

for a in A:
    for index, item in enumerate(a):
        if item == 1:
            print(f"itemのインデックス番号: {index}")
```
## リストの中に、特定の文字が何番目（インデックス番号）にあるかを返す
```Python
P = [1, 3, 5, 2, 7, 9]  # 例としてのリスト

# リストの中に2が存在するインデックスを返す
index_of_two = P.index(2)
print(index_of_two)
```
## リストを並べ替える
```Python
# 昇順に並び替える
a.sort

# 降順に並べ替える
a.sort(reverse=True)

# リストを反転する
a.reverse()

a = [3, 1, 4, 1, 5]

# a を昇順に並び替える。a は [1, 1, 3, 4, 5] になる。
a.sort()
print(a)

# a を反転する。a は [5, 4, 3, 1, 1] になる。
a.reverse()
print(a)
```
## リストの重複を排除する
```Python
s = set(a)  # 重複要素を削除した集合を作成

# リストの要素の順序が重要でない、かつ要素がハッシュ可能な場合
a = [7, 3, 3, 2, 5, 8, 2, 5, 6, 5]
s = set(a)  # 重複要素を削除した集合を作成
result = list(s)  # その集合からリストを作成
print(result)  # [2, 3, 5, 6, 7, 8]など
```
## リストの一致するもの一致しないもの合計
- 正の整数nとが与えられますm。
- 2つの整数を以下のように定義します。
- num1[1, n]: 範囲内の整数(両端を含む)で割り切れないすべての整数の合計m。
- num2[1, n]: 範囲内の(両端を含む)で割り切れるすべての整数の合計m。
- 整数 を返しますnum1 - num2。

- 例１：
- 入力: n = 10、m = 3
- 出力: 19
```Python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum(x if x % m != 0 else -x for x in range(1, n + 1))
```
### リストの豆知識
- nums =  元のリストの要素を置き換えません。
- nums[:] = 要素をその場で置き換えます。
- つまり、 がなければ[:]、新しいリストオブジェクトが作成されてしまいますが、これはこの問題の要求に反します。
  - 「別の配列のために余分な領域を割り当てないでください。入力配列をその場で変更し、O(1)の追加メモリを使用することで、これを実現する必要があります。」
# Setの基本
- セット（集合）は、リストと同様に複数の要素から構成されるデータです。
- ただし、セットはリストと異なり要素の重複がない、また要素の順番もない
- セットを作成するには、波括弧で要素を囲みます。
- 辞書と似ているが、辞書はkey:value形式の点が異なる
```Python
set1= {2, 1, 2, 3}
set1 # {1, 2, 3}
```
セットは組み込み関数でもある
```Python
set([1,1,2,2,2,3])
# {1, 2, 3}

set('aabdceabdae')
# {'a', 'b', 'c', 'd', 'e'}

set({'apple' : 3, 'pen' : 5})
# {'apple', 'pen'}
```
# 計算
## 小数の計算
- 小数の計算では、小数を整数に変換、計算後にもとに戻す処理を行う
- 小数→整数の変換では、掛け算より、文字列での変換が確実
```Python

a = 9.79

print(int(a*100))
# 978

print(int(str(a).replace(".", "")))
# 979
```
## 最大公約数、最小公倍数
```Python

# 最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)
```
## 素因数分解
```Python

# nを素因数分解したリストを返す
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
```
## 約数の列挙
```Python

def divs_list(num):
  divs = []
  i = 1
  while i*i <= num:
    if num % i == 0:
      divs.append(i)

      if num // i != i:
        divs.append(num//i)

    i += 1
  return divs
```
## 素数の列挙
- なぜか、「1」より大きいで、「1」含まないに引っかかったから条件確認要
  - 対策：if のandで「1」除外した
- 範囲指定だと、上手く機能しないので、列挙させてから、リスト内包表記で該当部分だけリスト化する
```Python

def sieve_of_eratosthenes(x):
  nums = [i for i in range(x+1)]

  root = int(pow(x, 0.5))
  for i in range(2 ,root + 1):
    if nums[i] != 0:
      for j in range(i, x+1):
        if i*j >= x+1:
          break
        nums[i*j] = 0

  return set(nums)
```
# 文字列
## 先頭を一番後ろに持っていく
```Python
s = 'test'
s = s[1:] + s[0]
```
## 回転文
力尽く(´;ω;｀)
```Python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ans = bool(0)
        new_s = s
        for i in range(len(s)):
          if new_s == goal:
            ans = bool(1)
          new_s = new_s[1:] + new_s[0]
        return ans
```
- 回転文の特徴攻略
  - したがって、goalを回転させることで得られる場合s、それはの部分文字列でなければなりませんs + s。これを実装するには、が連結された文字列の部分文字列であるかどうかをチェックするだけですgoal。部分文字列であればを返しtrue、そうでなければを返しますfalse。
```Python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if the lengths are different
        if len(s) != len(goal):
            return False

        # Create a new string by concatenating 's' with itself
        doubled_string = s + s

        # Use find to search for 'goal' in 'doubledString'
        # If find returns an index that is not -1
        # then 'goal' is a substring
        return doubled_string.find(goal) != -1
```

# 参考URL
- [[Python]Atcoderで入茶するために使ったチートシート](https://zenn.dev/rabbit_penguin0/articles/bcc95f7703124a)
- [Pythonで使う競技プログラミング用チートシート](https://qiita.com/_-_-_-_-_/items/34f933adc7be875e61d0)
- [競プロ用チートシート（Python）](https://qiita.com/wihan23/items/8aa52bcc4d9c45334b1c)
```Python

```
