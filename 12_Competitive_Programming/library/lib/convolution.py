"""
【畳み込み（NTT: Number Theoretic Transform）】
多い難易度: ABC E〜F（典型だと F 寄り、パターンが分かれば E もあり）
適する問題:
  - 「2つの数列 a, b の畳み込み c[k] = Σ a[i]*b[k-i]」
  - 多項式の掛け算
  - 「個数の分布どうしを足し合わせて新しい分布を作る」
キーワード: 畳み込み, FFT, NTT, 多項式積, 生成関数
計算量: O((n+m) log (n+m))
注意:
  - この実装は mod = 998244353 専用（AtCoder で最もよく使う素数）
  - 他の mod や整数そのままが欲しいときは別手法が必要
"""

from typing import List

MOD = 998244353
# 998244353 = 119 * 2^23 + 1 なので、長さ 2^23 まで NTT 可能
PRIMITIVE_ROOT = 3


def _ntt(a: List[int], invert: bool) -> None:
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    length = 2
    while length <= n:
        wlen = pow(PRIMITIVE_ROOT, (MOD - 1) // length, MOD)
        if invert:
            wlen = pow(wlen, MOD - 2, MOD)
        for i in range(0, n, length):
            w = 1
            half = length >> 1
            for j in range(i, i + half):
                u = a[j]
                v = a[j + half] * w % MOD
                a[j] = u + v if u + v < MOD else u + v - MOD
                a[j + half] = u - v if u >= v else u - v + MOD
                w = w * wlen % MOD
        length <<= 1

    if invert:
        inv_n = pow(n, MOD - 2, MOD)
        for i in range(n):
            a[i] = a[i] * inv_n % MOD


def convolution(a: List[int], b: List[int], mod: int = MOD) -> List[int]:
    """
    c = a * b （多項式積 / 線形畳み込み）
    戻り値の長さは len(a)+len(b)-1（片方空なら空）
    """
    if mod != MOD:
        raise ValueError("この実装は mod=998244353 専用です")
    if not a or not b:
        return []

    n1, n2 = len(a), len(b)
    n = 1
    while n < n1 + n2 - 1:
        n <<= 1

    fa = [x % MOD for x in a] + [0] * (n - n1)
    fb = [x % MOD for x in b] + [0] * (n - n2)
    _ntt(fa, False)
    _ntt(fb, False)
    for i in range(n):
        fa[i] = fa[i] * fb[i] % MOD
    _ntt(fa, True)
    return fa[: n1 + n2 - 1]


def convolution_naive(a: List[int], b: List[int], mod: int = MOD) -> List[int]:
    """検算用の O(nm) 畳み込み"""
    if not a or not b:
        return []
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % mod
    return c


# ============================================================
# 使用例
# ============================================================
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [4, 5]
    # (1+2x+3x^2)*(4+5x) = 4 + 13x + 22x^2 + 15x^3
    assert convolution(a, b) == [4, 13, 22, 15]
    assert convolution(a, b) == convolution_naive(a, b)
    print("convolution.py OK")
