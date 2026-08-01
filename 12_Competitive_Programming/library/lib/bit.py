"""
【bit 全探索・部分集合】
多い難易度: ABC C〜E（N≤20 前後なら D、bit DP は E も）
適する問題:
  - 「各要素を選ぶ／選ばないを全部試す」（2^N）
  - 「部分集合の和がちょうど K」
  - 「状態をビットで持つ DP」（訪問集合・使用集合）
キーワード: 全探索, 2^N, 部分集合, bit DP, N≤20
注意: N が 25 を超えると普通は間に合わない
"""

from typing import Iterable, List, Tuple


def bit_enumerate(n: int) -> Iterable[int]:
    """0 .. 2^n - 1 を列挙（各 bit が要素の採用可否）"""
    return range(1 << n)


def subset_sums(a: List[int]) -> List[int]:
    """
    全部分集合の和を返す。長さ 2^n。
    計算量: O(n * 2^n)
    """
    n = len(a)
    res = [0] * (1 << n)
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if s & bit:
                res[s] = res[s ^ bit] + a[i]
    return res


def popcount(x: int) -> int:
    """立っている bit の個数（Python 3.10+ なら x.bit_count() でも可）"""
    return bin(x).count("1")


def bits_of(mask: int, n: int) -> List[int]:
    """mask で選ばれたインデックス一覧（0-index, 長さ n まで見る）"""
    return [i for i in range(n) if mask >> i & 1]


def meet_in_the_middle(a: List[int], k: int) -> bool:
    """
    半分全列挙: 部分集合和がちょうど k になるか。
    N≤40 くらいまで狙える典型テクニック（D〜E）。
    計算量: O(2^(N/2) * N)
    """
    n = len(a)
    left = a[: n // 2]
    right = a[n // 2 :]
    L = sorted(set(subset_sums(left)))
    R = set(subset_sums(right))
    for x in L:
        if k - x in R:
            return True
    return False


# ============================================================
# 使用例
# ============================================================
if __name__ == "__main__":
    a = [1, 2, 4]
    sums = subset_sums(a)
    assert sorted(sums) == [0, 1, 2, 3, 4, 5, 6, 7]
    assert meet_in_the_middle([1, 3, 5, 7], 8) is True
    assert meet_in_the_middle([1, 3, 5, 7], 2) is False
    print("bit.py OK")
