"""
【典型 DP の雛形】
多い難易度: ABC C〜E
適する問題:
  - 「重さの上限 W までで価値を最大化」→ ナップサック
  - 「合計をちょうど K にできるか」→ 部分和 DP
キーワード: DP, ナップサック, 部分和, 区間DP, bit DP
"""

from typing import List

INF = 10**18


def knapsack_01(weights: List[int], values: List[int], W: int) -> int:
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
    import bisect

    tails: List[int] = []
    for x in a:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】品物 N 個。重さ w_i・価値 v_i。容量 W で価値の最大は？
#         （各品物は高々1個）
# 【入力】
#   N W
#   w1 v1
#   ...
#   wN vN
# 【入力例】
# 3 5
# 2 3
# 3 4
# 4 5
# 【出力例】
# 7
# （重さ2+3、価値3+4）
# 【どこを変えるか】
#   - 何個でも使える → knapsack_unbounded
#   - 「できるか」だけ → subset_sum_possible
#   - W が大きすぎる（10^9）→ 別方針（価値側DP・二分探索など）
# ============================================================
if __name__ == "__main__":
    from io import StringIO
    import sys

    demo = """3 5
2 3
3 4
4 5
"""
    sys.stdin = StringIO(demo)
    input = sys.stdin.readline

    N, W = map(int, input().split())
    weights, values = [], []
    for _ in range(N):
        w, v = map(int, input().split())
        weights.append(w)
        values.append(v)
    ans = knapsack_01(weights, values, W)
    print(ans)
    assert ans == 7
    assert subset_sum_possible([1, 2, 4], 6) is True
    assert lis_length([1, 3, 2, 4]) == 3
    print("dp_utils.py OK")
