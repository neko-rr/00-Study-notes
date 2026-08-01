"""
【行列累乗】
多い難易度: ABC E〜H
適する問題:
  - 「漸化式を N 項目まで高速に」
  - 「グラフでちょうど K 歩の通り数」
  - フィボナッチの一般化
キーワード: 行列累乗, 線形漸化式, ダブリング
計算量: O(D^3 log N)（D は行列サイズ）
関連: lib/modint.py, math_basics.md
"""

from typing import List

MOD_DEFAULT = 998244353


def mat_mul(a: List[List[int]], b: List[List[int]], mod: int) -> List[List[int]]:
    """a は n×m, b は m×p"""
    n = len(a)
    m = len(a[0])
    p = len(b[0])
    res = [[0] * p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            aik = a[i][k]
            if aik == 0:
                continue
            for j in range(p):
                res[i][j] = (res[i][j] + aik * b[k][j]) % mod
    return res


def mat_pow(a: List[List[int]], exp: int, mod: int = MOD_DEFAULT) -> List[List[int]]:
    """正方行列 a の exp 乗"""
    n = len(a)
    # 単位行列
    res = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    base = [row[:] for row in a]
    e = exp
    while e > 0:
        if e & 1:
            res = mat_mul(res, base, mod)
        base = mat_mul(base, base, mod)
        e >>= 1
    return res


def fib(n: int, mod: int = MOD_DEFAULT) -> int:
    """
    0-index: F(0)=0, F(1)=1, F(2)=1, ...
    n 番目のフィボナッチを O(log n) で。
    """
    if n < 0:
        raise ValueError("n は 0 以上")
    if n <= 1:
        return n % mod
    m = mat_pow([[1, 1], [1, 0]], n - 1, mod)
    return m[0][0] % mod


# ============================================================
# 使用例（ミニ問題）
# ------------------------------------------------------------
# 【問題】フィボナッチ数列 F(0)=0,F(1)=1,... の F(N) を 998244353 で割った余り。
# 【入力】
#   N
# 【入力例】
# 10
# 【出力例】
# 55
# 【どこを変えるか】
#   - 一般の漸化式: 遷移行列を自分で作って mat_pow
#   - MOD が 10^9+7 なら引数 mod を変える
#   - 「K 歩の通り数」: 隣接行列を mat_pow(..., K)
# ============================================================
if __name__ == "__main__":
    from io import StringIO
    import sys

    demo = """10
"""
    sys.stdin = StringIO(demo)
    input = sys.stdin.readline

    N = int(input())
    ans = fib(N)
    print(ans)
    assert ans == 55
    print("matrix.py OK")
