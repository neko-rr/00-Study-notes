"""
【最小費用流（Min Cost Flow）】ベルマンフォード版（負辺対応・実装重視）
多い難易度: ABC F〜H
適する問題:
  - 「流量をちょうど F 流すときの最小コスト」
  - 「割当問題でコスト最小」
キーワード: 最小費用流, MCF, 割当
計算量: だいたい O(F * N * M)（流量・グラフ次第）
注意: N,M,F が大きいと厳しい。ポテンシャル付き Dijkstra 版が必要な場合あり
関連: lib/maxflow.py
"""

from typing import List, Optional, Tuple

INF = 10**18


class MinCostFlow:
    class Edge:
        __slots__ = ("to", "rev", "cap", "cost")

        def __init__(self, to: int, rev: int, cap: int, cost: int):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.cost = cost

    def __init__(self, n: int):
        if n < 0:
            raise ValueError("n は 0 以上")
        self.n = n
        self.g: List[List[MinCostFlow.Edge]] = [[] for _ in range(n)]

    def add_edge(self, fr: int, to: int, cap: int, cost: int) -> None:
        forward = MinCostFlow.Edge(to, len(self.g[to]), cap, cost)
        backward = MinCostFlow.Edge(fr, len(self.g[fr]), 0, -cost)
        self.g[fr].append(forward)
        self.g[to].append(backward)

    def flow(self, s: int, t: int, flow_limit: int) -> Tuple[int, int]:
        """
        s→t に最大 flow_limit まで流す。
        戻り値: (実際の流量, 総コスト)
        """
        if flow_limit < 0:
            raise ValueError("flow_limit は 0 以上")
        res_flow = 0
        res_cost = 0
        prev_v = [-1] * self.n
        prev_e = [-1] * self.n

        while res_flow < flow_limit:
            dist = [INF] * self.n
            dist[s] = 0
            update = True
            # ベルマンフォード（負辺対応）
            while update:
                update = False
                for v in range(self.n):
                    if dist[v] == INF:
                        continue
                    for i, e in enumerate(self.g[v]):
                        if e.cap > 0 and dist[e.to] > dist[v] + e.cost:
                            dist[e.to] = dist[v] + e.cost
                            prev_v[e.to] = v
                            prev_e[e.to] = i
                            update = True
            if dist[t] == INF:
                break

            add = flow_limit - res_flow
            v = t
            while v != s:
                e = self.g[prev_v[v]][prev_e[v]]
                add = min(add, e.cap)
                v = prev_v[v]

            v = t
            while v != s:
                e = self.g[prev_v[v]][prev_e[v]]
                e.cap -= add
                self.g[v][e.rev].cap += add
                v = prev_v[v]

            res_flow += add
            res_cost += add * dist[t]
        return res_flow, res_cost


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】左2人・右2仕事。各応募にコスト。ちょうど2人割り当てる最小コストは？
#        （割当を最小費用流で解く典型）
# 【入力】（このデモは辺をコード内で固定）
# 【入力例】なし（固定グラフ）
# 【モデル】
#   S→左(cap1,cost0), 左→右(cap1,cost=c), 右→T(cap1,cost0)
# 【出力例】
# 6
# （L2→R1 コスト2 + L1→R2 コスト4）
# 【どこを変えるか】
#   - 流量を変えたい → flow(s,t, F)
#   - 辺の張り方を問題のモデルに合わせる
# ============================================================
if __name__ == "__main__":
    # S=0, L1=1, L2=2, R1=3, R2=4, T=5
    mcf = MinCostFlow(6)
    S, T = 0, 5
    mcf.add_edge(S, 1, 1, 0)
    mcf.add_edge(S, 2, 1, 0)
    mcf.add_edge(1, 3, 1, 3)
    mcf.add_edge(1, 4, 1, 4)
    mcf.add_edge(2, 3, 1, 2)
    mcf.add_edge(2, 4, 1, 5)
    mcf.add_edge(3, T, 1, 0)
    mcf.add_edge(4, T, 1, 0)
    flow, cost = mcf.flow(S, T, 2)
    print(cost)
    assert flow == 2 and cost == 6  # 2→3(2) + 1→4(4)
    print("mincostflow.py OK")
