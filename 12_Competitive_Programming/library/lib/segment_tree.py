"""
【セグメント木（点更新・区間取得）】
多い難易度: ABC D〜E
適する問題:
  - 「1点の値を更新」しつつ「区間の min / max / 和 / gcd」を聞く
  - Fenwick では書きにくい演算（min, max, gcd など）
キーワード: 区間最小, 区間最大, 区間和, 点更新, RMQ
計算量: 構築 O(N), 更新・クエリ O(log N)

使い分け:
  - 区間和だけ → Fenwick の方が短いことも多い
  - min/max/任意のモノイド → セグメント木
  - 区間への一括更新も必要 → lazy_segtree.py
"""

from typing import Callable, List, TypeVar

T = TypeVar("T")


class SegmentTree:
    """
    汎用セグ木。
    op: 結合的な二項演算（例: min, max, 加算）
    e : 単位元（例: min→INF, max→-INF, 和→0）
    """

    def __init__(self, n: int, op: Callable[[T, T], T], e: T):
        if n < 0:
            raise ValueError("n は 0 以上")
        self.op = op
        self.e = e
        self.n = n
        size = 1
        while size < n:
            size <<= 1
        self.size = size
        self.data: List[T] = [e] * (2 * size)

    @classmethod
    def from_list(cls, a: List[T], op: Callable[[T, T], T], e: T) -> "SegmentTree":
        st = cls(len(a), op, e)
        for i, v in enumerate(a):
            st.data[st.size + i] = v
        for i in range(st.size - 1, 0, -1):
            st.data[i] = op(st.data[2 * i], st.data[2 * i + 1])
        return st

    def set(self, i: int, x: T) -> None:
        """0-index 位置 i を x で上書き"""
        i += self.size
        self.data[i] = x
        while i > 1:
            i >>= 1
            self.data[i] = self.op(self.data[2 * i], self.data[2 * i + 1])

    def get(self, i: int) -> T:
        return self.data[i + self.size]

    def prod(self, l: int, r: int) -> T:
        """半開区間 [l, r) の演算結果"""
        l += self.size
        r += self.size
        left = self.e
        right = self.e
        while l < r:
            if l & 1:
                left = self.op(left, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                right = self.op(self.data[r], right)
            l >>= 1
            r >>= 1
        return self.op(left, right)

    def all_prod(self) -> T:
        return self.data[1]


def make_rmq(a: List[int]) -> SegmentTree:
    """区間最小用の便利コンストラクタ"""
    INF = 10**18
    return SegmentTree.from_list(a, min, INF)


def make_rsq(a: List[int]) -> SegmentTree:
    """区間和用の便利コンストラクタ"""
    return SegmentTree.from_list(a, lambda x, y: x + y, 0)


# ============================================================
# 使用例
# ============================================================
if __name__ == "__main__":
    st = make_rmq([3, 1, 4, 1, 5])
    assert st.prod(0, 3) == 1
    st.set(1, 10)
    assert st.prod(0, 3) == 3

    st2 = make_rsq([1, 2, 3, 4])
    assert st2.prod(1, 4) == 9
    print("segment_tree.py OK")
