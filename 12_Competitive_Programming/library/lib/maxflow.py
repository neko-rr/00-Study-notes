"""
【最大流（Dinic 法）・最小カット】
多い難易度: ABC E〜H（F 以降で本領）
適する問題:
  - 「始点から終点へ最大でどれだけ流せるか」
  - 二部マッチング
関連: lib/mincostflow.py, graph_terms.md
"""

from typing import List, Optional, Tuple
from collections import deque


class MaxFlow:
    class Edge:
        __slots__ = ("to", "rev", "cap")

        def __init__(self, to: int, rev: int, cap: int):
            self.to = to
            self.rev = rev
            self.cap = cap

    def __init__(self, n: int):
        if n < 0:
            raise ValueError("n は 0 以上")
        self.n = n
        self.g: List[List[MaxFlow.Edge]] = [[] for _ in range(n)]

    def add_edge(self, fr: int, to: int, cap: int) -> int:
        if cap < 0:
            raise ValueError("容量は 0 以上")
        forward = MaxFlow.Edge(to, len(self.g[to]), cap)
        backward = MaxFlow.Edge(fr, len(self.g[fr]), 0)
        self.g[fr].append(forward)
        self.g[to].append(backward)
        return len(self.g[fr]) - 1

    def max_flow(self, s: int, t: int, flow_limit: Optional[int] = None) -> int:
        if s == t:
            return 0
        if flow_limit is None:
            flow_limit = 10**18
        flow = 0
        while flow < flow_limit:
            level = self._bfs(s)
            if level[t] < 0:
                break
            it = [0] * self.n
            while flow < flow_limit:
                f = self._dfs(s, t, flow_limit - flow, level, it)
                if f == 0:
                    break
                flow += f
        return flow

    def _bfs(self, s: int) -> List[int]:
        level = [-1] * self.n
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for e in self.g[v]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level

    def _dfs(self, v: int, t: int, up: int, level: List[int], it: List[int]) -> int:
        if v == t:
            return up
        for i in range(it[v], len(self.g[v])):
            it[v] = i
            e = self.g[v][i]
            if e.cap > 0 and level[v] < level[e.to]:
                d = self._dfs(e.to, t, min(up, e.cap), level, it)
                if d > 0:
                    e.cap -= d
                    self.g[e.to][e.rev].cap += d
                    return d
        return 0


def bipartite_matching(n_left: int, n_right: int, edges: List[Tuple[int, int]]) -> int:
    S = 0
    left0 = 1
    right0 = 1 + n_left
    T = 1 + n_left + n_right
    mf = MaxFlow(T + 1)
    for i in range(n_left):
        mf.add_edge(S, left0 + i, 1)
    for i in range(n_right):
        mf.add_edge(right0 + i, T, 1)
    for u, v in edges:
        mf.add_edge(left0 + u, right0 + v, 1)
    return mf.max_flow(S, T)


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】左 N 人・右 M 仕事。応募の辺が K 本。最大マッチング数は？
# 【入力】
#   N M K
#   辺 K 行: a b （左 a・右 b、1-index）
# 【入力例】
# 2 2 3
# 1 1
# 1 2
# 2 2
# 【出力例】
# 2
# 【どこを変えるか】
#   - 一般の最大流なら MaxFlow に自分で辺を張る（下のコメント）
#   - 頂点番号・S/T の置き方を問題のモデルに合わせる
# ============================================================
if __name__ == "__main__":
    from io import StringIO
    import sys

    demo = """2 2 3
1 1
1 2
2 2
"""
    sys.stdin = StringIO(demo)
    input = sys.stdin.readline

    N, M, K = map(int, input().split())
    edges = []
    for _ in range(K):
        a, b = map(int, input().split())
        edges.append((a - 1, b - 1))
    ans = bipartite_matching(N, M, edges)
    print(ans)
    assert ans == 2

    # 一般最大流の小さな例
    mf = MaxFlow(4)
    mf.add_edge(0, 1, 3)
    mf.add_edge(0, 2, 2)
    mf.add_edge(1, 2, 1)
    mf.add_edge(1, 3, 2)
    mf.add_edge(2, 3, 3)
    assert mf.max_flow(0, 3) == 5
    print("maxflow.py OK")
