# AtCoder 二分探索・しゃくとり法の型（初学者向け）

「答えを探す」問題で効く 2 大パターンです。  
コード部品は [lib/binary_search.py](lib/binary_search.py) にあります。

## 関連リンク

| 行きたい内容 | リンク |
|---|---|
| 目次 | [README.md](README.md) |
| めぐる式・bisect コード | [lib/binary_search.py](lib/binary_search.py) |
| 計算量 | [complexity.md](complexity.md) |
| 累積和との合わせ技 | [imos_prefix.md](imos_prefix.md) |
| DP との境界 | [dp_patterns.md](dp_patterns.md) |

---

## いつどっち？

| 手法 | こんなとき | 多い難易度 |
|---|---|---|
| **答えの二分探索** | 「最小の X」「最大の X」で、X を決めると可否が単調 | C〜E |
| **配列上の二分探索** | ソート済み列で位置・個数を探す | C〜D |
| **しゃくとり法** | 単調な区間をスライドして条件を満たす最長／最短 | D〜E |

---

## 1. 答えの二分探索（めぐる式）

### 核心
ある値 X について「条件を満たすか？」が  
`NG NG ... NG OK OK ... OK` のように **途中で一度だけ切り替わる**（単調）。

```text
例: 「全員に配るのに必要な最小時間 X」
X が小さい → 無理 (NG)
X が大きい → できる (OK)
→ 境界の最小 OK を探す
```

### 実装の型

```python
def is_ok(x: int) -> bool:
    # x で条件を満たすなら True
    ...

# 「最小の OK」を求めるとき
ok = 10**18   # 必ず OK な大きい値
ng = 0        # 必ず NG な小さい値（問題に合わせる）
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok)
```

部品 → [lib/binary_search.py](lib/binary_search.py) の `meguru_bisect`

### チェックリスト
1. 最適化したい値を X と置く  
2. `is_ok(X)` を書く（シミュレーションや貪欲）  
3. 単調か確認（X を上げると OK が増える／減るだけか）  
4. 初期の ok/ng を「絶対に正しい側」にする  

---

## 2. 配列上の二分探索（bisect）

### いつ使う
- 配列がソート済み
- 「初めて x 以上になる位置」「x 未満の個数」

```python
from bisect import bisect_left, bisect_right

A = [1, 3, 3, 5, 7]
bisect_left(A, 3)   # 1  … 最初の 3
bisect_right(A, 3)  # 3  … 3 より右
# 3 以上 6 未満の個数
bisect_left(A, 6) - bisect_left(A, 3)
```

→ [lib/binary_search.py](lib/binary_search.py)

---

## 3. しゃくとり法（two pointers）

### 核心
左端・右端を持ち、条件を満たすあいだ右を伸ばす／満たさなくなったら左を縮める。  
区間の「良さ」が単調なときに `O(N)`。

### 典型: 和が K 以下の最長区間

```python
def longest_sum_at_most_k(A, K):
    n = len(A)
    ans = 0
    s = 0
    l = 0
    for r in range(n):
        s += A[r]
        while l <= r and s > K:
            s -= A[l]
            l += 1
        ans = max(ans, r - l + 1)
    return ans
```

### いつ使えるか
- 要素が **非負** で、区間を広げると和が非減少、など単調性がある  
- 「条件を満たす区間の個数／最長／最短」

負数が混ざると単調性が壊れ、しゃくとりが使えないことが多いです（その場合は別手法）。

### 累積和との違い
| | しゃくとり | 累積和＋二分探索 |
|---|---|---|
| 条件 | 単調に伸び縮み | 区間和を任意に取る |
| 計算量 | `O(N)` | `O(N log N)` |
| 向く例 | 最長区間 | 「和がちょうど」「任意の [l,r]」 |

累積和 → [imos_prefix.md](imos_prefix.md)

---

## 4. よくある失敗

| 失敗 | 対策 |
|---|---|
| 単調でないのに二分探索 | 反例を考える（X で OK、X+1 で NG にならないか） |
| ok/ng の初期値が弱い | 「絶対 OK／絶対 NG」を入れる |
| しゃくとりで負数を許す | 単調性を再確認 |
| mid で割り算して 0 割り | `is_ok` 内のコーナーを処理 |

---

## 問題を見たら

| ヒント | 手法 |
|---|---|
| 「最小の〜」「最大の〜」＋判定が書ける | 答えの二分探索 |
| ソート済み・何番目 | bisect |
| 「連続する区間で条件」「最長／最短」 | しゃくとり |
| 「区間の和」が主 | [累積和](imos_prefix.md) |
