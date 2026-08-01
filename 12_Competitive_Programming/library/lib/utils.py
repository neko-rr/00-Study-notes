"""
【ユーティリティ】累積和・座標圧縮・ヒープ・二次元累積和
多い難易度: ABC C〜D（二次元累積和は D〜E も）
適する問題:
  - 「区間 [L,R] の和を何度も聞く」→ 累積和
  - 「座標の値が 10^9 と大きいが、実際の点は少ない」→ 座標圧縮
  - 「毎回いちばん小さい／大きいものを取り出す」→ heapq
  - 「長方形領域の和を何度も聞く」→ 二次元累積和
"""

from typing import List, Tuple
import heapq


# ============================================================
# 累積和（1次元）
# ============================================================
class PrefixSum:
    """
    配列 A の区間和を O(1) で答える。
    計算量: 前計算 O(N), クエリ O(1)
    """

    def __init__(self, a: List[int]):
        # S[i] = A[0] + ... + A[i-1]
        self.S = [0]
        for x in a:
            self.S.append(self.S[-1] + x)

    def range_sum(self, l: int, r: int) -> int:
        """半開区間 [l, r) の和"""
        return self.S[r] - self.S[l]


# ============================================================
# 二次元累積和
# ============================================================
class PrefixSum2D:
    """
    グリッドの長方形和を O(1) で答える。
    計算量: 前計算 O(HW), クエリ O(1)
    """

    def __init__(self, grid: List[List[int]]):
        if not grid or not grid[0]:
            self.H = self.W = 0
            self.S = [[0]]
            return
        self.H = len(grid)
        self.W = len(grid[0])
        # S[i][j] = (0,0)〜(i-1,j-1) の長方形和
        self.S = [[0] * (self.W + 1) for _ in range(self.H + 1)]
        for i in range(self.H):
            for j in range(self.W):
                self.S[i + 1][j + 1] = (
                    self.S[i][j + 1]
                    + self.S[i + 1][j]
                    - self.S[i][j]
                    + grid[i][j]
                )

    def range_sum(self, r1: int, c1: int, r2: int, c2: int) -> int:
        """半開長方形 [r1,r2) x [c1,c2) の和"""
        return (
            self.S[r2][c2]
            - self.S[r1][c2]
            - self.S[r2][c1]
            + self.S[r1][c1]
        )


# ============================================================
# 座標圧縮
# ============================================================
def compress(values: List[int]) -> Tuple[List[int], List[int]]:
    """
    大きい座標を 0,1,2,... に詰め直す。
    戻り値: (圧縮後の配列, ソート済みユニーク値)
    例: [100, 1, 50, 100] → ([2, 0, 1, 2], [1, 50, 100])
    """
    uniq = sorted(set(values))
    rank = {v: i for i, v in enumerate(uniq)}
    return [rank[v] for v in values], uniq


# ============================================================
# ヒープ（優先度付きキュー）の使い方メモ
# ============================================================
def heap_examples():
    """
    heapq は最小ヒープ。最大ヒープにしたいときは符号を反転する。
    適する問題: 「常に最小コストを選ぶ」「Dijkstra」「スケジューリング」
    """
    # 最小ヒープ
    h = []
    heapq.heappush(h, 3)
    heapq.heappush(h, 1)
    heapq.heappush(h, 2)
    # heapq.heappop(h) → 1, 2, 3 の順

    # 最大ヒープ（符号反転）
    hmax = []
    heapq.heappush(hmax, -3)
    heapq.heappush(hmax, -1)
    # -heapq.heappop(hmax) → 3


# ============================================================
# 使用例（実行確認用）
# ============================================================
if __name__ == "__main__":
    ps = PrefixSum([1, 2, 3, 4])
    assert ps.range_sum(1, 3) == 5  # 2+3

    g = [[1, 2], [3, 4]]
    ps2 = PrefixSum2D(g)
    assert ps2.range_sum(0, 0, 2, 2) == 10

    comp, uniq = compress([100, 1, 50, 100])
    assert comp == [2, 0, 1, 2]
    assert uniq == [1, 50, 100]
    print("utils.py OK")
