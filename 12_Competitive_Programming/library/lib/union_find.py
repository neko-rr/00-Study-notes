"""
【Union-Find（DSU / 素集合データ構造）】
多い難易度: ABC D〜E
適する問題:
  - 「同じグループに属するか？」を何度も聞く
  - 「辺を追加していくと連結になるか」
  - 「連結成分の個数・サイズ」
  - 無向グラフで、辺の追加のみ（削除は苦手）
キーワード: 連結, グループ, 友達関係, 道路を繋ぐ, 同じ集合
計算量: ほぼ O(α(N)) ≒ 定数（アッカーマンの逆関数）
"""

from typing import List


class UnionFind:
    def __init__(self, n: int):
        if n < 0:
            raise ValueError("n は 0 以上")
        # parent[i] < 0 のとき i は根で、絶対値がサイズ
        self.parent = [-1] * n
        self.n = n
        self.parts = n  # 連結成分数

    def find(self, x: int) -> int:
        """x の代表元（根）"""
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        x と y を同じ集合にまとめる。
        すでに同じなら False、新たに結合したら True。
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        # サイズの大きい方へくっつける（union by size）
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.parts -= 1
        return True

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def size(self, x: int) -> int:
        return -self.parent[self.find(x)]

    def groups(self) -> List[List[int]]:
        """各連結成分のメンバー一覧"""
        buckets = [[] for _ in range(self.n)]
        for i in range(self.n):
            buckets[self.find(i)].append(i)
        return [g for g in buckets if g]


# ============================================================
# 使用例
# ============================================================
if __name__ == "__main__":
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    assert uf.same(0, 2) is True
    assert uf.same(0, 3) is False
    assert uf.size(0) == 3
    assert uf.parts == 3
    print("union_find.py OK")
