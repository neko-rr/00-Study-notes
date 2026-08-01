# AtCoder 部分文字列・文字列用語まとめ（初学者向け）

「部分文字列」と「部分列」は名前が似ていますが、**意味がまったく違います**。  
ここを取り違えると、ほぼ確実に間違いになります。

## 関連リンク

| 行きたい内容 | リンク |
|---|---|
| 目次（ライブラリ全体） | [README.md](README.md) |
| 数学の基礎（素数・GCD・剰余） | [math_basics.md](math_basics.md) |
| 整数論（素因数分解・包除） | [math_number_theory.md](math_number_theory.md) |
| 幾何・ビット・確率 | [math_geometry_other.md](math_geometry_other.md) |
| 計算量の目安 | [complexity.md](complexity.md) |
| 二分探索・しゃくとり | [search_patterns.md](search_patterns.md) |
| bit 全探索（部分列の列挙など） | [lib/bit.py](lib/bit.py) |

---

## いちばん大事な違い（先に覚える）

| 用語 | 英語 | 連続？ | 例（`S = "abcde"`） |
|---|---|---|---|
| **部分文字列** | substring | **必須** | `"bcd"`, `"a"`, `"abcde"` |
| **部分列** | subsequence | **不要**（飛ばしてOK） | `"ace"`, `"bd"`, `"abcde"` |

```text
S = a b c d e
      ↑ ↑ ↑
部分文字列 "bcd" … 隣り合っている

S = a b c d e
    ↑   ↑   ↑
部分列 "ace" … 間を飛ばしてよい（順番は守る）
```

- 問題文に **「連続する」** とあれば → だいたい部分文字列
- **「順番を保って取り出す」** だけで連続と言わなければ → 部分列のことも多い
- 英語問題や解説で `substring` / `subsequence` が出たら、上の表で確認

---

## 用語一覧（よく出る順）

| 用語 | 多い難易度 | ひとこと |
|---|---|---|
| 部分文字列 | C〜E | 連続した切り出し |
| 部分列 | D〜E | 飛ばしてよい取り出し |
| 接頭辞（プレフィックス） | C〜D | 先頭からの部分文字列 |
| 接尾辞（サフィックス） | C〜E | 末尾までの部分文字列 |
| スライス | 全般 | Python での切り出し方 |
| 包含・出現 | C〜D | 含むか／何回出るか |
| 辞書順 | C〜E | 五十音・アルファベット順 |
| 回文 | C〜E | 前からでも後ろからでも同じ |
| ランレングス圧縮 | C〜D | 連続同じ文字をまとめる |
| ローリングハッシュ | D〜E | 部分文字列を数で持って高速比較 |
| Z-algorithm / KMP | E寄り | 「何回出てくる？」を高速に |

---

## 1. 部分文字列（substring）

### 意味
文字列の中から、**隣り合った文字だけ**を切り取ったもの。

### 何を実装するか
- すべての部分文字列を列挙する（長さが短いとき）
- `S[l:r]` で切り出す（0-index、半開区間）
- 「長さちょうど K の部分文字列」を全部見る

```text
【入力例】
abcd
2
【出力例】
ab
bc
cd
（長さちょうど K の部分文字列を列挙）
```

```python
S = input().strip()
K = int(input())
N = len(S)
# 長さちょうど K。全部列挙するなら二重ループに変える
for i in range(N - K + 1):
    print(S[i:i + K])
```

### 問題の言い回し例
- 「連続する部分文字列」
- 「文字列 S の部分文字列のうち〜」
- 「長さ K の区間」

---

## 2. 部分列（subsequence）

### 意味
元の順番は守るが、**途中の文字を飛ばしてよい**取り出し。

### 何を実装するか
- bit 全探索（N≤20）
- DP（最長共通部分列 LCS など）
- 貪欲に「次に必要な文字を探す」

```python
S = "abcde"

# bit 全探索で全部分列を作る（N小さいとき）
N = len(S)
for mask in range(1 << N):
    t = []
    for i in range(N):
        if mask >> i & 1:
            t.append(S[i])
    subseq = "".join(t)
    # subseq を使う

# 「T が S の部分列か？」を判定（順番どおりに探せるか）
def is_subsequence(S: str, T: str) -> bool:
    j = 0
    for ch in S:
        if j < len(T) and ch == T[j]:
            j += 1
    return j == len(T)

assert is_subsequence("abcde", "ace") is True
assert is_subsequence("abcde", "aec") is False  # 順番が違う
```

### 問題の言い回し例
- 「部分列として含む」
- 「いくつかの文字を選んで（順番は変えず）作る」
- 英語: subsequence

---

## 3. 接頭辞（プレフィックス）・接尾辞（サフィックス）

