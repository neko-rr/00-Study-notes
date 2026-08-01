"""
【Union-Find（DSU / 素集合データ構造）】
多い難易度: ABC D〜E
適する問題:
  - 「同じグループに属するか？」を何度も聞く
  - 「辺を追加していくと連結になるか」
  - 「連結成分の個数・サイズ」
キーワード: 連結, グループ, 友達関係, 道路を繋ぐ, 同じ集合
計算量: ほぼ O(α(N)) ≒ 定数
"""

from typing import List


class UnionFind:
    def __init__(self, n: int):
        if n < 0:
            raise ValueError("n は 0 以上")
        self.parent = [-1] * n
        self.n = n
        self.parts = n

    def find(self, x: int) -> int:
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
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
        buckets = [[] for _ in range(self.n)]
        for i in range(self.n):
            buckets[self.find(i)].append(i)
        return [g for g in buckets if g]


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】人が N 人（1..N）。クエリ Q 個。
#   型1: a b を同じグループにする
#   型2: a b が同じグループなら Yes / 違うなら No
# 【入力】
#   N Q
#   クエリ Q 行: t a b
# 【入力例】
# 5 4
# 1 1 2
# 1 2 3
# 2 1 3
# 2 1 4
# 【出力例】
# Yes
# No
# 【どこを変えるか】
#   - 頂点が 1-index なら UnionFind(N+1) にして 1..N を使う（下記）
#   - 「辺を足したあとの成分数」なら uf.parts を見る
#   - 「グループの人数」なら uf.size(a) を見る
# ============================================================
if __name__ == "__main__":
    from io import StringIO
    import sys

    demo = """5 4
1 1 2
1 2 3
2 1 3
2 1 4
"""
    sys.stdin = StringIO(demo)
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    uf = UnionFind(N + 1)  # 1-index 用に N+1
    out = []
    for _ in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            uf.union(a, b)
        else:
            out.append("Yes" if uf.same(a, b) else "No")
    print("\n".join(out))
    assert out == ["Yes", "No"]
    print("union_find.py OK")
