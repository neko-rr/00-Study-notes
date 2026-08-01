"""
【グラフアルゴリズム】BFS / DFS / Dijkstra / トポロジカルソート
多い難易度: ABC C〜E（Dijkstra・トポソは D〜E）
適する問題:
  - 「最短手数で到達できるか／何手？」→ BFS（辺の重みがすべて1）
  - 「重み付き最短路」→ Dijkstra（負の辺なし）
  - 「依存関係を守って並べる／サイクルがあるか」→ トポロジカルソート
  - 連結判定・木の探索 → DFS/BFS
キーワード: 最短路, 迷路, グリッド, DAG, 依存関係
"""

from typing import List, Optional, Tuple
from collections import deque
import heapq

INF = 10**18


def bfs_shortest(n: int, edges: List[Tuple[int, int]], start: int) -> List[int]:
    """
    重みなし（または重み1）無向グラフの最短距離。
    edges: (u, v) のリスト（0-index）
    計算量: O(N + M)
    """
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
    """
    グリッド上の最短手数（上下左右）。
    grid[y][x] == wall は壁。
    計算量: O(HW)
    """
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
    """
    ダイクストラ法。graph[v] = [(to, cost), ...]
    負の辺があると使えない。
    計算量: O((N+M) log N)
    """
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
    """
    有向グラフのトポロジカルソート。
    サイクルがあれば None。
    計算量: O(N + M)
    """
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


# ============================================================
# 使用例
# ============================================================
if __name__ == "__main__":
    dist = bfs_shortest(4, [(0, 1), (1, 2), (0, 3)], 0)
    assert dist == [0, 1, 2, 1]

    g = [[] for _ in range(3)]
    g[0].append((1, 2))
    g[0].append((2, 5))
    g[1].append((2, 1))
    d = dijkstra(3, g, 0)
    assert d == [0, 2, 3]

    order = topological_sort(3, [(0, 1), (1, 2)])
    assert order == [0, 1, 2]
    assert topological_sort(2, [(0, 1), (1, 0)]) is None
    print("graph.py OK")
