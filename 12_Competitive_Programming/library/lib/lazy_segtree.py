"""
【遅延評価セグメント木（Lazy Segment Tree）】
多い難易度: ABC E〜H（F 以降の定番）
適する問題:
  - 「区間に一括で加算」しつつ「区間の和／min」を聞く
キーワード: 区間加算, 区間更新, 遅延評価
計算量: 区間更新・区間取得 O(log N)
関連: data_structures_guide.md, lib/segment_tree.py
"""

from typing import Callable, Generic, List, TypeVar

S = TypeVar("S")
F = TypeVar("F")


class LazySegTree(Generic[S, F]):
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


def make_range_add_range_sum(a: List[int]) -> LazySegTree:
    def op(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def e():
        return (0, 0)

    def mapping(f, x):
        return (x[0] + f * x[1], x[1])

    def composition(f, g):
        return f + g

    def id_():
        return 0

    v = [(val, 1) for val in a]
    return LazySegTree(v, op, e, mapping, composition, id_)


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
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】長さ N の数列（初期0）。クエリ2種類。
#   1 L R x : 区間 [L,R] に +x（1-index 閉区間）
#   2 L R   : 区間 [L,R] の和
# 【入力】
#   N Q
#   クエリ Q 行
# 【入力例】
# 4 3
# 1 2 3 10
# 2 1 4
# 2 2 3
# 【出力例】
# 20
# 20
# （配列は [0,10,10,0]）
# 【どこを変えるか】
#   - 区間minが欲しい → make_range_add_range_min
#   - 初期配列が 0 でない → make_range_add_range_sum(初期A)
#   - 「区間代入」は mapping/composition を問題に合わせて書き換える
# ============================================================
if __name__ == "__main__":
    from io import StringIO
    import sys

    demo = """4 3
1 2 3 10
2 1 4
2 2 3
"""
    sys.stdin = StringIO(demo)
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    st = make_range_add_range_sum([0] * N)
    out = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            _, L, R, x = query
            st.apply(L - 1, R, x)  # 閉区間 → 半開
        else:
            _, L, R = query
            out.append(str(st.prod(L - 1, R)[0]))
    print("\n".join(out))
    assert out == ["20", "20"]
    print("lazy_segtree.py OK")
