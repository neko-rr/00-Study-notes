# Python 頻出テク（競プロ・B/C帯向け）

AtCoder の A〜C（ときどき D）でよく使う書き方だけまとめます。

## 関連リンク

| 行きたい内容 | リンク |
|---|---|
| 目次 | [README.md](README.md) |
| A〜C の型 | [abc_ac_patterns.md](abc_ac_patterns.md) |
| 提出テンプレ | [template.py](template.py) |
| エラー対策 | [checklist_wa_tle.md](checklist_wa_tle.md) |
| グリッド | [grid_intro.md](grid_intro.md) |

---

## 1. 入力の基本

```text
【入力例】
3 4
1 2 3
```

```python
N, M = map(int, input().split())
A = list(map(int, input().split()))
```

行が多いとき:

```python
import sys
input = sys.stdin.readline
# 注意: 文字列は rstrip() した方が安全
S = input().rstrip()
```

---

## 2. リスト・二次元配列

```python
# 長さ N の 0 埋め
A = [0] * N

# 二次元（H行W列）※内包表記で作る（同じ行を共有しない）
grid = [[0] * W for _ in range(H)]

# NG例（全部の行が同じリストを指す）
# grid = [[0] * W] * H
```

```text
【入力例】（H行の文字列グリッド）
2 3
#.#
.##
```

```python
H, W = map(int, input().split())
S = [input().rstrip() for _ in range(H)]
print(S[0][1])  # '.'
```

---

## 3. Counter（個数）

```text
【入力例】
4
1 2 1 3
【出力例】（1が何個？）
2
```

```python
from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
print(cnt[1])
```

---

## 4. deque（両端キュー）

BFS・前後からの出し入れに使う。

```python
from collections import deque
q = deque([1, 2, 3])
q.append(4)       # 右に追加
q.appendleft(0)   # 左に追加
q.popleft()       # 左から取る（先頭 pop(0) より速い）
```

迷路 BFS → [grid_intro.md](grid_intro.md)

---

## 5. bisect（ソート済み配列）

```text
【入力例】
5
1 3 3 5 7
3
【出力例】（3 以上の個数）
4
```

```python
from bisect import bisect_left, bisect_right
N = int(input())
A = list(map(int, input().split()))  # ソート済み想定
x = int(input())
# x 以上の個数
print(N - bisect_left(A, x))
```

---

## 6. heapq（優先度付きキュー）

常に最小を取り出す。

```python
import heapq
h = [3, 1, 4]
heapq.heapify(h)
print(heapq.heappop(h))  # 1
heapq.heappush(h, 2)
```

最大が欲しい → 符号を反転して入れる。

---

## 7. set / dict

```python
seen = set()
seen.add(3)
print(3 in seen)  # True

d = {}
d["a"] = d.get("a", 0) + 1

from collections import defaultdict
dd = defaultdict(int)
dd["a"] += 1
```

---

## 8. よく使う一行技

```python
# 合計・最大・最小
print(sum(A), max(A), min(A))

# 全部満たす／どれか満たす
print(all(x > 0 for x in A))
print(any(x == 0 for x in A))

# 文字列の逆
print(S[::-1])

# 空白区切り出力
print(*A)

# 割り算の切り上げ（正の整数）
def ceil_div(a, b):
    return (a + b - 1) // b
```

---

## 9. itertools（順列・組み合わせ）

```python
from itertools import permutations, combinations, product

# 順列（N!）… N≤10 目安
for p in permutations([1, 2, 3]):
    ...

# 組み合わせ
for c in combinations([1, 2, 3, 4], 2):
    ...

# 直積（多重ループの代わり）
for x, y in product(range(H), range(W)):
    ...
```

---

## 10. 提出時の言語

| 場面 | 推奨 |
|---|---|
| A・B | CPython / PyPy どちらでも |
| C 以降 | **PyPy** が多い（速いことが多い） |
| 再帰 DFS | PyPy なら再帰おまじない（[template.py](template.py)） |

詳しい入力パターン → [AtCoder.md](https://github.com/neko-rr/00-Study-notes/blob/main/12_Competitive_Programming/AtCoder.md)
