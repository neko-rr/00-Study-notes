# AtCoder 数学用語まとめ①：基本（初学者向け）

素数・約数・GCD・剰余・組合せなど、**ABC の C〜E でほぼ毎回見る基礎**です。

## 関連リンク

| 行きたい内容 | リンク |
|---|---|
| 目次（ライブラリ全体） | [README.md](README.md) |
| 素因数分解・φ・中国剰余など | [math_number_theory.md](math_number_theory.md) |
| 幾何・ビット・確率 | [math_geometry_other.md](math_geometry_other.md) |
| 文字列用語 | [substring.md](substring.md) |
| 計算量の目安 | [complexity.md](complexity.md) |
| DP・通り数 | [dp_patterns.md](dp_patterns.md) |
| 剰余・nCr の提出用コード | [lib/modint.py](lib/modint.py) |
| bit 全探索 | [lib/bit.py](lib/bit.py) |

---

## 用語一覧

| 用語 | 多い難易度 | ひとこと |
|---|---|---|
| [素数](#1-素数prime) | C〜D | 1 とその数以外で割れない |
| [約数・倍数](#2-約数divisor倍数multiple) | C〜D | 割り切れる／割る側 |
| [GCD / LCM](#3-gcd最大公約数--lcm最小公倍数) | C〜E | 最大公約数／最小公倍数 |
| [剰余・合同](#4-剰余mod--合同congruence) | C〜E | 割った余り |
| [階乗・順列・組合せ](#5-階乗順列組合せ) | D〜E | n!, nPr, nCr |
| [逆元](#6-逆元modular-inverse) | D〜E | mod 上の「割り算」 |
| [等差・等比](#7-等差数列等比数列) | C〜D | 公差／公比で増える列 |
| [切り上げ・切り捨て](#8-切り上げ切り捨て) | C〜D | 割り算の端数処理 |
| [オーバーフロー注意](#9-大きな数とオーバーフロー注意) | C〜E | Python は安心寄り |

---

## 1. 素数（prime）

### 意味
1 とその数自身以外では割り切れない 2 以上の整数。  
例: 2, 3, 5, 7, 11 …

### 何を実装するか
- 1 個が素数か判定
- 1〜N の素数をまとめて列挙（エラトステネス）

```python
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sieve(n: int):
    """0..n が素数かのリスト。計算量 O(N log log N)"""
    is_p = [True] * (n + 1)
    if n >= 0:
        is_p[0] = False
    if n >= 1:
        is_p[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, n + 1, i):
                is_p[j] = False
    return is_p
```

より進んだ分解は → [素因数分解](math_number_theory.md#1-素因数分解prime-factorization)

---

## 2. 約数（divisor）／倍数（multiple）

### 意味
- **約数**: `N % d == 0` となる d（N を割り切る数）
- **倍数**: N の倍数は `N, 2N, 3N, ...`

### 何を実装するか
約数列挙は **O(√N)** が定石。

```python
def divisors(n: int):
    """昇順の約数リスト"""
    res = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            res.append(i)
            if i * i != n:
                res.append(n // i)
        i += 1
    return sorted(res)

print(divisors(12))  # [1, 2, 3, 4, 6, 12]
```

---

## 3. GCD（最大公約数） / LCM（最小公倍数）

### 意味
- **GCD**: 両方を割り切る最大の数
- **LCM**: 両方の倍数になる最小の数  
  公式: `lcm(a,b) = a // gcd(a,b) * b`（先に割ると溢れにくい）

```python
import math

def gcd(a: int, b: int) -> int:
    return math.gcd(a, b)  # Python 3.5+


def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return a // math.gcd(a, b) * b


# 3つ以上
from functools import reduce
def gcd_all(xs):
    return reduce(math.gcd, xs)
```

拡張ユークリッド（ax+by=gcd）は → [math_number_theory.md](math_number_theory.md#3-拡張ユークリッドの互除法)

---

## 4. 剰余（mod） / 合同（congruence）

### 意味
- `a % m` … a を m で割った余り
- `a ≡ b (mod m)` … a と b を m で割った余りが同じ

AtCoder では答えを **`998244353`** や **`10^9+7`** で割った余り、が超頻出。

```python
MOD = 998244353

def mod_add(a, b):
    return (a + b) % MOD

def mod_mul(a, b):
    return (a * b) % MOD

# 余りが負にならないようにする（Python の % は非負になりやすいが習慣として）
def mod_norm(x):
    return x % MOD
```

提出用クラスは → [lib/modint.py](lib/modint.py)

---

## 5. 階乗・順列・組合せ

### 意味
| 記号 | 意味 | 例 |
|---|---|---|
| `n!` | 1×2×…×n | `5! = 120` |
| `nPr` | 順番ありで n 個から r 個 | `5P2 = 20` |
| `nCr` | 順番なしで n 個から r 個 | `5C2 = 10` |

```python
# 小さい n なら math でOK
import math
print(math.factorial(5))
print(math.perm(5, 2))   # Python 3.8+
print(math.comb(5, 2))   # Python 3.8+

# mod 付き（前計算）は lib を使う
# → lib/modint.py の ModIntContext.nCr
```

「通り数を数えよ」系はほぼこれ＋[逆元](#6-逆元modular-inverse)。

---

## 6. 逆元（modular inverse）

### 意味
mod 上で「割る」ための数。  
`a * inv(a) ≡ 1 (mod MOD)` となる `inv(a)`。

**前提**: MOD が素数で、a が MOD の倍数でないこと（よくある設定）。

```python
MOD = 998244353

def modinv(a: int, mod: int = MOD) -> int:
    # フェルマーの小定理: a^(mod-2) ≡ a^{-1}
    return pow(a, mod - 2, mod)

def moddiv(a: int, b: int, mod: int = MOD) -> int:
    """a / b (mod MOD)"""
    return a * modinv(b, mod) % mod

print(moddiv(6, 2))  # 3
```

詳しい背景 → [フェルマーの小定理](math_number_theory.md#4-フェルマーの小定理)

---

## 7. 等差数列／等比数列

### 意味
- **等差**: 一定の差（公差）で増える。例: 3, 5, 7, 9（公差 2）
- **等比**: 一定の比（公比）で増える。例: 3, 6, 12, 24（公比 2）

```python
# 初項 a, 公差 d, 項数 n の等差の和
def arithmetic_sum(a, d, n):
    return n * (2 * a + (n - 1) * d) // 2

# 初項 a, 公比 r, 項数 n の等比の和（r!=1）
def geometric_sum(a, r, n):
    if r == 1:
        return a * n
    return a * (r**n - 1) // (r - 1)
```

---

## 8. 切り上げ／切り捨て

### 意味
整数割り算で端数をどうするか。

```python
# 切り捨て（0 方向ではない。Python の // は負で床関数）
print(7 // 2)   # 3
print(-7 // 2)  # -4

# 正の整数だけで切り上げ: (a + b - 1) // b
def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b

print(ceil_div(7, 2))  # 4
```

---

## 9. 大きな数とオーバーフロー注意

### 意味
C++ では `long long` を超えると壊れやすいが、**Python の int は自動で桁が増える**ので普通は安心。  
ただし **mod を取り忘れる**と遅くなったり、問題の要求とずれたりする。

```python
# 悪い例（答えが mod なのに取り忘れ）
# ans = ans * x

# 良い例
MOD = 998244353
ans = ans * x % MOD
```

---

## 問題を見たらこう選ぶ

| ヒント | 見るところ |
|---|---|
| 「素数」「素数列挙」 | [#1 素数](#1-素数prime) |
| 「約数の個数」「約数の和」 | [#2 約数](#2-約数divisor倍数multiple) → [素因数分解](math_number_theory.md#1-素因数分解prime-factorization) |
| 「最大公約数」「互いに素」 | [#3 GCD](#3-gcd最大公約数--lcm最小公倍数) |
| 「998244353 で割った余り」 | [#4 剰余](#4-剰余mod--合同congruence) / [lib/modint.py](lib/modint.py) |
| 「通り数」「組合せ」 | [#5](#5-階乗順列組合せ) / [#6 逆元](#6-逆元modular-inverse) |
| 「切り上げ」 | [#8](#8-切り上げ切り捨て) |
