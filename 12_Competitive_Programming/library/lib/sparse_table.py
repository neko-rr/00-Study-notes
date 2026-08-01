"""
【Sparse Table】更新なしの区間クエリ
多い難易度: ABC E〜F（F〜H の前処理部品にも）
適する問題:
  - 配列が途中で変わらない
  - 区間の min / max / gcd を何度も聞く
キーワード: Sparse Table, RMQ, 冪等演算
計算量: 前計算 O(N log N), クエリ O(1)（min/max/gcd）
注意: 区間和には向かない（重複が困る）。和は累積和へ
関連: lib/segment_tree.py, lib/utils.py
"""

from typing import Callable, List, TypeVar

T = TypeVar("T")


class SparseTable:
    def __init__(self, a: List[T], op: Callable[[T, T], T]):
        """
        op は結合的かつ冪等（min, max, gcd など）を想定。
        """
        n = len(a)
        if n == 0:
            self.n = 0
            self.op = op
            self.st = []
            self.log = []
            return
        self.n = n
        self.op = op
        logn = n.bit_length()
        self.st: List[List[T]] = [a[:]]
        for k in range(1, logn):
            prev = self.st[k - 1]
            length = 1 << (k - 1)
            cur = []
            for i in range(n - (1 << k) + 1):
                cur.append(op(prev[i], prev[i + length]))
            self.st.append(cur)
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1

    def prod(self, l: int, r: int) -> T:
        """半開区間 [l, r) 。空区間は呼ばないこと"""
        if not (0 <= l < r <= self.n):
            raise ValueError("区間が不正")
        k = self.log[r - l]
        return self.op(self.st[k][l], self.st[k][r - (1 << k)])


def make_rmq(a: List[int]) -> SparseTable:
    return SparseTable(a, min)


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】長さ N の数列。クエリ Q 個で区間 [L,R] の最小値（1-index 閉区間）。
# 【入力】
#   N Q
#   A1 ... AN
#   クエリ Q 行: L R
# 【入力例】
# 5 3
# 3 1 4 1 5
# 1 3
# 2 5
# 3 3
# 【出力例】
# 1
# 1
# 4
# 【どこを変えるか】
#   - 区間最大 → op=max
#   - 区間 gcd → op=math.gcd
#   - 更新がある → セグ木へ
# ============================================================
if __name__ == "__main__":
    from io import StringIO
    import sys

    demo = """5 3
3 1 4 1 5
1 3
2 5
3 3
"""
    sys.stdin = StringIO(demo)
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    st = make_rmq(A)
    out = []
    for _ in range(Q):
        L, R = map(int, input().split())
        out.append(str(st.prod(L - 1, R)))
    print("\n".join(out))
    assert out == ["1", "1", "4"]
    print("sparse_table.py OK")
