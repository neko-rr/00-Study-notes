# AtCoder 累積和・いもす法・差分（初学者向け）

「区間の情報をまとめて扱う」定石です。データ構造より軽く、C〜D で頻出です。

## 関連リンク

| 行きたい内容 | リンク |
|---|---|
| 目次 | [README.md](README.md) |
| PrefixSum コード | [lib/utils.py](lib/utils.py) |
| 更新がある区間和 | [data_structures_guide.md](data_structures_guide.md) / [lib/fenwick.py](lib/fenwick.py) |
| しゃくとりとの使い分け | [search_patterns.md](search_patterns.md) |
| 座標圧縮 | [math_geometry_other.md](math_geometry_other.md#10-座標圧縮へのつなぎ) |

---

## 早見表

| やりたいこと | 手法 | 多い難易度 |
|---|---|---|
| 更新なしで区間和を何度も聞く | 累積和 | C〜D |
| 長方形領域の和 | 二次元累積和 | D〜E |
| 区間に +x をたくさん行い、最後に全体を見る | いもす法（差分） | C〜D |
| 点更新が途中で何度もある | Fenwick / セグ木へ | D〜E |

---

## 1. 累積和（1次元）

### 意味
前から足し込んだ配列 `S` を作り、区間和を引き算で取る。

```text
A = [a0, a1, a2, a3]
S = [0, a0, a0+a1, a0+a1+a2, a0+...+a3]
区間 [l, r) の和 = S[r] - S[l]
```

```python
from itertools import accumulate

A = [1, 2, 3, 4]
S = [0] + list(accumulate(A))
# S[r] - S[l] が [l, r) の和
assert S[3] - S[1] == 5  # 2+3
```

クラス版 → [lib/utils.py](lib/utils.py) の `PrefixSum`

### いつ使う
- 配列が途中で変わらない
- 「L から R までの合計」を何回も聞く

---

## 2. 二次元累積和

### 意味
グリッドの長方形和を `O(1)` で取る。

```python
# S[i][j] = 左上 (0,0) から (i-1,j-1) までの和
# 長方形 [r1,r2) x [c1,c2) =
#   S[r2][c2] - S[r1][c2] - S[r2][c1] + S[r1][c1]
```

実装 → [lib/utils.py](lib/utils.py) の `PrefixSum2D`

---

## 3. いもす法（差分配列）

### 意味
「区間 `[l, r)` に +x」を何度も行うとき、毎回ループで足さず、  
**端だけ記録 → 最後に累積和**で展開する。

```text
長さ 5 の配列に [1,4) へ +3 したい
差分 B:  index 0 1 2 3 4 5
         値   0 +3 0 0 -3 0
累積和後:     0  3 3 3  0
```

```python
def imos_range_add(n, operations):
    """
    operations: (l, r, x) のリスト = 半開区間 [l,r) に +x
    戻り値: 最終的な配列（長さ n）
    """
    B = [0] * (n + 1)
    for l, r, x in operations:
        if l < 0 or r > n or l >= r:
            continue
        B[l] += x
        B[r] -= x
    for i in range(n):
        B[i + 1] += B[i]
    return B[:n]
```

#### 入力例・出力例つき（AtCoder 風）

```text
【問題】長さ N の配列（初期0）。区間加算を Q 回したあと、配列を出力。
【入力】
N Q
Q 行: L R X   … 1-index 閉区間 [L,R] に +X
【入力例】
5 2
2 4 3
1 2 1
【出力例】
1 4 3 3 0
```

```python
# 提出イメージ（1-index 閉区間 → 半開に変換）
N, Q = map(int, input().split())
ops = []
for _ in range(Q):
    L, R, X = map(int, input().split())
    ops.append((L - 1, R, X))  # [L,R] → [L-1, R)
print(*imos_range_add(N, ops))
```

【どこを変えるか】
- 最後に配列全体ではなく「最大値だけ」欲しい → `max(imos_range_add(...))`
- 途中で区間和クエリが混ざる → いもすではなく遅延セグ木

### いつ使う
- 区間加算クエリがたくさん
- **途中経過は不要**で、全部終わったあとの配列・最大値が欲しい
- 時刻 `[L,R]` にイベントが起きる人数、など

### 使えないとき
- 「区間加算した直後に、別の区間和を聞かれ、また更新…」が混ざる  
  → [遅延セグ木](lib/lazy_segtree.py) や Fenwick

---

## 4. 差分の考え方（1階差分）

隣との差を取ると、元に戻すのは累積和です。

```python
A = [2, 5, 5, 9]
D = [A[0]] + [A[i] - A[i - 1] for i in range(1, len(A))]
# D = [2, 3, 0, 4]
# 累積すると A に戻る
```

いもす法は「区間加算を差分への 2 点更新に落とす」技法、と覚えるとよいです。

---

## 5. 累積和 ＋ 二分探索

非負配列なら、「左端を固定したとき、和が K 以下になる最大の右端」などを  
累積和＋`bisect` で探せます（`O(N log N)`）。

しゃくとりで `O(N)` にできることも多い → [search_patterns.md](search_patterns.md)

```python
from bisect import bisect_right
from itertools import accumulate

def count_subarrays_sum_at_most_k(A, K):
    S = [0] + list(accumulate(A))
    ans = 0
    for r in range(1, len(S)):
        # S[r] - S[l] <= K → S[l] >= S[r]-K
        # l は 0..r-1。ここでは例として「和 <= K となる l の個数」を簡易に
        # 本問に合わせて書き換えること
        pass
    return ans
```

---

## 問題を見たら

| ヒント | 手法 |
|---|---|
| 区間和を何度も（更新なし） | 累積和 |
| グリッドの長方形和 | 二次元累積和 |
| 区間に加算をたくさん → 最後に見る | いもす法 |
| 更新と区間和が交互 | Fenwick / セグ木 / 遅延セグ木 |
| 連続区間の最長・最短 | [しゃくとり](search_patterns.md) |
