# AtCoder 計算量・制約の見方（初学者向け）

「解けそうなのに TLE」を減らすための、**制約 → 許される計算量** の早見表です。

## 関連リンク

| 行きたい内容 | リンク |
|---|---|
| 目次 | [README.md](README.md) |
| 二分探索・しゃくとり | [search_patterns.md](search_patterns.md) |
| DP の型 | [dp_patterns.md](dp_patterns.md) |
| bit 全探索 | [lib/bit.py](lib/bit.py) / [math_geometry_other.md](math_geometry_other.md) |
| 高速入力テンプレ | [template.py](template.py) |

---

## 1. まず見る場所

問題文の **制約**（`1 ≤ N ≤ 10^5` など）が、アルゴリズムの上限を決めます。

目安（AtCoder・制限 2 秒前後の感覚）:

| だいたい許される計算量 | 典型制約のイメージ |
|---|---|
| `O(1)` / `O(log N)` | 何でも余裕 |
| `O(N)` / `O(N log N)` | `N ≤ 10^5`〜`10^6` |
| `O(N √N)` | `N ≤ 10^5` ぎりぎり〜注意 |
| `O(N^2)` | `N ≤ 3000`〜`5000` 程度 |
| `O(N^3)` | `N ≤ 300`〜`400`（Floyd もこの帯） |
| `O((N+Q)√N)` | Mo's algorithm（F〜H） |
| `O(2^N * poly)` | `N ≤ 20`〜`22` |
| `O(D^3 log K)` | 行列累乗（D=行列サイズ） |
| `O(N!)` | `N ≤ 10`〜`11` |

※ 言語・定数倍で変わるので「だいたい」です。Python は C++ より遅く感じることが多い → **PyPy** 提出が基本。

---

## 2. よくある制約と「これで解く」

| 制約の例 | 狙いやすい方針 | 関連 |
|---|---|---|
| `N ≤ 20` | bit 全探索 / bit DP | [lib/bit.py](lib/bit.py) |
| `N ≤ 40` | 半分全列挙 | [lib/bit.py](lib/bit.py) |
| `N ≤ 300` | `O(N^3)` DP（区間 DP など） | [dp_patterns.md](dp_patterns.md) |
| `N ≤ 3000` | `O(N^2)` DP・全ペア | [dp_patterns.md](dp_patterns.md) |
| `N ≤ 10^5` | `O(N log N)`（ソート・セグ木・ダイクストラ） | [data_structures_guide.md](data_structures_guide.md) |
| `N,Q ≤ 10^5` | セグ木 / Fenwick / ソート＋二分探索 | 同上 |
| `W ≤ 10^5` でナップサック | `O(NW)` が間に合うか確認 | [dp_patterns.md](dp_patterns.md) |
| 答えに単調性 | 二分探索で `log` を稼ぐ | [search_patterns.md](search_patterns.md) |
| `N≤10^5` の木クエリ | LCA ダブリング | [lib/lca.py](lib/lca.py) |
| 有向グラフのかたまり | SCC | [lib/scc.py](lib/scc.py) |
| 区間種類数など | Mo | [mo.md](mo.md) |
| 線形漸化式の N 項目 | 行列累乗 | [lib/matrix.py](lib/matrix.py) |

---

## 3. 計算量の数え方（ざっくり）

```python
# O(N): 1重ループ
for i in range(N):
    ...

# O(N^2): 二重ループ
for i in range(N):
    for j in range(N):
        ...

# O(N log N): ソートや「ループ × 二分探索」
A.sort()                    # N log N
for x in A:                 # N
    bisect.bisect_left(A, x)  # log N

# O(2^N): bit 全列挙
for mask in range(1 << N):
    ...
```

同じループでも、中が `O(log N)` や `O(N)` だと全体が変わります。

---

## 4. TLE になりやすい実装（Python）

| やりがち | 対策 |
|---|---|
| `input()` を何十万回 | `sys.stdin.readline`（[template.py](template.py)） |
| リストの先頭 `pop(0)` | `collections.deque` |
| 深い再帰 | `sys.setrecursionlimit` ＋ PyPy なら再帰おまじない |
| 文字列の何度も連結 | リストに溜めて `"".join` |
| `N=10^5` で `O(N^2)` | アルゴリズム自体を見直す |

---

## 5. 迷ったらこの順で考える

1. 制約を見て、`O(?)` の上限を決める  
2. その計算量に収まる典型手法を思い浮かべる（上の表）  
3. 実装定数が怖いときは、より軽い手法へ（例: セグ木 → Fenwick）

---

## 練習のコツ

同じ問題でも「制約が `N≤100` なら愚直、`N≤10^5` なら別解」と **制約だけ変えて考える**と、計算量の感覚が身につきます。
