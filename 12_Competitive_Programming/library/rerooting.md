# 全方位木 DP（Rerooting）（初学者向け・F〜H 対策）

根付き木 DP を、**すべての頂点を根にした結果**へ拡張する技法です。

## 関連リンク

| 行きたい内容 | リンク |
|---|---|
| 目次 | [README.md](README.md) |
| 木・LCA | [lib/lca.py](lib/lca.py) / [graph_terms.md](graph_terms.md) |
| DP 全般 | [dp_patterns.md](dp_patterns.md) |
| 計算量 | [complexity.md](complexity.md) |

---

## いつ使う（多い難易度: F〜H）

| 言い回し | イメージ |
|---|---|
| 「各頂点について、そこを根としたときの答え」 | 全方位 |
| 「木上で最も遠い点までの距離（各点）」 | 木の直径の親戚 |
| 部分木の情報をマージして全体を作る | マージが結合的 |

通常の木 DP は「根を1つ固定」→ 全方位は「根を全部試すのを O(N) でやる」。

---

## アルゴリズムの型（2 回 DFS）

1. **1 回目**: 適当な根で、子方向の partial（部分木の答え）を計算  
2. **2 回目**: 親方向の情報を受け取り、各頂点で「自分を根にした答え」を確定  

マージ演算 `merge` と、辺を渡すときの `add_edge` を問題ごとに定義します。

---

## 入力例・出力例つき雛形（各点からの最遠距離）

```text
【問題】木が与えられる。各頂点 v について、v から最も遠い頂点までの距離を出力。
【入力例】
4
1 2
2 3
2 4
【出力例】
2
1
2
2
```

```python
from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

# down[v] = v の部分木内での最遠距離（根=0 で計算）
down = [0] * N
parent = [-1] * N

def dfs1(v, p):
    parent[v] = p
    best = 0
    for to in g[v]:
        if to == p:
            continue
        dfs1(to, v)
        best = max(best, down[to] + 1)
    down[v] = best

dfs1(0, -1)

# ans[v] = v を根にしたときの最遠距離
ans = [0] * N

def dfs2(v, p, up):
    # 子方向の down と親方向の up を並べて最大を取る
    childs = []
    for to in g[v]:
        if to == p:
            continue
        childs.append(down[to] + 1)
    # v の答え
    cand = childs + ([up] if p != -1 else [])
    ans[v] = max(cand) if cand else 0

    # 各子へ渡す up を計算（自分以外の最大）
    # pref/suf で「その子以外の max」
    m = len(childs)
    pref = [0] * (m + 1)
    suf = [0] * (m + 1)
    for i in range(m):
        pref[i + 1] = max(pref[i], childs[i])
    for i in range(m - 1, -1, -1):
        suf[i] = max(suf[i + 1], childs[i])

    idx = 0
    for to in g[v]:
        if to == p:
            continue
        other = max(pref[idx], suf[idx + 1])
        if p != -1:
            other = max(other, up)
        dfs2(to, v, other + 1)
        idx += 1

dfs2(0, -1, 0)
print(*ans)
```

【どこを変えるか】
- 「最遠」以外なら `down` の意味とマージを問題に合わせる
- 辺に重みがあるなら `+1` を重みに変える
- 一般化ライブラリが欲しければ「マージがモノイド」前提の全方位テンプレを別途用意

---

## チェックリスト

1. まず根付き木 DP が書けるか  
2. マージが順序に依存しない（結合的）か  
3. 親方向の情報を子へ渡すとき、**自分自身の寄与を二重に足していないか**  
