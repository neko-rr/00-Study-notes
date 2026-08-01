"""
【bit 全探索・部分集合】
多い難易度: ABC C〜E（N≤20 前後なら D、bit DP は E も）
適する問題:
  - 「各要素を選ぶ／選ばないを全部試す」（2^N）
  - 「部分集合の和がちょうど K」
キーワード: 全探索, 2^N, 部分集合, bit DP, N≤20
"""

from typing import Iterable, List


def bit_enumerate(n: int) -> Iterable[int]:
    return range(1 << n)


def subset_sums(a: List[int]) -> List[int]:
    n = len(a)
    res = [0] * (1 << n)
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if s & bit:
                res[s] = res[s ^ bit] + a[i]
    return res


def popcount(x: int) -> int:
    return bin(x).count("1")


def bits_of(mask: int, n: int) -> List[int]:
    return [i for i in range(n) if mask >> i & 1]


def meet_in_the_middle(a: List[int], k: int) -> bool:
    n = len(a)
    left = a[: n // 2]
    right = a[n // 2 :]
    L = set(subset_sums(left))
    R = set(subset_sums(right))
    for x in L:
        if k - x in R:
            return True
    return False


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】N 個の整数 A。部分集合の和をちょうど K にできるなら Yes、否なら No。
# 【入力】
#   N K
#   A1 ... AN
# 【入力例】
# 3 5
# 1 2 4
# 【出力例】
# Yes
# （1+4=5）
# 【どこを変えるか】
#   - 「個数も最大」など条件が増えたら mask の中で追加判定
#   - N が 40 前後なら meet_in_the_middle(A, K)
#   - N≤20 を超えると基本的に間に合わない（complexity.md 参照）
# ============================================================
if __name__ == "__main__":
    from io import StringIO
    import sys

    demo = """3 5
1 2 4
"""
    sys.stdin = StringIO(demo)
    input = sys.stdin.readline

    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ok = K in set(subset_sums(A))
    print("Yes" if ok else "No")
    assert ok is True
    assert meet_in_the_middle([1, 3, 5, 7], 8) is True
    print("bit.py OK")
