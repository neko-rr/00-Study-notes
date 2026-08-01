"""
【2-SAT】
多い難易度: ABC F〜H
適する問題:
  - 「各変数を真偽のどちらにするか」で条件をすべて満たせるか
  - 条件が「A または B」の形だけ（2つのリテラルの OR）
キーワード: 2-SAT, 充足可能性, 含意グラフ, SCC
計算量: O(変数 + 条件)
関連: lib/scc.py
"""

from typing import List, Optional, Tuple


class TwoSAT:
    """
    変数 x0..x_{n-1}
    リテラル: i （真） / i+n （偽）
    """

    def __init__(self, n: int):
        if n < 0:
            raise ValueError("n は 0 以上")
        self.n = n
        self.edges: List[Tuple[int, int]] = []

    def add_clause(self, i: int, f: bool, j: int, g: bool) -> None:
        """
        (x_i == f) or (x_j == g) を追加。
        例: x0 が真 または x1 が偽 → add_clause(0, True, 1, False)
        """
        if not (0 <= i < self.n and 0 <= j < self.n):
            raise ValueError("変数番号が範囲外")
        # a or b  ⇔  (~a → b) and (~b → a)
        a = i if f else i + self.n
        b = j if g else j + self.n
        na = i + self.n if f else i
        nb = j + self.n if g else j
        self.edges.append((na, b))
        self.edges.append((nb, a))

    def satisfiable(self) -> Optional[List[bool]]:
        """
        充足可能なら各変数の割り当て list[bool]、不能なら None。
        """
        # インライン SCC（提出時は scc.py をコピペしてもよい）
        n2 = 2 * self.n
        g = [[] for _ in range(n2)]
        rg = [[] for _ in range(n2)]
        for u, v in self.edges:
            g[u].append(v)
            rg[v].append(u)

        visited = [False] * n2
        order = []

        def dfs(v: int) -> None:
            visited[v] = True
            for to in g[v]:
                if not visited[to]:
                    dfs(to)
            order.append(v)

        for i in range(n2):
            if not visited[i]:
                dfs(i)

        ids = [-1] * n2
        k = 0

        def rdfs(v: int, comp: int) -> None:
            ids[v] = comp
            for to in rg[v]:
                if ids[to] < 0:
                    rdfs(to, comp)

        for v in reversed(order):
            if ids[v] < 0:
                rdfs(v, k)
                k += 1

        for i in range(self.n):
            if ids[i] == ids[i + self.n]:
                return None
        # トポ順で後ろの成分ほど「後」→ 真を優先する定石
        return [ids[i] > ids[i + self.n] for i in range(self.n)]


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】変数 x,y（0/1）。条件:
#   (x が真) or (y が真)
#   (x が偽) or (y が偽)
# を同時に満たす割当はあるか？あれば 0/1 で出力。
# 【入力例】なし（条件固定）
# 【出力例】
# Yes
# 0 1
# （x=偽, y=真 など。逆でも可）
# 【どこを変えるか】
#   - 条件を add_clause で追加していく
#   - 「xi と xj が異なる」→ (xi真 or xj真) と (xi偽 or xj偽)
# ============================================================
if __name__ == "__main__":
    ts = TwoSAT(2)
    ts.add_clause(0, True, 1, True)   # x or y
    ts.add_clause(0, False, 1, False)  # not x or not y
    ans = ts.satisfiable()
    if ans is None:
        print("No")
        raise SystemExit(1)
    print("Yes")
    print(*(1 if v else 0 for v in ans))
    assert ans[0] != ans[1]
    print("twosat.py OK")
