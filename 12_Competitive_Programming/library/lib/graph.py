"""
【グラフアルゴリズム】BFS / DFS / Dijkstra / トポロジカルソート
多い難易度: ABC C〜E
適する問題:
  - 「最短手数」→ BFS
  - 「重み付き最短路」→ Dijkstra
  - 「依存関係を守って並べる」→ トポロジカルソート
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


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】無向グラフ。頂点 1 から各頂点への最短手数を出力。
#         到達不能は -1。
# 【入力】
#   N M
#   辺 M 行: u v （1-index）
# 【入力例】
# 4 3
# 1 2
# 2 3
# 1 4
# 【出力例】
# 0 1 2 1
# 【どこを変えるか】
#   - 辺に重みがある → dijkstra（下のコメント例）
#   - 迷路 → bfs_grid
#   - 依存関係の並べ替え → topological_sort
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
        edges.append((u - 1, v - 1))  # 0-index に変換
    dist = bfs_shortest(N, edges, 0)
    print(*dist)
    assert dist == [0, 1, 2, 1]

    # 重み付きの例（入力は省略）: g[u].append((v, cost))
    g = [[] for _ in range(3)]
    g[0].append((1, 2))
    g[0].append((2, 5))
    g[1].append((2, 1))
    assert dijkstra(3, g, 0) == [0, 2, 3]
    assert topological_sort(3, [(0, 1), (1, 2)]) == [0, 1, 2]
    print("graph.py OK")
