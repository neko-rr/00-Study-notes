"""
【二分探索・めぐる式】
多い難易度: ABC C〜E（答えの二分探索は D〜E で特に多い）
適する問題:
  - 「条件を満たす最小／最大の X を求めよ」
  - 答え X を決めると「できる／できない」が単調に分かれる
  - 配列がソート済みで「ある値以上の最初の位置」を知りたい（bisect）
キーワード: 最小の〜、最大の〜、単調性、めぐる式、境界
"""

from typing import Callable, List
from bisect import bisect_left, bisect_right


def meguru_bisect(ok: int, ng: int, is_ok: Callable[[int], bool]) -> int:
    """
    めぐる式二分探索。
    is_ok(x) が True になる境界の ok 側を返す。

    初期値の決め方:
      - 「最小の X」を求める → ok=十分大, ng=小さすぎる値
      - 「最大の X」を求める → ok=小さすぎる値, ng=十分大
        （その場合 is_ok は「X 以下なら可能」など単調になるよう定義）

    計算量: O(log |ok-ng| * is_ok のコスト)
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


def lower_bound(a: List[int], x: int) -> int:
    """ソート済み a で a[i] >= x となる最小の i（無いとき len(a)）"""
    return bisect_left(a, x)


def upper_bound(a: List[int], x: int) -> int:
    """ソート済み a で a[i] > x となる最小の i（無いとき len(a)）"""
    return bisect_right(a, x)


def count_range(a: List[int], left: int, right: int) -> int:
    """ソート済み a で left <= 値 < right の個数"""
    return bisect_left(a, right) - bisect_left(a, left)


# ============================================================
# 使用例
# ============================================================
if __name__ == "__main__":
    # 例: 「x*x >= 30 となる最小の正整数 x」
    ans = meguru_bisect(ok=10**9, ng=0, is_ok=lambda x: x * x >= 30)
    assert ans == 6

    a = [1, 3, 3, 5, 7]
    assert lower_bound(a, 3) == 1
    assert upper_bound(a, 3) == 3
    assert count_range(a, 3, 6) == 3  # 3,3,5
    print("binary_search.py OK")
