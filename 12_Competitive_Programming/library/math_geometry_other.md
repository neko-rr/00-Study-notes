# AtCoder 数学用語まとめ③：幾何・ビット・確率（初学者向け）

座標・距離・ビット演算・期待値など、**文章題や実装で引っかかりやすい用語**です。

## 関連リンク

| 行きたい内容 | リンク |
|---|---|
| 目次（ライブラリ全体） | [README.md](README.md) |
| 数学の基礎 | [math_basics.md](math_basics.md) |
| 整数論 | [math_number_theory.md](math_number_theory.md) |
| 文字列 | [substring.md](substring.md) |
| グラフ用語 | [graph_terms.md](graph_terms.md) |
| 計算量の目安 | [complexity.md](complexity.md) |
| bit 全探索コード | [lib/bit.py](lib/bit.py) |
| 最短路・グラフ | [lib/graph.py](lib/graph.py) |
| 累積和・座標圧縮 | [lib/utils.py](lib/utils.py) / [imos_prefix.md](imos_prefix.md) |

---

## 用語一覧

| 用語 | 多い難易度 | ひとこと |
|---|---|---|
| [ユークリッド距離](#1-ユークリッド距離) | C〜D | まっすぐの距離 |
| [マンハッタン距離](#2-マンハッタン距離) | C〜E | 縦横だけの距離 |
| [チェビシェフ距離](#3-チェビシェフ距離) | D〜E | 王将の手数 |
| [ベクトル・内積・外積](#4-ベクトル内積外積) | D〜E | 向き・面積・左右判定 |
| [偏角ソート](#5-偏角ソート) | E寄り | 原点まわりの角度順 |
| [ビット演算](#6-ビット演算) | C〜E | AND/OR/XOR/シフト |
| [部分集合とビット](#7-部分集合とビット) | C〜E | 集合を整数で持つ |
| [期待値](#8-期待値) | D〜E | 平均的に得られる値 |
| [確率の基本](#9-確率の基本) | D〜E | 場合の数／余事象 |
| [座標圧縮](#10-座標圧縮へのつなぎ) | D〜E | 大きい座標を詰め直す |

---

## 1. ユークリッド距離

### 意味
平面上で「定規で測った」まっすぐの距離。  
`√((x1-x2)^2 + (y1-y2)^2)`

```python
import math

def euclidean(x1, y1, x2, y2) -> float:
    return math.hypot(x1 - x2, y1 - y2)  # 精度・速さともおすすめ
```

比較だけなら **平方のまま**（`dx*dx + dy*dy`）にすると平方根が不要。

---

## 2. マンハッタン距離

### 意味
縦と横にしか動けないときの距離（碁盤の目）。  
`|x1-x2| + |y1-y2|`

```python
def manhattan(x1, y1, x2, y2) -> int:
    return abs(x1 - x2) + abs(y1 - y2)
```

### よくある変形
`u = x+y`, `v = x-y` に変換すると、マンハッタンが「最大値の差」扱いになりやすい（D〜E 定石）。

```python
def to_diag(x, y):
    return x + y, x - y
```

---

## 3. チェビシェフ距離

### 意味
8 方向に 1 歩で進めるとき（将棋の王将）の手数。  
`max(|x1-x2|, |y1-y2|)`

```python
def chebyshev(x1, y1, x2, y2) -> int:
    return max(abs(x1 - x2), abs(y1 - y2))
```

---

## 4. ベクトル・内積・外積

### 意味
点を「矢印」として扱う。

| 名前 | 計算（2D） | 使い道 |
|---|---|---|
| 内積 | `ax*bx + ay*by` | 角度が鋭角／直角／鈍角 |
| 外積（z成分） | `ax*by - ay*bx` | 左右どちら向きか、三角形面積 |

```python
def dot(ax, ay, bx, by):
    return ax * bx + ay * by

def cross(ax, ay, bx, by):
    return ax * by - ay * bx

def triangle_area(ax, ay, bx, by, cx, cy):
    """三角形 ABC の面積（符号付き/2）。絶対値を取る"""
    return abs(cross(bx - ax, by - ay, cx - ax, cy - ay)) / 2
```

「線分が交差するか」「点が多角形の内部か」などに発展します。

---

## 5. 偏角ソート

### 意味
点を「原点から見た角度」の順に並べる。  
ラジアンを `atan2` で取るのが定石。

```python
import math

def arg_sort(points, ox=0, oy=0):
    """points: [(x,y), ...] を偏角の昇順で返す"""
    return sorted(
        points,
        key=lambda p: math.atan2(p[1] - oy, p[0] - ox),
    )
```

同角度の扱いや、半直線のグループ分けは問題ごとに注意。

---

## 6. ビット演算

### 意味
整数を 2 進数の「スイッチの列」と見て操作する。

| 演算 | 記号 | 意味 |
|---|---|---|
| AND | `a & b` | 両方 1 なら 1 |
| OR | `a \| b` | どちらか 1 なら 1 |
| XOR | `a ^ b` | 片方だけ 1 なら 1 |
| NOT | `~a` | ビット反転（Python は符号に注意） |
| 左シフト | `a << k` | 2^k 倍 |
| 右シフト | `a >> k` | 2^k で割る（切り捨て） |

```python
x = 13  # 1101
print(x & 1)          # 最下位ビット（奇数判定）
print(x >> 1)         # 1ビット右
print(x | (1 << 3))   # 3 ビット目を立てる
print(x & ~(1 << 2))  # 2 ビット目を消す
print(x ^ (1 << 0))   # 0 ビット目を反転
print(x.bit_count())  # 立っている bit 数（Python 3.10+）
```

---

## 7. 部分集合とビット

### 意味
N 個の要素の「選ぶ／選ばない」を、長さ N のビット列＝整数 `0 .. 2^N-1` で表す。

```python
# i 番目を含むか
def bit_on(mask: int, i: int) -> bool:
    return (mask >> i & 1) == 1

# 全部分集合
N = 3
for mask in range(1 << N):
    chosen = [i for i in range(N) if mask >> i & 1]
    # chosen を使う
```

詳しい列挙・半分全列挙 → [lib/bit.py](lib/bit.py)  
包除との合わせ技 → [math_number_theory.md#7-包除原理inclusion-exclusion](math_number_theory.md#7-包除原理inclusion-exclusion)

---

## 8. 期待値

### 意味
「何回も同じ試行をしたときの平均値」。  
有限個の結果なら  
`E = Σ（その結果になる確率 × その結果の値）`

競プロでは「残り状態からの期待値 DP」も多い。

```python
# サイコロ（1..6 が等確率）の期待値
E = sum(i * (1 / 6) for i in range(1, 7))
print(E)  # 3.5

# 分数で持ちたいとき（誤差回避）→ 分母を揃える／mod 逆元
# 「期待値を mod 998244353 で」と書かれたら逆元を使う
# → math_basics.md の逆元 / lib/modint.py
```

---

## 9. 確率の基本

### 意味
| 考え方 | 内容 |
|---|---|
| 場合の数 | 望ましい場合 ÷ 全体 |
| 余事象 | `1 -（起きてほしくない確率）` の方が簡単 |
| 独立 | 掛け算できる |
| 排反 | 足し算できる（同時には起きない） |

```python
# 例: 赤3, 青2 の袋から1つ。赤の確率
p_red = 3 / (3 + 2)

# 余事象: 「少なくとも1回出る」= 1 - 「一度も出ない」
N, p = 5, 0.3
at_least_one = 1 - (1 - p) ** N
```

数え上げが整数なら [組合せ](math_basics.md#5-階乗順列組合せ) とセットで考える。

---

## 10. 座標圧縮へのつなぎ

### 意味
座標が `10^9` と大きいが、実際に使う点は少ないとき、  
値を `0,1,2,...` に詰め直す。

実装 → [lib/utils.py](lib/utils.py) の `compress`

```python
# イメージ
# [100, 1, 50, 100] → [2, 0, 1, 2]
```

区間に乗せるデータ構造（[Fenwick](lib/fenwick.py) / [SegTree](lib/segment_tree.py)）の前処理で頻出。

---

## 問題を見たらこう選ぶ

| ヒント | 見るところ |
|---|---|
| 「距離」「直線距離」 | [#1](#1-ユークリッド距離) |
| 「上下左右に移動」「|dx|+|dy|」 | [#2](#2-マンハッタン距離) |
| 「8 方向」「王将」 | [#3](#3-チェビシェフ距離) |
| 「面積」「左右どちら」 | [#4](#4-ベクトル内積外積) |
| 「角度順」「偏角」 | [#5](#5-偏角ソート) |
| 「XOR」「ビットが立っている」 | [#6](#6-ビット演算) |
| 「選ぶ／選ばないを全部」 | [#7](#7-部分集合とビット) / [lib/bit.py](lib/bit.py) |
| 「期待値を求めよ」 | [#8](#8-期待値) |
| 「確率」「少なくとも」 | [#9](#9-確率の基本) |
| 「座標が大きい」 | [#10](#10-座標圧縮へのつなぎ) / [lib/utils.py](lib/utils.py) |
