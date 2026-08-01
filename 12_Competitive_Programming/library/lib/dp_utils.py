"""
【典型 DP の雛形】
多い難易度: ABC C〜E（bit DP・区間 DP は E 寄り）
適する問題:
  - 「重さの上限 W までで価値を最大化」→ ナップサック
  - 「合計をちょうど K にできるか」→ 部分和 DP
  - 「区間を分割してコスト最小」→ 区間 DP
  - 「訪問集合をビットで持つ」→ bit DP（N≤20）
キーワード: DP, ナップサック, 部分和, 区間DP, bit DP
"""

from typing import List


INF = 10**18


def knapsack_01(weights: List[int], values: List[int], W: int) -> int:
    """
    0-1 ナップサック: 各品物は高々1個。
    計算量: O(N * W)
    W が大きすぎる（例: 10^9）ときは使えない → 価値側 DP や二分探索を検討
    """
    n = len(weights)
    if n != len(values) or W < 0:
        return 0
    dp = [0] * (W + 1)
    for i in range(n):
        w, v = weights[i], values[i]
        for j in range(W, w - 1, -1):
            cand = dp[j - w] + v
            if cand > dp[j]:
                dp[j] = cand
    return dp[W]


def knapsack_unbounded(weights: List[int], values: List[int], W: int) -> int:
    """
    個数制限なしナップサック。
    計算量: O(N * W)
    """
    n = len(weights)
    if n != len(values) or W < 0:
        return 0
    dp = [0] * (W + 1)
    for i in range(n):
        w, v = weights[i], values[i]
        for j in range(w, W + 1):
            cand = dp[j - w] + v
            if cand > dp[j]:
                dp[j] = cand
    return dp[W]


def subset_sum_possible(a: List[int], K: int) -> bool:
    """
    部分集合の和をちょうど K にできるか。
    計算量: O(N * K)
    """
    if K < 0:
        return False
    dp = [False] * (K + 1)
    dp[0] = True
    for x in a:
        for s in range(K, x - 1, -1):
            if dp[s - x]:
                dp[s] = True
    return dp[K]


def lis_length(a: List[int]) -> int:
    """
    最長増加部分列（狭義）の長さ。O(N log N)
    多い難易度: D〜E
    """
    import bisect

    tails: List[int] = []
    for x in a:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def interval_dp_example(cost: List[List[int]]) -> int:
    """
    区間 DP の形の例（区間を結合する最小コスト）。
    cost[l][r] は区間 [l,r) をまとめるときの追加コスト、という想定の雛形。
    実際の問題では遷移式を問題に合わせて書き換える。
    計算量: O(N^3)
    """
    n = len(cost)
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i][i + 1] = 0
    for length in range(2, n + 1):
        for l in range(0, n - length + 1):
            r = l + length
            best = INF
            for m in range(l + 1, r):
                best = min(best, dp[l][m] + dp[m][r] + cost[l][r - 1])
            dp[l][r] = best
    return dp[0][n]


# ============================================================
# 使用例
# ============================================================
if __name__ == "__main__":
    assert knapsack_01([2, 3, 4], [3, 4, 5], 5) == 7  # 2+3
    assert knapsack_unbounded([2, 3], [3, 4], 5) == 7
    assert subset_sum_possible([1, 2, 4], 6) is True
    assert lis_length([1, 3, 2, 4]) == 3
    print("dp_utils.py OK")