### 意味
- **接頭辞**: 先頭から続く部分文字列（`""`, `"a"`, `"ab"`, `"abc"` …）
- **接尾辞**: ある位置から最後までの部分文字列（`"abc"`, `"bc"`, `"c"`, `""` …）

```python
S = "abc"

prefixes = [S[:i] for i in range(len(S) + 1)]
# ['', 'a', 'ab', 'abc']

suffixes = [S[i:] for i in range(len(S) + 1)]
# ['abc', 'bc', 'c', '']
```

### 何を実装するか
- 「接頭辞と接尾辞が一致するか」（回文判定の一部にも使える）
- 接尾辞をソートして辞書順最小を探す
- Z-algorithm（後述）は「各接尾辞と全体の共通接頭辞長」

### 問題の言い回し例
- 「先頭から一致」
- 「末尾が〜である」
- prefix / suffix

---

## 4. スライス（Python の切り出し）

### 意味
`S[l:r]` は **l 文字目から r 文字目の手前まで**（0始まり）。

```python
S = "abcdef"
# index: 012345

S[1:4]   # "bcd"   … 1,2,3
S[:3]    # "abc"   … 先頭から3文字
S[3:]    # "def"   … 3文字目から最後
S[:-1]   # "abcde" … 最後の1文字を除く
S[::-1]  # "fedcba" … 逆順（回文判定で頻出）
```

### 注意（バグりやすい点）
- AtCoder の問題文は **1-index** が多い → 実装では `-1` する
- `S[l:r]` の `r` は含まない（半開区間）
- 文字列の連結 `S+T` やスライスの繰り返しは、N が大きいと遅いことがある

---

## 5. 包含・出現（含むか／何回出るか）

### 意味
ある文字列 T が S の部分文字列として現れるか、何回現れるか。

```python
S = "ababa"
T = "aba"

# 含むか
print(T in S)  # True

# 重なりを許して出現位置を全部探す
def find_all(S: str, T: str):
    res = []
    start = 0
    while True:
        i = S.find(T, start)
        if i < 0:
            break
        res.append(i)
        start = i + 1  # 重なり許可。禁止なら i + len(T)
    return res

print(find_all(S, T))  # [0, 2]
```

### 何を実装するか
- `in` / `find` / `count`（短い・回数が少ないとき）
- 回数が多い・長いときは **ローリングハッシュや Z/KMP**

---

## 6. 辞書順

### 意味
辞書に載せるときの順番。Python では文字列をそのまま比較できる。

```python
# 小さい方（辞書順で前）
print(min("abc", "abd"))   # abc
print("ab" < "abc")        # True（共通部分のあと、短い方が前）

# 部分文字列の中で辞書順最小を求める例（長さ固定）
S = "bac"
K = 2
best = min(S[i:i+K] for i in range(len(S) - K + 1))
print(best)  # "ac"
```

### 問題の言い回し例
- 「辞書順で最小／最大」
- 「最も若い文字列」

---

## 7. 回文（palindrome）

### 意味
前から読んでも後ろから読んでも同じ文字列。  
部分文字列のうち回文であるもの、を聞く問題が多い。

```python
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# すべての回文部分文字列を列挙（N小さいとき）
def all_palindromic_substrings(S: str):
    N = len(S)
    res = []
    for l in range(N):
        for r in range(l + 1, N + 1):
            t = S[l:r]
            if t == t[::-1]:
                res.append(t)
    return res
```

### 中心展開（N≤10^3〜10^4 向けの定石）

```python
def count_palindromic_substrings(S: str) -> int:
    """回文部分文字列の個数（中心展開）。計算量 O(N^2)"""
    N = len(S)
    ans = 0

    def expand(l, r):
        nonlocal ans
        while l >= 0 and r < N and S[l] == S[r]:
            ans += 1
            l -= 1
            r += 1

    for i in range(N):
        expand(i, i)       # 奇数長（中心が1文字）
        expand(i, i + 1)   # 偶数長（中心が文字の間）
    return ans
```

---

## 8. ランレングス圧縮（RLE）

### 意味
連続する同じ文字をまとめる。  
例: `"aaabbc"` → `[('a',3), ('b',2), ('c',1)]`

```python
def rle(S: str):
    if not S:
        return []
    res = []
    prev = S[0]
    cnt = 1
    for ch in S[1:]:
        if ch == prev:
            cnt += 1
        else:
            res.append((prev, cnt))
            prev = ch
            cnt = 1
    res.append((prev, cnt))
    return res

print(rle("aaabbc"))  # [('a', 3), ('b', 2), ('c', 1)]
```

### 問題の言い回し例
- 「同じ文字が連続している」
- 「まとめて消す」「連続部分を操作する」

---

## 9. ローリングハッシュ（部分文字列の高速比較）

### 意味
文字列を「大きな整数」に変換しておき、任意の部分文字列のハッシュを **O(1)** で取り出す。  
同じハッシュなら（衝突を除き）同じ文字列、とみなして比較する。

