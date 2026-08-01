"""
【畳み込み（NTT）】
多い難易度: ABC E〜H（生成関数・多項式は G〜H 寄り）
適する問題:
  - 2つの数列の畳み込み / 多項式の積
注意: mod = 998244353 専用
関連: lib/modint.py, lib/matrix.py
"""

from typing import List

MOD = 998244353
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
    if not a or not b:
        return []
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % mod
    return c


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】多項式 A, B の積 C を 998244353 で求め、係数を空白区切りで出力。
# 【入力】
#   N M
#   A0 ... A_{N-1}
#   B0 ... B_{M-1}
# 【入力例】
# 3 2
# 1 2 3
# 4 5
# 【出力例】
# 4 13 22 15
# （(1+2x+3x^2)*(4+5x)）
# 【どこを変えるか】
#   - 「個数の分布の畳み込み」も同じ（配列の意味だけ変わる）
#   - mod が 998244353 以外ならこのファイルは使えない
# ============================================================
if __name__ == "__main__":
    from io import StringIO
    import sys

    demo = """3 2
1 2 3
4 5
"""
    sys.stdin = StringIO(demo)
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = convolution(A, B)
    print(*C)
    assert C == [4, 13, 22, 15]
    print("convolution.py OK")
