# AtCoder 数学用語まとめ②：整数論（初学者向け）

素因数分解・オイラーのφ・中国剰余など、**D〜E で効いてくる一歩進んだ道具**です。  
先に [math_basics.md](math_basics.md)（素数・GCD・剰余・逆元）を読んでおくと安心です。

## 関連リンク

| 行きたい内容 | リンク |
|---|---|
| 目次（ライブラリ全体） | [README.md](README.md) |
| 数学の基礎 | [math_basics.md](math_basics.md) |
| 幾何・ビット・確率 | [math_geometry_other.md](math_geometry_other.md) |
| 文字列 | [substring.md](substring.md) |
| 計算量の目安 | [complexity.md](complexity.md) |
| 包除と bit | [lib/bit.py](lib/bit.py) |
| 剰余演算コード | [lib/modint.py](lib/modint.py) |

---

## 用語一覧

| 用語 | 多い難易度 | ひとこと |
|---|---|---|
| [素因数分解](#1-素因数分解prime-factorization) | C〜E | 素数の積に分解 |
| [互いに素](#2-互いに素coprime) | C〜E | gcd が 1 |
| [拡張ユークリッド](#3-拡張ユークリッドの互除法) | D〜E | ax+by=gcd の x,y |
| [フェルマーの小定理](#4-フェルマーの小定理) | D〜E | 逆元計算の根拠 |
| [オイラーのφ関数](#5-オイラーのφ関数totient) | E寄り | 1..n で n と互いに素な個数 |
| [中国剰余定理 CRT](#6-中国剰余定理crt) | E〜F | 余りの連立を解く |
| [包除原理](#7-包除原理inclusion-exclusion) | D〜E | 重なりを足し引き |
| [床関数・天井関数](#8-床関数天井関数) | D〜E | floor / ceil |
| [商が同じ区間](#9-商が同じ区間floor-sumsの前段階) | E寄り | ⌊N/i⌋ の高速化 |

---

## 1. 素因数分解（prime factorization）

### 意味
整数を素数の積で表すこと。  
例: `12 = 2^2 * 3`

### 何を実装するか
- 1 個の数を O(√N) で分解
- 約数の個数は指数+1 の積（`12` なら (2+1)*(1+1)=6）

```python
def factorize(n: int):
    """n を素因数分解。戻り値: {素数: 指数}"""
    res = {}
    if n <= 1:
        return res
    # 2 を先に
    while n % 2 == 0:
        res[2] = res.get(2, 0) + 1
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            res[p] = res.get(p, 0) + 1
            n //= p
        p += 2
    if n > 1:
        res[n] = res.get(n, 0) + 1
    return res


def count_divisors_from_factors(fac: dict) -> int:
    ans = 1
    for e in fac.values():
        ans *= e + 1
    return ans

print(factorize(12))                 # {2: 2, 3: 1}
print(count_divisors_from_factors(factorize(12)))  # 6
```

素数判定・列挙は → [math_basics.md#1-素数prime](math_basics.md#1-素数prime)

---

## 2. 互いに素（coprime）

### 意味
`gcd(a, b) == 1` であること。  
例: 8 と 15 は互いに素。8 と 12 は互いに素でない。

```python
import math

def is_coprime(a: int, b: int) -> bool:
    return math.gcd(a, b) == 1
```

「mod で割れる／逆元が存在する」とセットで出ることが多い → [逆元](math_basics.md#6-逆元modular-inverse)

---

## 3. 拡張ユークリッドの互除法

### 意味
`gcd(a,b)` だけでなく、`a*x + b*y = gcd(a,b)` となる整数 x,y も求める。  
線形合同式 `a*x ≡ c (mod m)` を解くときに使う。

```python
def extgcd(a: int, b: int):
    """
    戻り値: (g, x, y) で a*x + b*y = g = gcd(a,b)
    """
    if b == 0:
        return a, 1, 0
    g, x, y = extgcd(b, a % b)
    return g, y, x - (a // b) * y


def modinv_ext(a: int, m: int):
    """m が素数でなくても、gcd(a,m)=1 なら逆元を返す"""
    g, x, _ = extgcd(a, m)
    if g != 1:
        return None  # 逆元なし
    return x % m

g, x, y = extgcd(240, 46)
print(g, x, y)  # 2, -9, 47 など（2 = 240*(-9)+46*47）
```

MOD が素数のときの短い逆元は → [math_basics.md#6-逆元modular-inverse](math_basics.md#6-逆元modular-inverse)

---

## 4. フェルマーの小定理

### 意味
素数 p と、p の倍数でない a について  
`a^(p-1) ≡ 1 (mod p)`  
よって `a^(p-2) ≡ a^{-1} (mod p)`（逆元）。

```python
MOD = 998244353  # 素数
a = 123456
inv = pow(a, MOD - 2, MOD)
print(a * inv % MOD)  # 1
```

実装としては `pow(a, MOD-2, MOD)` を覚えれば十分。  
コード部品 → [lib/modint.py](lib/modint.py)

---

## 5. オイラーのφ関数（totient）

### 意味
`φ(n)` = `1,2,...,n` のうち n と互いに素な個数。  
例: `φ(6)=2`（1 と 5）

```python
def totient(n: int) -> int:
    """O(√N) で φ(n) を1個求める"""
    res = n
    p = 2
    x = n
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            res = res // p * (p - 1)
        p += 1 if p == 2 else 2
    if x > 1:
        res = res // x * (x - 1)
    return res

print(totient(6))   # 2
print(totient(10))  # 4
```

素因数が分かれば高速 → [素因数分解](#1-素因数分解prime-factorization)

---

## 6. 中国剰余定理（CRT）

### 意味
次のような「余りの連立」を解く定理。

```text
x ≡ a1 (mod m1)
x ≡ a2 (mod m2)
...
```

`m1, m2, ...` が互いに素なら解が一意（mod それらの積）。

```python
import math

def crt_coprime(a1, m1, a2, m2):
    """
    x ≡ a1 (mod m1), x ≡ a2 (mod m2)
    前提: m1 と m2 が互いに素。戻り値 (x, m1*m2)
    """
    # Python 3.8+: pow(a, -1, m) で逆元
    inv = pow(m1, -1, m2)
    x = (a1 + m1 * ((a2 - a1) * inv % m2)) % (m1 * m2)
    return x, m1 * m2

# 例: x≡2 (mod 3), x≡3 (mod 5) → x=8
print(crt_coprime(2, 3, 3, 5))  # (8, 15)
print(math.gcd(3, 5))           # 1（互いに素であることの確認）
```

※ `gcd(m1,m2)≠1` の一般ケースまで必要なら AtCoder Library の `crt` を参照。

---

## 7. 包除原理（inclusion-exclusion）

### 意味
集合の重なりを「足して、引き、また足す…」で全体を求める考え方。

```text
|A ∪ B| = |A| + |B| - |A ∩ B|
|A ∪ B ∪ C| = |A|+|B|+|C| - |A∩B|-|B∩C|-|C∩A| + |A∩B∩C|
```

競プロでは「N 以下で 2 または 3 または 5 の倍数の個数」などに使う。

```python
import math

def count_multiples_up_to(N: int, factors: list) -> int:
    """包除で、factors のいずれかの倍数の個数（1..N）"""
    k = len(factors)
    ans = 0
    for mask in range(1, 1 << k):
        l = 1
        bits = 0
        ok = True
        for i in range(k):
            if mask >> i & 1:
                bits += 1
                g = math.gcd(l, factors[i])
                # lcm（オーバーフロー回避のため先に割る）
                if l // g > N // factors[i]:
                    ok = False
                    break
                l = l // g * factors[i]
        if not ok:
            continue
        cnt = N // l
        if bits % 2 == 1:
            ans += cnt
        else:
            ans -= cnt
    return ans

print(count_multiples_up_to(10, [2, 3]))  # 2,3,4,6,8,9,10 → 7
```

bit の列挙は → [lib/bit.py](lib/bit.py)

---

## 8. 床関数／天井関数

### 意味
- 床関数 `floor(x)`: x 以下の最大整数（例: 3.7 → 3）
- 天井関数 `ceil(x)`: x 以上の最小整数（例: 3.2 → 4）

```python
import math
print(math.floor(3.7))  # 3
print(math.ceil(3.2))   # 4

# 正整数の切り上げ割り算
def ceil_div(a, b):
    return (a + b - 1) // b
```

基礎の切り上げとセット → [math_basics.md#8-切り上げ切り捨て](math_basics.md#8-切り上げ切り捨て)

---

## 9. 商が同じ区間（floor の高速化）

### 意味
`⌊N/1⌋, ⌊N/2⌋, ...` を全部計算したいとき、同じ商が連続する区間をまとめて飛ばすと **O(√N)** で済む。

```python
def floor_ranges(n: int):
    """
    (l, r, q) を列挙: i=l..r で n//i == q
    """
    res = []
    l = 1
    while l <= n:
        q = n // l
        r = n // q
        res.append((l, r, q))
        l = r + 1
    return res

# 例: sum(n//i for i in 1..n) を高速に
def sum_floor(n: int) -> int:
    ans = 0
    for l, r, q in floor_ranges(n):
        ans += q * (r - l + 1)
    return ans
```

---

## 問題を見たらこう選ぶ

| ヒント | 見るところ |
|---|---|
| 「素因数に分解」「約数の個数」 | [#1](#1-素因数分解prime-factorization) |
| 「互いに素」 | [#2](#2-互いに素coprime) |
| 「ax ≡ b (mod m) を解け」 | [#3](#3-拡張ユークリッドの互除法) |
| 「逆元」「割り算の余り」 | [#4](#4-フェルマーの小定理) / [math_basics 逆元](math_basics.md#6-逆元modular-inverse) |
| 「1..n で互いに素な個数」 | [#5](#5-オイラーのφ関数totient) |
| 「あまりが a,b を同時に満たす」 | [#6](#6-中国剰余定理crt) |
| 「A または B または C」の個数 | [#7](#7-包除原理inclusion-exclusion) |
| 「N/i の和を全部」 | [#9](#9-商が同じ区間floor-sumsの前段階) |
