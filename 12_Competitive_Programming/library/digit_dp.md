# 桁 DP（初学者向け・F〜H 対策）

「N 以下の整数で条件を満たす個数」を、**桁ごとに決めていく DP**です。

## 関連リンク

| 行きたい内容 | リンク |
|---|---|
| 目次 | [README.md](README.md) |
| DP の型全般 | [dp_patterns.md](dp_patterns.md) |
| 計算量 | [complexity.md](complexity.md) |
| 通り数の剰余 | [lib/modint.py](lib/modint.py) |

---

## いつ使う（多い難易度: E〜H）

| 言い回し | 例 |
|---|---|
| 「N 以下で〜を満たす整数の個数」 | 桁和が D、4 と 9 を含まない、など |
| N が非常に大きい（最大 10^18 や桁文字列） | ループで回せない |
| 「未満フラグ」が出てくる解説 | 典型の桁 DP |

---

## 状態の定石

```text
dp[桁位置][未満フラグ][その他] = 通り数
```

| 状態 | 意味 |
|---|---|
| 桁位置 | 上から何桁目を決めるか |
| 未満フラグ | もう N より小さいと確定したか（0/1） |
| その他 | 桁和、登場した数字、leading zero など |

**未満フラグが 1 になったら、その先の桁は 0〜9 を自由に選べる**のがポイントです。

---

## 入力例・出力例つき雛形

```text
【問題】1 以上 N 以下の整数のうち、桁和がちょうど D の個数（mod 不要のデモ）
【入力例】
20
5
【出力例】
2
（5 と 14）
```

```python
import sys
sys.setrecursionlimit(1 << 25)

N = input().strip()  # 桁で扱うので文字列のまま
D = int(input())
digits = [int(c) for c in N]
L = len(digits)

# memo[pos][tight][sum] ; tight=1 ならまだ N と同じ接頭辞
memo = {}

def dfs(pos: int, tight: int, s: int) -> int:
    if pos == L:
        return 1 if s == D else 0
    key = (pos, tight, s)
    if key in memo:
        return memo[key]
    lim = digits[pos] if tight else 9
    res = 0
    for d in range(lim + 1):
        ntight = tight and (d == lim)
        ns = s + d
        if ns > D:
            continue
        res += dfs(pos + 1, ntight, ns)
    memo[key] = res
    return res

# 「1 以上」なので 0 を除く。桁和0の 0 が答えに入る場合は調整
ans = dfs(0, 1, 0)
if D == 0:
    ans -= 1  # 0 を除外
print(ans)
```

【どこを変えるか】
- 条件を `ns` や追加状態に載せる（「4と9禁止」なら数字制限）
- mod が必要なら `res %= MOD`
- leading zero を区別したいなら状態に `leading` を追加

---

## チェックリスト

1. N を文字列（桁配列）にする  
2. 未満フラグを忘れない  
3. 先頭の 0（leading zero）が条件に影響するか確認  
4. 「0 以上」か「1 以上」かで答えを調整  
