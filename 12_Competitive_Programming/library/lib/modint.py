"""
【剰余演算・逆元・組合せ】
多い難易度: ABC D〜E（組合せ数え上げは E も多い）
適する問題:
  - 「答えを 998244353（または 10^9+7）で割った余り」
  - 「通り数を数えよ」「組合せ nCr」
  - 割り算が mod 上で必要（逆元）
キーワード: 998244353, 10^9+7, nCr, 逆元, フェルマー
"""

from typing import List


class ModIntContext:
    """
    素数 MOD 上の演算と、前計算付き nCr。
    計算量:
      - 四則・pow: O(log MOD) 程度（組み込み）
      - 前計算: O(N + log MOD)
      - nCr クエリ: O(1)
    """

    def __init__(self, mod: int = 998244353, n_max: int = 0):
        if mod <= 1:
            raise ValueError("mod は 2 以上の素数を想定")
        self.mod = mod
        self.fact: List[int] = []
        self.inv_fact: List[int] = []
        if n_max > 0:
            self.build_fact(n_max)

    def build_fact(self, n_max: int) -> None:
        """0..n_max の階乗と逆元階乗を前計算"""
        if n_max < 0:
            return
        mod = self.mod
        fact = [1] * (n_max + 1)
        for i in range(1, n_max + 1):
            fact[i] = fact[i - 1] * i % mod
        inv_fact = [1] * (n_max + 1)
        inv_fact[n_max] = pow(fact[n_max], mod - 2, mod)
        for i in range(n_max, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % mod
        self.fact = fact
        self.inv_fact = inv_fact

    def add(self, a: int, b: int) -> int:
        return (a + b) % self.mod

    def sub(self, a: int, b: int) -> int:
        return (a - b) % self.mod

    def mul(self, a: int, b: int) -> int:
        return (a * b) % self.mod

    def div(self, a: int, b: int) -> int:
        """a / b ≡ a * b^{-1} (mod MOD)。b と MOD が互いに素である必要あり"""
        return a * pow(b, self.mod - 2, self.mod) % self.mod

    def nCr(self, n: int, r: int) -> int:
        if r < 0 or n < r:
            return 0
        if not self.fact or n >= len(self.fact):
            raise ValueError("build_fact(n_max) を先に呼んでください")
        return (
            self.fact[n]
            * self.inv_fact[r]
            % self.mod
            * self.inv_fact[n - r]
            % self.mod
        )

    def nPr(self, n: int, r: int) -> int:
        if r < 0 or n < r:
            return 0
        if not self.fact or n >= len(self.fact):
            raise ValueError("build_fact(n_max) を先に呼んでください")
        return self.fact[n] * self.inv_fact[n - r] % self.mod


# ============================================================
# 使用例
# ============================================================
if __name__ == "__main__":
    mi = ModIntContext(998244353, n_max=10)
    assert mi.nCr(5, 2) == 10
    assert mi.div(6, 2) == 3
    assert mi.mul(3, 5) == 15
    print("modint.py OK")