### 多い難易度
**D〜E**（「同じ部分文字列か？」を何度も聞くとき）

```python
class RollingHash:
    """
    部分文字列 S[l:r] のハッシュを O(1) で取得。
    前計算 O(N)。衝突を減らしたいときは mod を2つ使うのも定石。
    """

    def __init__(self, s: str, base: int = 1000003, mod: int = (1 << 61) - 1):
        self.mod = mod
        self.base = base
        n = len(s)
        self.pow = [1] * (n + 1)
        self.hash = [0] * (n + 1)  # hash[i] = S[0:i] のハッシュ
        for i, ch in enumerate(s):
            self.pow[i + 1] = self.pow[i] * base % mod
            self.hash[i + 1] = (self.hash[i] * base + ord(ch)) % mod

    def get(self, l: int, r: int) -> int:
        """半開区間 [l, r) のハッシュ"""
        return (self.hash[r] - self.hash[l] * self.pow[r - l]) % self.mod


# 使い方: S[0:3] と T[1:4] が同じか
S, T = "abcdef", "xabcde"
rh_s, rh_t = RollingHash(S), RollingHash(T)
print(rh_s.get(0, 3) == rh_t.get(1, 4))  # "abc" == "abc" → True
```

### 何を実装するか
- 「2つの区間の文字列が等しいか」を高速判定
- 「重複する部分文字列があるか」を二分探索＋ハッシュで探す

---

## 10. Z-algorithm（「先頭とどれだけ一致？」）

### 意味
`Z[i]` = 「`S[i:]` と `S` 全体が、先頭から何文字一致するか」  
つまり **各接尾辞と、文字列全体の共通接頭辞の長さ**。

### 多い難易度
**E寄り**（出現回数、周期、一致判定の高速化）

```python
def z_algorithm(s: str):
    n = len(s)
    z = [0] * n
    if n == 0:
        return z
    z[0] = n
    i, j = 1, 0
    while i < n:
        while i + j < n and s[j] == s[i + j]:
            j += 1
        z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < n and k + z[k] < j:
            z[i + k] = z[k]
            k += 1
        i += k
        j -= k
    return z


# 例: S の中に T が何回出現するか
# コツ: T + "$" + S を作って Z を見る（$ は現れない文字）
def count_occurrences(S: str, T: str) -> int:
    if not T:
        return 0
    z = z_algorithm(T + "$" + S)
    return sum(1 for v in z if v == len(T))

print(count_occurrences("ababa", "aba"))  # 2
```

---

## 11. KMP（パターン検索の定石）

### 意味
失敗したときに「何文字目からやり直すか」を前計算して、文字列検索を高速にする。

### 多い難易度
**E寄り**（Z-algorithm と用途が近い）

```python
def kmp_table(pattern: str):
    """部分マッチ表（失敗関数）"""
    n = len(pattern)
    table = [-1] * (n + 1)
    j = -1
    for i in range(n):
        while j >= 0 and pattern[i] != pattern[j]:
            j = table[j]
        j += 1
        table[i + 1] = j
    return table


def kmp_search(text: str, pattern: str):
    """pattern の出現開始位置一覧。計算量 O(|text| + |pattern|)"""
    if not pattern:
        return []
    table = kmp_table(pattern)
    res = []
    j = 0
    for i, ch in enumerate(text):
        while j >= 0 and ch != pattern[j]:
            j = table[j]
        j += 1
        if j == len(pattern):
            res.append(i - len(pattern) + 1)
            j = table[j]
    return res

print(kmp_search("ababa", "aba"))  # [0, 2]
```

---

## 問題を見たらこう選ぶ（早見表）

| 問題文のヒント | 使うもの |
|---|---|
| 「連続する」「区間 `[L,R]`」 | 部分文字列・スライス |
| 「順番を保って選ぶ」「飛ばしてよい」 | 部分列 |
| 「先頭が一致」「末尾が〜」 | 接頭辞・接尾辞 |
| 「含むか」「何回出てくるか」（短い） | `in` / `find` |
| 「何回出てくるか」（長い・回数多い） | Z / KMP / ハッシュ |
| 「同じ部分文字列か」を何度も | ローリングハッシュ |
| 「前からでも後ろからでも」 | 回文 |
| 「同じ文字が連続」 | ランレングス |
| 「辞書順で最小／最大」 | 文字列比較・`min`/`max` |

---

## 練習のおすすめ順

1. スライスと **部分文字列 vs 部分列** の区別  
2. 接頭辞・接尾辞・回文・RLE  
3. ローリングハッシュ  
4. Z-algorithm または KMP  

ABC の C・D で「文字列」と付く問題を、上の早見表に当てはめながら解くと定着しやすいです。
