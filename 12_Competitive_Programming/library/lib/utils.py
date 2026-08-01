"""
【ユーティリティ】累積和・座標圧縮・ヒープ・二次元累積和
多い難易度: ABC C〜D（二次元累積和は D〜E も）
適する問題:
  - 「区間 [L,R] の和を何度も聞く」→ 累積和
  - 「座標の値が 10^9 と大きいが、実際の点は少ない」→ 座標圧縮
  - 「長方形領域の和を何度も聞く」→ 二次元累積和
"""

from typing import List, Tuple
import heapq


class PrefixSum:
    def __init__(self, a: List[int]):
        self.S = [0]
        for x in a:
            self.S.append(self.S[-1] + x)

    def range_sum(self, l: int, r: int) -> int:
        """半開区間 [l, r) の和"""
        return self.S[r] - self.S[l]


class PrefixSum2D:
    def __init__(self, grid: List[List[int]]):
        if not grid or not grid[0]:
            self.H = self.W = 0
            self.S = [[0]]
            return
        self.H = len(grid)
        self.W = len(grid[0])
        self.S = [[0] * (self.W + 1) for _ in range(self.H + 1)]
        for i in range(self.H):
            for j in range(self.W):
                self.S[i + 1][j + 1] = (
                    self.S[i][j + 1] + self.S[i + 1][j] - self.S[i][j] + grid[i][j]
                )

    def range_sum(self, r1: int, c1: int, r2: int, c2: int) -> int:
        """半開長方形 [r1,r2) x [c1,c2) の和"""
        return self.S[r2][c2] - self.S[r1][c2] - self.S[r2][c1] + self.S[r1][c1]


def compress(values: List[int]) -> Tuple[List[int], List[int]]:
    uniq = sorted(set(values))
    rank = {v: i for i, v in enumerate(uniq)}
    return [rank[v] for v in values], uniq


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】長さ N の数列 A。クエリ Q 個で区間和（1-index 閉区間）を答えよ。
#         ※更新はない（あるなら Fenwick）
# 【入力】
#   N Q
#   A1 ... AN
#   クエリ Q 行: L R
# 【入力例】
# 4 2
# 1 2 3 4
# 2 3
# 1 4
# 【出力例】
# 5
# 10
# 【どこを変えるか】
#   - グリッドの長方形和 → PrefixSum2D
#   - 座標が大きすぎる → compress(values)
#   - 区間加算をまとめてやる → imos_prefix.md のいもす法
# ============================================================
if __name__ == "__main__":
    from io import StringIO
    import sys

    demo = """4 2
1 2 3 4
2 3
1 4
"""
    sys.stdin = StringIO(demo)
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    ps = PrefixSum(A)
    out = []
    for _ in range(Q):
        L, R = map(int, input().split())
        out.append(str(ps.range_sum(L - 1, R)))
    print("\n".join(out))
    assert out == ["5", "10"]

    g = [[1, 2], [3, 4]]
    assert PrefixSum2D(g).range_sum(0, 0, 2, 2) == 10
    assert compress([100, 1, 50, 100])[0] == [2, 0, 1, 2]
    print("utils.py OK")
