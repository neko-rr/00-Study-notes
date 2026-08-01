"""
【LCA（最小共通祖先）】ダブリング
多い難易度: ABC E〜H
適する問題:
  - 「木上で頂点 u,v の距離」
  - 「u と v の共通の祖先で最も深いもの」
  - パスクエリ（辺の max など）の前処理にも応用
キーワード: LCA, ダブリング, 木, 距離
計算量: 前計算 O(N log N), クエリ O(log N)
関連: lib/graph.py, rerooting.md
"""

from typing import List, Optional, Tuple


class LCA:
    def __init__(self, n: int, root: int, edges: List[Tuple[int, int]]):
        if n <= 0:
            raise ValueError("n は 1 以上")
        self.n = n
        self.root = root
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        self.LOG = n.bit_length()
        self.parent = [[-1] * n for _ in range(self.LOG)]
        self.depth = [0] * n

        # 根からの DFS（再帰が深いと危険なのでスタック）
        stack = [root]
        parent0 = self.parent[0]
        parent0[root] = -1
        seen = [False] * n
        seen[root] = True
        while stack:
            v = stack.pop()
            for to in g[v]:
                if seen[to]:
                    continue
                seen[to] = True
                parent0[to] = v
                self.depth[to] = self.depth[v] + 1
                stack.append(to)

        for k in range(self.LOG - 1):
            for v in range(n):
                p = self.parent[k][v]
                self.parent[k + 1][v] = -1 if p < 0 else self.parent[k][p]

    def query(self, u: int, v: int) -> int:
        """u と v の LCA"""
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        # u を v と同じ深さへ
        diff = self.depth[u] - self.depth[v]
        for k in range(self.LOG):
            if diff >> k & 1:
                u = self.parent[k][u]
        if u == v:
            return u
        for k in range(self.LOG - 1, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]

    def dist(self, u: int, v: int) -> int:
        """辺の重みがすべて1のときの距離"""
        w = self.query(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[w]


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】木が与えられる。Q 個のクエリで u,v の距離を答えよ。
# 【入力】
#   N
#   辺 N-1 行: u v （1-index）
#   Q
#   クエリ Q 行: u v
# 【入力例】
# 5
# 1 2
# 1 3
# 3 4
# 3 5
# 3
# 2 4
# 4 5
# 1 5
# 【出力例】
# 3
# 2
# 2
# 【どこを変えるか】
#   - 根を変えるなら LCA(N, root, edges) の root
#   - 「LCA そのもの」が欲しいなら lca.query(u,v) を出力
# ============================================================
if __name__ == "__main__":
    from io import StringIO
    import sys

    demo = """5
1 2
1 3
3 4
3 5
3
2 4
4 5
1 5
"""
    sys.stdin = StringIO(demo)
    input = sys.stdin.readline

    N = int(input())
    edges = []
    for _ in range(N - 1):
        u, v = map(int, input().split())
        edges.append((u - 1, v - 1))
    Q = int(input())
    lca = LCA(N, 0, edges)
    out = []
    for _ in range(Q):
        u, v = map(int, input().split())
        out.append(str(lca.dist(u - 1, v - 1)))
    print("\n".join(out))
    assert out == ["3", "2", "2"]
    print("lca.py OK")
