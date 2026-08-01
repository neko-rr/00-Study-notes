"""
【遅延評価セグメント木（Lazy Segment Tree）】
多い難易度: ABC E〜F（標準セグ木で足りないとき）
適する問題:
  - 「区間に一括で加算／代入」しつつ「区間の和／min／max」を聞く
  - 点更新だけでは間に合わない区間更新クエリ
キーワード: 区間加算, 区間更新, 遅延評価, 作用素, モノイド
計算量: 構築 O(N), 区間更新・区間取得 O(log N)

よくある組み合わせ（下に便利クラスあり）:
  - 区間加算 + 区間和
  - 区間加算 + 区間最小
"""

from typing import Callable, Generic, List, TypeVar

S = TypeVar("S")
F = TypeVar("F")


class LazySegTree(Generic[S, F]):
    """
    ACL 互換に近い汎用遅延セグ木。

    引数:
      op(s, t)     : 区間のマージ
      e()          : 単位元
      mapping(f,s) : 作用 f をデータ s に適用
      composition(f,g): 作用の合成（f を後から適用）
      id()         : 作用の単位元
    """

    def __init__(
        self,
        v: List[S],
        op: Callable[[S, S], S],
        e: Callable[[], S],
        mapping: Callable[[F, S], S],
        composition: Callable[[F, F], F],
        id_: Callable[[], F],
    ):
        n = len(v)
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_
        self._n = n
        size = 1
        log = 0
        while size < n:
            size <<= 1
            log += 1
        self._size = size
        self._log = log
        self.d: List[S] = [e() for _ in range(2 * size)]
        self.lz: List[F] = [id_() for _ in range(size)]
        for i in range(n):
            self.d[size + i] = v[i]
        for i in range(size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: S) -> None:
        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self.d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> S:
        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self.d[p]

    def prod(self, l: int, r: int) -> S:
        """半開区間 [l, r)"""
        if l == r:
            return self._e()
        l += self._size
        r += self._size
        for i in range(self._log, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push((r - 1) >> i)
        sml = self._e()
        smr = self._e()
        while l < r:
            if l & 1:
                sml = self._op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self.d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)

    def apply(self, l: int, r: int, f: F) -> None:
        """半開区間 [l, r) に作用 f を適用"""
        if l == r:
            return
        l += self._size
        r += self._size
        for i in range(self._log, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push((r - 1) >> i)
        l2, r2 = l, r
        while l < r:
            if l & 1:
                self._all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self._all_apply(r, f)
            l >>= 1
            r >>= 1
        l, r = l2, r2
        for i in range(1, self._log + 1):
            if ((l >> i) << i) != l:
                self._update(l >> i)
            if ((r >> i) << i) != r:
                self._update((r - 1) >> i)

    def _update(self, k: int) -> None:
        self.d[k] = self._op(self.d[2 * k], self.d[2 * k + 1])

    def _all_apply(self, k: int, f: F) -> None:
        self.d[k] = self._mapping(f, self.d[k])
        if k < self._size:
            self.lz[k] = self._composition(f, self.lz[k])

    def _push(self, k: int) -> None:
        self._all_apply(2 * k, self.lz[k])
        self._all_apply(2 * k + 1, self.lz[k])
        self.lz[k] = self._id()


# ------------------------------------------------------------
# 便利: 区間加算 + 区間和
# データ S = (和, 長さ), 作用 F = 加算値
# ------------------------------------------------------------
def make_range_add_range_sum(a: List[int]) -> LazySegTree:
    INF_ID = 0  # 加算の単位元は 0

    def op(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def e():
        return (0, 0)

    def mapping(f, x):
        return (x[0] + f * x[1], x[1])

    def composition(f, g):
        return f + g

    def id_():
        return INF_ID

    v = [(val, 1) for val in a]
    return LazySegTree(v, op, e, mapping, composition, id_)


# ------------------------------------------------------------
# 便利: 区間加算 + 区間最小
# ------------------------------------------------------------
def make_range_add_range_min(a: List[int]) -> LazySegTree:
    INF = 10**18

    def op(x, y):
        return x if x < y else y

    def e():
        return INF

    def mapping(f, x):
        return x + f

    def composition(f, g):
        return f + g

    def id_():
        return 0

    return LazySegTree(a[:], op, e, mapping, composition, id_)


# ============================================================
# 使用例
# ============================================================
if __name__ == "__main__":
    st = make_range_add_range_sum([1, 2, 3, 4])
    st.apply(1, 3, 10)  # [1, 12, 13, 4]
    assert st.prod(0, 4)[0] == 30
    assert st.prod(1, 3)[0] == 25

    st2 = make_range_add_range_min([5, 1, 4, 2])
    st2.apply(0, 2, 3)  # [8, 4, 4, 2]
    assert st2.prod(0, 4) == 2
    print("lazy_segtree.py OK")
