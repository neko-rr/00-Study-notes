"""
【グラフアルゴリズム】BFS / Dijkstra / トポソ / Floyd / Bellman-Ford / 橋
多い難易度: ABC C〜H
適する問題:
  - 「最短手数」→ BFS
  - 「重み付き最短路（非負）」→ Dijkstra
  - 「負の辺がある最短路」→ Bellman-Ford
  - 「全点対最短路（N≤400）」→ Floyd-Warshall
  - 「依存関係を守って並べる」→ トポロジカルソート
  - 「橋（抜くと連結性が増える辺）」→ bridges
関連: lib/scc.py, lib/lca.py, lib/maxflow.py, graph_terms.md
"""

from typing import List, Optional, Tuple
from collections import deque
import heapq

INF = 10**18


def bfs_shortest(n: int, edges: List[Tuple[int, int]], start: int) -> List[int]:
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    dist = [-1] * n
    dist[start] = 0
    q = deque([start])
    while q:
        v = q.popleft()
        for to in g[v]:
            if dist[to] == -1:
                dist[to] = dist[v] + 1
                q.append(to)
    return dist


def bfs_grid(H: int, W: int, grid: List[str], sy: int, sx: int, wall: str = "#") -> List[List[int]]:
    dist = [[-1] * W for _ in range(H)]
    if grid[sy][sx] == wall:
        return dist
    dist[sy][sx] = 0
    q = deque([(sy, sx)])
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while q:
        y, x = q.popleft()
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] != wall and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))
    return dist


def dijkstra(n: int, graph: List[List[Tuple[int, int]]], start: int) -> List[int]:
    dist = [INF] * n
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        d, v = heapq.heappop(hq)
        if d > dist[v]:
            continue
        for to, cost in graph[v]:
            nd = d + cost
            if nd < dist[to]:
                dist[to] = nd
                heapq.heappush(hq, (nd, to))
    return dist


def topological_sort(n: int, edges: List[Tuple[int, int]]) -> Optional[List[int]]:
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for to in g[v]:
            indeg[to] -= 1
            if indeg[to] == 0:
                q.append(to)
    if len(order) != n:
        return None
    return order


def bellman_ford(
    n: int, edges: List[Tuple[int, int, int]], start: int
) -> Tuple[Optional[List[int]], bool]:
    """
    辺リスト (u,v,cost)。負辺OK。
    戻り値: (dist, has_negative_cycle_reachable)
      負閉路が start から到達可能なら dist=None, True
    """
    dist = [INF] * n
    dist[start] = 0
    for i in range(n):
        updated = False
        for u, v, c in edges:
            if dist[u] == INF:
                continue
            nd = dist[u] + c
            if nd < dist[v]:
                dist[v] = nd
                updated = True
                if i == n - 1:
                    return None, True
        if not updated:
            break
    return dist, False


def floyd_warshall(n: int, edges: List[Tuple[int, int, int]]) -> List[List[int]]:
    """
    全点対最短路。辺 (u,v,cost)。無向なら両方向を渡す。
    到達不能は INF。N≤400 目安。
    """
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, c in edges:
        if c < dist[u][v]:
            dist[u][v] = c
    for k in range(n):
        dk = dist[k]
        for i in range(n):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(n):
                cand = dik + dk[j]
                if cand < di[j]:
                    di[j] = cand
    return dist


def bridges(n: int, edges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    無向グラフの橋（取り除くと連結成分が増える辺）を列挙。
    戻り値の辺は u < v に正規化。
    """
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    order = [-1] * n
    low = [0] * n
    k = 0
    res = []

    def dfs(v: int, p: int) -> None:
        nonlocal k
        order[v] = low[v] = k
        k += 1
        for to in g[v]:
            if to == p:
                continue
            if order[to] == -1:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > order[v]:
                    res.append((v, to) if v < to else (to, v))
            else:
                low[v] = min(low[v], order[to])

    for i in range(n):
        if order[i] == -1:
            dfs(i, -1)
    return res


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】無向グラフ。頂点 1 から各頂点への最短手数を出力。
# 【入力例】
# 4 3
# 1 2
# 2 3
# 1 4
# 【出力例】
# 0 1 2 1
# 【どこを変えるか】
#   - 重み付き非負 → dijkstra
#   - 負の辺 → bellman_ford
#   - 全点対・N小さい → floyd_warshall
#   - 橋の列挙 → bridges
# ============================================================
if __name__ == "__main__":
    from io import StringIO
    import sys

    demo = """4 3
1 2
2 3
1 4
"""
    sys.stdin = StringIO(demo)
    input = sys.stdin.readline

    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v = map(int, input().split())
        edges.append((u - 1, v - 1))
    dist = bfs_shortest(N, edges, 0)
    print(*dist)
    assert dist == [0, 1, 2, 1]

    g = [[] for _ in range(3)]
    g[0].append((1, 2))
    g[0].append((2, 5))
    g[1].append((2, 1))
    assert dijkstra(3, g, 0) == [0, 2, 3]
    assert topological_sort(3, [(0, 1), (1, 2)]) == [0, 1, 2]

    bf, neg = bellman_ford(3, [(0, 1, 2), (1, 2, -1), (0, 2, 4)], 0)
    assert neg is False and bf == [0, 2, 1]
    fw = floyd_warshall(3, [(0, 1, 2), (1, 0, 2), (1, 2, 1), (2, 1, 1), (0, 2, 5), (2, 0, 5)])
    assert fw[0][2] == 3
    assert bridges(4, [(0, 1), (1, 2), (2, 0), (1, 3)]) == [(1, 3)]
    print("graph.py OK")
