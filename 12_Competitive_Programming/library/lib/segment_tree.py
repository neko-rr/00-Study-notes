"""
【セグメント木（点更新・区間取得）】
多い難易度: ABC D〜E
適する問題:
  - 「1点の値を更新」しつつ「区間の min / max / 和」を聞く
キーワード: 区間最小, 区間最大, 区間和, 点更新, RMQ
計算量: 構築 O(N), 更新・クエリ O(log N)
"""

from typing import Callable, List, TypeVar

T = TypeVar("T")


class SegmentTree:
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
        i += self.size
        self.data[i] = x
        while i > 1:
            i >>= 1
            self.data[i] = self.op(self.data[2 * i], self.data[2 * i + 1])

    def get(self, i: int) -> T:
        return self.data[i + self.size]

    def prod(self, l: int, r: int) -> T:
        """半開区間 [l, r)"""
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
    INF = 10**18
    return SegmentTree.from_list(a, min, INF)


def make_rsq(a: List[int]) -> SegmentTree:
    return SegmentTree.from_list(a, lambda x, y: x + y, 0)


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】長さ N の数列。クエリは2種類。
#   1 i x : A_i を x に変更（1-index）
#   2 L R : 区間 [L,R] の最小値（1-index 閉区間）
# 【入力】
#   N Q
#   A1 ... AN
#   クエリ Q 行
# 【入力例】
# 5 3
# 3 1 4 1 5
# 2 1 3
# 1 2 10
# 2 1 3
# 【出力例】
# 1
# 3
# 【どこを変えるか】
#   - 区間和なら make_rsq / op=加算, e=0
#   - 区間最大なら max と e=-INF
#   - 区間更新が必要なら lazy_segtree.py
# ============================================================
if __name__ == "__main__":
    from io import StringIO
    import sys

    demo = """5 3
3 1 4 1 5
2 1 3
1 2 10
2 1 3
"""
    sys.stdin = StringIO(demo)
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    st = make_rmq(A)
    out = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            _, i, x = query
            st.set(i - 1, x)
        else:
            _, L, R = query
            out.append(str(st.prod(L - 1, R)))
    print("\n".join(out))
    assert out == ["1", "3"]
    print("segment_tree.py OK")
