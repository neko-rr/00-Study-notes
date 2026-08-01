"""
【強連結成分分解（SCC）】Kosaraju
多い難易度: ABC F〜H
適する問題:
  - 「互いに行き来できる頂点のかたまり」
  - 有向グラフを DAG に縮約してから DP
  - 「閉じたグループの個数」など
キーワード: SCC, 強連結, 縮約, Kosaraju
計算量: O(N + M)
関連: lib/twosat.py（内部で SCC を使う）, graph_terms.md
"""

from typing import List, Tuple


def scc(n: int, edges: List[Tuple[int, int]]) -> Tuple[int, List[int]]:
    """
    有向グラフの強連結成分分解。
    戻り値: (成分数 k, ids)
      ids[v] = 頂点 v の成分番号（トポ順で 0..k-1）
    """
    if n < 0:
        raise ValueError("n は 0 以上")
    g = [[] for _ in range(n)]
    rg = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        rg[v].append(u)

    visited = [False] * n
    order = []

    def dfs(v: int) -> None:
        visited[v] = True
        for to in g[v]:
            if not visited[to]:
                dfs(to)
        order.append(v)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    ids = [-1] * n
    k = 0

    def rdfs(v: int, comp: int) -> None:
        ids[v] = comp
        for to in rg[v]:
            if ids[to] < 0:
                rdfs(to, comp)

    for v in reversed(order):
        if ids[v] < 0:
            rdfs(v, k)
            k += 1
    return k, ids


def scc_groups(n: int, edges: List[Tuple[int, int]]) -> List[List[int]]:
    """各強連結成分の頂点一覧（成分番号の昇順）"""
    k, ids = scc(n, edges)
    groups = [[] for _ in range(k)]
    for v in range(n):
        groups[ids[v]].append(v)
    return groups


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】有向グラフの強連結成分の個数を求めよ。
# 【入力】
#   N M
#   辺 M 行: u v （1-index, u→v）
# 【入力例】
# 4 4
# 1 2
# 2 3
# 3 1
# 3 4
# 【出力例】
# 2
# （{1,2,3} と {4}）
# 【どこを変えるか】
#   - 縮約後の DAG で DP するなら ids[u] → ids[v] の辺を作る
#   - 成分内の頂点数は groups の長さを見る
# ============================================================
if __name__ == "__main__":
    from io import StringIO
    import sys

    demo = """4 4
1 2
2 3
3 1
3 4
"""
    sys.stdin = StringIO(demo)
    input = sys.stdin.readline

    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v = map(int, input().split())
        edges.append((u - 1, v - 1))
    k, ids = scc(N, edges)
    print(k)
    assert k == 2
    print("scc.py OK")
