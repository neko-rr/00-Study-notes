"""
【二分探索・めぐる式】
多い難易度: ABC C〜E（答えの二分探索は D〜E で特に多い）
適する問題:
  - 「条件を満たす最小／最大の X を求めよ」
  - 答え X を決めると「できる／できない」が単調に分かれる
キーワード: 最小の〜、最大の〜、単調性、めぐる式、境界
"""

from typing import Callable, List
from bisect import bisect_left, bisect_right


def meguru_bisect(ok: int, ng: int, is_ok: Callable[[int], bool]) -> int:
    """めぐる式二分探索。is_ok(x) が True になる境界の ok 側を返す。"""
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


def lower_bound(a: List[int], x: int) -> int:
    return bisect_left(a, x)


def upper_bound(a: List[int], x: int) -> int:
    return bisect_right(a, x)


def count_range(a: List[int], left: int, right: int) -> int:
    """ソート済み a で left <= 値 < right の個数"""
    return bisect_left(a, right) - bisect_left(a, left)


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】正整数 X のうち、X*X >= N を満たす最小の X を求めよ。
# 【入力】
#   N
# 【入力例】
# 30
# 【出力例】
# 6
# （理由: 5*5=25 < 30、6*6=36 >= 30）
# 【どこを変えるか】
#   - is_ok(x) の中身を「その問題の判定」に書き換える
#   - 「最大の X」なら ok/ng の初期値を入れ替え、単調性の向きに注意
#   - 配列上の位置探しなら lower_bound / count_range を使う
# ============================================================
if __name__ == "__main__":
    from io import StringIO
    import sys

    demo = """30
"""
    sys.stdin = StringIO(demo)
    input = sys.stdin.readline

    N = int(input())
    ans = meguru_bisect(ok=10**9, ng=0, is_ok=lambda x: x * x >= N)
    print(ans)
    assert ans == 6

    a = [1, 3, 3, 5, 7]
    assert lower_bound(a, 3) == 1
    assert count_range(a, 3, 6) == 3
    print("binary_search.py OK")
