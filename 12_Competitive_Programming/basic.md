# 参考URL
## リスト
- [K - 1.10.リスト](https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_k)
## 個数数える
- [PythonのCounterでリストの各要素の出現個数をカウント](https://note.nkmk.me/python-collections-counter/#count)
## 判定・正規表現・文字列
- [Pythonで文字列が数字か英字か英数字か判定・確認](https://note.nkmk.me/python-str-num-determine/)
- [Pythonの正規表現で漢字・ひらがな・カタカナ・英数字を判定・抽出・カウント](https://note.nkmk.me/python-re-regex-character-type/)
- [Python - 文字列から最後の文字を削除する](https://www.curict.com/item/09/09c27e4.html)
- [Pythonで文字列の一部を削除（stripなど）](https://note.nkmk.me/python-str-remove-strip/)
- [分かりやすいpythonの正規表現の例](https://qiita.com/luohao0404/items/7135b2b96f9b0b196bf3)
## 含む・位置
- [Pythonで文字列を検索（〜を含むか判定、位置取得）](https://note.nkmk.me/python-str-search/)
- [Pythonで文字列を抽出（位置・文字数、正規表現）](https://note.nkmk.me/python-str-extract/)
- [Pythonで文字列のリスト（配列）の条件を満たす要素を抽出、置換](https://note.nkmk.me/python-list-str-select-replace/)
- [Pythonのリスト（配列）の特定の要素を抽出、置換、変換](https://note.nkmk.me/python-list-select-replace/)
## 削除
- [Pythonでリスト（配列）の要素を削除するclear, pop, remove, del](https://note.nkmk.me/python-list-clear-pop-remove-del/)
## 処理
- [Pythonリスト内包表記の使い方](https://note.nkmk.me/python-list-comprehension/)
- [[Python]リストの要素全てに処理を行いたいメモ](https://qiita.com/zhengxi__/items/15f1941f53204f40f30d#%E4%B8%8A%E3%81%AE%E6%93%8D%E4%BD%9C%E3%82%92%E3%83%AB%E3%83%BC%E3%83%97%E3%81%A7%E8%A1%8C%E3%81%86)
## 多次元
### 多次元のソート
- [Pythonで2次元配列（リストのリスト）をソート](https://note.nkmk.me/python-list-2d-sort/#google_vignette)
### 多次元配列変換
- [【Python】二次元配列を自在に操れ。【初期化・参照・抽出・計算・転置】](https://qiita.com/sho11hei12-1998/items/2458aa0822cc6e7268fa)
- [`append`と`extend`の違いを知らないと、思わぬバグを生むことになる](https://zenn.dev/ykesamaru/articles/73958e64c226bb)
## 辞書
- [Pythonの辞書（dict）のforループ処理（keys, values, items）](https://note.nkmk.me/python-dict-keys-values-items/#items-for)
## 集合
- [Pythonで階乗、順列・組み合わせを計算、生成](https://note.nkmk.me/python-math-factorial-permutations-combinations/)
- [Pythonで複数のリストの直積（デカルト積）を生成するitertools.product](https://note.nkmk.me/python-itertools-product/)
## 出力
- [Pythonの真偽値bool型（True, False）と他の型との変換・判定](https://note.nkmk.me/python-bool-true-false-usage/)
## エラー
- [【AtCoder】RE,MLEが出た時の対処法(灰色コーダー向け)【競技プログラミング】](https://qiita.com/sano192/items/2da11eaeeeea3daab944)
# 範囲:range()
range(a, b, c) という書き方もできこれによりいくつずつ増やすかを決めることができます  
（c を省略したときのデフォルトは 1 なので、これまでの書き方では全て 1 ずつ増えていました）。
よって、次のように書くことで 2 ずつ増やすことができます。  
なお、いくつずつ増やすかを決めるときは a がたとえ 
0 だとしても省略できないことに注意してください。つまり、上のコードで range(10, 2) と書くと異なる挙動になってしまいます。
```Python
for i in range(0, 10, 2):
    print(i)
```
```
0
2
4
6
8
```
## 昇順・降順range()
```Python
N = 5

print("昇順")
for i in range(N):
    print(i)

print("降順")
for i in range(N - 1, -1, -1):
    print(i)
```
```
昇順
0
1
2
3
4
降順
4
3
2
1
0
```
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
## リストに追加
appendとextendの違い
### append()
引数に渡された値をリストの末尾に追加
```Python
lst = [1, 2, 3]
lst.append(4)  # [1, 2, 3, 4]
```
誤用
```Python
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1.append(lst2)  # [1, 2, 3, [4, 5, 6]]
```
### extend()　リストにリストを追加する場合
引数に渡された別のリストを追加してリストを拡張
```Python
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1.extend(lst2)  # [1, 2, 3, 4, 5, 6]
```
誤用
```Python
lst = [1, 2, 3]
lst.extend(4)  # TypeError: 'int' object is not iterable
```
## 空リスト作成
長さがNですべての要素が0であるようなリストを作る
```Python
DP = [0]*N
```
## リストのコピー
- リストの仕組解説図解[Python の変数と参照, mutable と immutable](https://hackmd.io/@tatyam-prime/Hy-GpIvmp#)
### 一次元配列の中身をコピーしたい時
```Python
A = [1,2,3]
B = A[:]
A[1] = 100
print(A) #[1, 100, 3]
print(B) #[1, 2, 3]
```
リストに対してスライスを用いることで、新たなリストが生成されるため二つの参照する先のリストは別々のものとなり、Aを変更してもBが変更されなくなりました
### リストの豆知識
- nums =  元のリストの要素を置き換えません。
- nums[:] = 要素をその場で置き換えます。
- つまり、 がなければ[:]、新しいリストオブジェクトが作成されてしまいますが、これはこの問題の要求に反します。
  - 「別の配列のために余分な領域を割り当てないでください。入力配列をその場で変更し、O(1)の追加メモリを使用することで、これを実現する必要があります。」
## リストに変換
文章を1文字ずつ判定したい時に使用
```Python
S = "00_sample"
SS = list(S)  # ["0","0","_","s","a","m","p","l","e"]
print("".join(ans))  # "00_sample"に戻る
```
整数ならば
```Python
n = 1000
s = [int(ch) for ch in str(n)]
```
## リストに2乗
```Python
squareSum = sum(d * d for d in s)©leetcode
```
## 特定のものを特定
### リストの各要素の出現回数を得る
```Python
from collections import Counter
l = [0, 0, 1, 1, 3, 3, 3]

cnt = Counter(l)
# Counter({3: 3, 0: 2, 1: 2})が格納され、辞書型のように使える

print(cnt[0])
# 2
```
### リストのインデックスを単純に
リストで隣合う数字をビット処理するためにインデックスで指定
```Python
ans = []
n = len(nums)
  for i in range(n - 1):
    ans.append(nums[i] | nums[i + 1])
print(ans)
```
### インデックスにアクセスする
Pythonのループ内で特定の条件が満たされたときにアイテムのインデックス番号を出力するためには、enumerate関数を使うのが便利です。enumerate関数は、ループ中にインデックスとアイテムの両方を提供してくれます。
```Python
A = [[0, 1, 2], [3, 1, 4], [1, 5, 6]]  # 例としてのリスト

for a in A:
    for index, item in enumerate(a):
        if item == 1:
            print(f"itemのインデックス番号: {index}")
```
### リストの中に、特定の文字が何番目（インデックス番号）にあるかを返す
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
### 2次元配列を並び替える
[[0,1][0,1]]のindex1を降順で並び替え
```Python
a_sorted = sorted(a, key=lambda x: x[1], reverse=True)
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
# 多次元配列
```
a = [[1,2,3],[4,5,6]]
```
## 2次元配列の空配列作成
```Python
n = "空配列必要な個数の整数"
empty_matrix = [[] for _ in range(n)]
```
n = 3ならば、[[], [], []]
### 多次元配列の空配列作成
```Python
A = [[0]*3 for _ in range(3)]
A[1][1] = 100
print(A) #[[0, 0, 0], [0, 100, 0], [0, 0, 0]]
```
内包表記で[0]*3というリストを作るというのが3回行われるため、それぞれのリストは別のオブジェクトとなります。
## 2次元配列に値を追加
```Python
empty_matrix[0].append(1)
empty_matrix[1].append(2)
empty_matrix[2].append(3)
print(empty_matrix)
```
[[1], [2], [3]]
## 多次元配列のコピー / deepcopyは遅い
推奨
```Python
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [a[:] for a in A]
print(A) #[[1, 2, 3], [4, 100, 6], [7, 8, 9]]
print(B) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
次元が高くなったらその分だけ内包表記を深くしましょう
```Python
B = [a1[:] for a1 in A]
B = [[a1[:] for a1 in a2] for a2 in A]
B = [[[a1[:] for a1 in a2] for a2 in a3] for a3 in A]
B = [[[[a1[:] for a1 in a2] for a2 in a3] for a3 in a4] for a4 in A]
```
競技プログラミング以外では便利かもしれませんが、競技プログラミングにおいてはあまりに遅すぎるので下記は使わないことを強く推奨します。
```Python
import copy
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = copy.deepcopy(A)
A[1][1] = 100
print(A) #[[1, 2, 3], [4, 100, 6], [7, 8, 9]]
print(B) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
### 2次元配列のprint
- [Python 2次元配列(数値)の数値を半角空白で区切ってprintする](https://qiita.com/hakone_san/items/8c71917f966d7d407f11)
### 2次元配列色々
```Python
for i in n:
  kn += 1
  for j in range(1,xy[i][0] + 1):
    ans[xy[i][j]-1].append(kn)

ll = []
for l in n:
  ans[l].insert(0,len(ans[l][:]))

for i in n:
    print(' '.join(list(map(str,ans[i]))))
```
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
# 連結リスト
- [連結リストを学ぶ -Python-](https://qiita.com/tsudaryo1715/items/12c4848028716ab015bb)
- [4.2   連結リスト](https://www.hello-algo.com/ja/chapter_array_and_linkedlist/linked_list/)
# 再帰上限
Pythonではデフォルトで再帰関数の深さの上限が1000に設定されています。  
この1000という設定は競技プログラミングにおいて小さすぎます。上限を上げないとREしてしまうでしょう...  
上限はsys.setrecursionlimit()で変更可能なので再帰関数を用いるときは必ず大きめの値に変更しておきましょう。  
```Python
import sys
sys.setrecursionlimit(10**7)
```
# 4300桁制限
pythonのintは多倍長整数であり、数千桁といったとても大きい数も扱うことができます。が、CPython3.10.7, 3.9.14, 3.8.14, 3.7.14以降のバージョンではなんと文字列と整数の変換が4300桁に制限されました。これは文字列を整数、整数を文字列のどちらの変換でも発生し、10進数以外(2進数や16進数など)でも発生します。
最近のアップデートで追加された制限であり、実際に2023年の言語アップデート以前はなかった制限でした。ローカルにあるPythonのバージョンによっては、エラーが発生しないためなぜREが出ているのか長い間わからないケースもあるでしょう。
桁数の制限はsys.set_int_max_str_digits()で変更できます。特に、引数に0を指定すると制限自体がなくなります。多倍長整数を使いたいときは注意しましょう。
```Python
import sys
sys.set_int_max_str_digits(0)
```
多倍長整数とは、CPUが直接扱える固定ビット幅（例: 64bit）を超える大きさの整数を、配列など複数の機械語整数を組み合わせて表現し、任意に近い精度で計算できるようにした整数型です。暗号、数値計算、競技プログラミングなどで用いられ、多くの言語ではBigIntegerなどの名前でライブラリとして提供されます。
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
## roundは四捨五入じゃない
丸め方は、丸める桁が5より小さければ切り捨て、5より大きければ切り上げます。これだけを見ると四捨五入？と思うかもしれませんが、5と等しいときは偶数のほうに丸められます。例えばround(1.5)は2ですが、round(0.5)は0になります。
また、小数の誤差によって予想と反する結果となる場合があります。例えば、round(2.675, 2)は2.68ではなく2.67になります。
四捨五入をしたいときはdecimalのquantize()を用いましょう。第一引数に丸める桁を指定します。
roundingにROUND_HALF_UPを指定すると四捨五入となります。
```Python
from decimal import Decimal,ROUND_HALF_UP
print(Decimal('0.5').quantize(Decimal('1'),rounding = ROUND_HALF_UP)) #1
print(Decimal('1.55').quantize(Decimal('1.0'),rounding = ROUND_HALF_UP)) #1.6
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
## 文字列結合
pythonの文字列はイミュータブルです。つまり、何らかの処理をするたびにオブジェクトの作り直しが発生しています。オブジェクトを作り直すときに文字をコピーしないといけないため、文字列の長さをN
として、O(N)だけ文字列の作り直しにかかってしまいます。  
文字列をたくさん結合したいような時にはどのようにすればよいのでしょうか？そんな時は"".join()を使いましょう。結合する文字列を保持しておくためのリストを作ります
```Python
S = []
for i in range(10000000):
    S.append("x")
print("".join(S))
```
###　悪例
```Python
#めっちゃ遅い...
S = ""
for i in range(10000000):
    S += "x"
print(S)
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
# 型変換のコストは無視できない
結果がfloatになるようなDPなどで、初期値を10**18などで初期化してしまうと、毎回intをfloatに変換するコストがかかってしまい、結果的に低速になります。floatで計算したいものは初めから初期値もfloatにしましょう。
# 参考URL
- [[Python]Atcoderで入茶するために使ったチートシート](https://zenn.dev/rabbit_penguin0/articles/bcc95f7703124a)
- [Pythonで使う競技プログラミング用チートシート](https://qiita.com/_-_-_-_-_/items/34f933adc7be875e61d0)
- [競プロ用チートシート（Python）](https://qiita.com/wihan23/items/8aa52bcc4d9c45334b1c)
- [PythonのSortedContainersで一番大きい要素にアクセスしたいときは-1でアクセスした方がいい](https://qiita.com/kemuniku/items/9691f43cc81cf5271e84)
# 理解してない
## Fractions
Fractionsは有理数を扱うPythonの標準ライブラリです。割り算をしても分子と分母をもっているので誤差が生まれないので正確な計算をすることができるのですが、滅茶苦茶に遅いです。
CPythonでもPyPyでも遅いです。何回も有理数同士の比較を行うとすぐにTLEしてしまいます。
有理数ライブラリは自作しましょう...
## networkx
networkxはAtCoder上のジャッジに搭載されているグラフライブラリです。
たくさんのグラフアルゴリズムが入っていますが、とても低速です...
基本的にコンテスト中に使うのが怖いレベルで低速なので、ご利用は計画的に...
## defaultdict
defaultdictはその名の通り、デフォルトの設定されているdictです。
存在しないキーでアクセスをしようとしたときに、設定したデフォルト値を代入してそれが返ってきます。
競プロではとても便利なのですが、このアクセスしようとしたときにキーがなかったら代入されるという仕様のせいで、存在しないキーの値を何回も何回も呼び出そうとすると遅くなってしまうケースがあります。(具体的には
10**7回呼び出そうとして、TLEしたことがあります。)
デフォルト値を呼び出す回数が多そうである場合は、そのキーがdefaultdictのキーとして設定されているかをinなどを用いて判定したほうが良いでしょう。
## deque
pythonでcollections.deque()はqueue.Queue()よりも高速であることから、BFSなどによく使われています。が、このdequeのランダムアクセスにかかる平均計算量はサイズをNとしてO(N)になります。このことから、C++などのdequeと同じ感覚で使うと計算量が異なることからTLEの原因となってしまいます。


```Python

```

