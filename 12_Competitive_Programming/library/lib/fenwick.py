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
        """半開ではない: a[0] + ... + a[i-1]（長さ i の接頭和）"""
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
    値は座標圧縮してから BIT に載せる。
    計算量: O(N log N)
    """
    # 座標圧縮
    uniq = sorted(set(a))
    rank = {v: i for i, v in enumerate(uniq)}
    bit = FenwickTree(len(uniq))
    inv = 0
    # 右から見ると「すでに見た（右側の）より小さい個数」が分かる、
    # ここでは左から見て「自分より大きいものが左に何個あったか」を数える
    seen = 0
    for x in a:
        r = rank[x]
        # これまで追加した中で、rank > r の個数 = seen - (rank<=r の個数)
        inv += seen - bit.prefix_sum(r + 1)
        bit.add(r, 1)
        seen += 1
    return inv


# ============================================================
# 使用例
# ============================================================
if __name__ == "__main__":
    ft = FenwickTree(5)
    for i, v in enumerate([1, 2, 3, 4, 5]):
        ft.add(i, v)
    assert ft.range_sum(1, 4) == 9  # 2+3+4
    assert inversion_number([3, 1, 2]) == 2  # (3,1),(3,2)
    print("fenwick.py OK")
