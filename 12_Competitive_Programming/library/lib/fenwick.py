"""
【Fenwick Tree（Binary Indexed Tree, BIT）】
多い難易度: ABC D〜E
適する問題:
  - 「点更新（1箇所の値を変える）＋ 区間和」を何度も行う
  - 「転倒数（ペアの逆転数）を数えよ」
  - 座標圧縮とセットで「自分より小さいものが何個あるか」
キーワード: 区間和, 点更新, 転倒数, BIT, Fenwick
計算量: 更新・区間和とも O(log N)
注意: 区間への一括加算＋点取得も可能だが、区間更新＋区間和は遅延SegTree向き
"""

from typing import List


class FenwickTree:
    """
    1-index 内部実装。外部からは 0-index の add/sum を提供。
    """

    def __init__(self, n: int):
        if n < 0:
            raise ValueError("n は 0 以上")
        self.n = n
        self.data = [0] * (n + 1)

    def add(self, i: int, x: int) -> None:
        """0-index 位置 i に x を加える"""
        i += 1
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def prefix_sum(self, i: int) -> int:
        """a[0] + ... + a[i-1]（長さ i の接頭和）"""
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def range_sum(self, l: int, r: int) -> int:
        """半開区間 [l, r) の和"""
        return self.prefix_sum(r) - self.prefix_sum(l)


def inversion_number(a: List[int]) -> int:
    """
    転倒数: i < j かつ a[i] > a[j] となるペア数。
    計算量: O(N log N)
    """
    uniq = sorted(set(a))
    rank = {v: i for i, v in enumerate(uniq)}
    bit = FenwickTree(len(uniq))
    inv = 0
    seen = 0
    for x in a:
        r = rank[x]
        inv += seen - bit.prefix_sum(r + 1)
        bit.add(r, 1)
        seen += 1
    return inv


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】長さ N の数列 A がある。クエリ Q 個で区間和を答えよ。
# 【入力】
#   N Q
#   A1 A2 ... AN
#   クエリ Q 行: L R  （1-index の閉区間 [L,R] の和）
# 【入力例】
# 5 2
# 1 2 3 4 5
# 2 4
# 1 5
# 【出力例】
# 9
# 15
# 【どこを変えるか】
#   - 1-index / 0-index、閉区間 / 半開区間を問題文に合わせる
#   - 「点に値を足す」更新が来るなら ft.add(i, x) をクエリ中でも呼ぶ
#   - 転倒数なら inversion_number(A) を使う
# ============================================================
if __name__ == "__main__":
    from io import StringIO
    import sys

    demo = """5 2
1 2 3 4 5
2 4
1 5
"""
    sys.stdin = StringIO(demo)
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    ft = FenwickTree(N)
    for i, v in enumerate(A):
        ft.add(i, v)

    out = []
    for _ in range(Q):
        L, R = map(int, input().split())
        # 1-index 閉区間 [L,R] → 0-index 半開 [L-1, R)
        out.append(str(ft.range_sum(L - 1, R)))
    print("\n".join(out))
    assert out == ["9", "15"]
    assert inversion_number([3, 1, 2]) == 2
    print("fenwick.py OK")
