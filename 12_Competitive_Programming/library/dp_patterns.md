# AtCoder DP の見分け方（初学者向け）

「DP っぽい」まで分かっても、**どの型か**が分からないと手が止まります。  
キーワード → 型 → 実装の対応表です。

## 関連リンク

| 行きたい内容 | リンク |
|---|---|
| 目次 | [README.md](README.md) |
| 提出用 DP 雛形 | [lib/dp_utils.py](lib/dp_utils.py) |
| bit DP・部分集合 | [lib/bit.py](lib/bit.py) / [math_geometry_other.md](math_geometry_other.md) |
| 剰余・通り数 | [lib/modint.py](lib/modint.py) / [math_basics.md](math_basics.md) |
| 計算量の目安 | [complexity.md](complexity.md) |

---

## 早見表

| 問題の言い回し | DP の型 | 多い難易度 | 状態のイメージ |
|---|---|---|---|
| 重さ・容量の上限で価値最大 | ナップサック | C〜D | `dp[w] = 最大価値` |
| 合計をちょうど K にできるか | 部分和 | C〜D | `dp[s] = 可能か` |
| 選ぶ／選ばない（個数1） | 0-1 ナップサック | C〜D | 後ろから更新 |
| 何個でも使ってよい | 個数無制限 | D | 前から更新 |
| 区間を分割してコスト最小 | 区間 DP | E | `dp[l][r]` |
| 桁・大きい数の条件付き数え上げ | 桁 DP | E | `桁, 未満フラグ, ...` |
| 訪問集合を持つ（N≤20） | bit DP | D〜E | `dp[mask][v]` |
| 最長の増加部分 | LIS | D〜E | 長さ or `O(N log N)` |
| 期待値を求めよ | 期待値 DP | E | `dp[状態]=期待値` |
| N 以下の整数を数える | 桁 DP | E〜H | → [digit_dp.md](digit_dp.md) |
| 各頂点を根にした答え | 全方位木 DP | F〜H | → [rerooting.md](rerooting.md) |

コード雛形 → [lib/dp_utils.py](lib/dp_utils.py)

---

## 1. ナップサック／部分和

### いつ使う
- 「重さの合計 ≤ W」
- 「合計を K にできるか」
- 「いくつか選んで〜」

### 実装の要点＋入力例・出力例

```text
【入力例】
3 5
2 3
3 4
4 5
【出力例】
7
```

```python
N, W = map(int, input().split())
dp = [0] * (W + 1)
for _ in range(N):
    w, v = map(int, input().split())
    # 0-1: 後ろから更新。個数無制限なら range(w, W+1) で前から
    for j in range(W, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)
print(dp[W])
```

詳細コード → [lib/dp_utils.py](lib/dp_utils.py)

---

## 2. 区間 DP

### いつ使う
- 「区間 `[l,r]` をまとめるコスト」
- 「行列の連鎖」「石を合体」系
- 制約が `N ≤ 300`〜`400`（`O(N^3)`）

### 状態
`dp[l][r]` = 区間 `[l,r)` を処理した最適値

```python
# 長さの短い区間から埋める
for length in range(2, N + 1):
    for l in range(0, N - length + 1):
        r = l + length
        for m in range(l + 1, r):
            dp[l][r] = min(dp[l][r], dp[l][m] + dp[m][r] + cost)
```

---

## 3. bit DP

### いつ使う
- `N ≤ 20` 前後
- 「訪問した集合」「使った集合」が状態になる
- 巡回セールスマン（TSP）型

```python
# dp[mask][v] = 集合 mask を訪問し、今 v にいる最小コスト
N = 4
INF = 10**18
dp = [[INF] * N for _ in range(1 << N)]
dp[1 << 0][0] = 0  # 0 からスタートする例
for mask in range(1 << N):
    for v in range(N):
        if dp[mask][v] >= INF:
            continue
        for nv in range(N):
            if mask >> nv & 1:
                continue
            nmask = mask | (1 << nv)
            dp[nmask][nv] = min(dp[nmask][nv], dp[mask][v] + cost[v][nv])
```

ビットの意味 → [math_geometry_other.md](math_geometry_other.md#7-部分集合とビット)

---

## 4. 桁 DP（イメージ）

### いつ使う
- 「N 以下の整数で条件を満たす個数」
- N がとても大きい（桁で渡される）

### 状態の典型
- 上から何桁目か
- まだ N と同じ接頭辞か（未満フラグ）
- その他の条件（桁和、登場した数字など）

「未満フラグを立てたら、あとは自由」がポイントです。

---

## 5. LIS（最長増加部分列）

### いつ使う
- 「最長の増加する取り出し」
- 部分列（連続でなくてよい）に注意 → [substring.md](substring.md)

```python
# O(N log N) の長さだけ求める版は dp_utils.lis_length
```

→ [lib/dp_utils.py](lib/dp_utils.py)

---

## 6. 期待値 DP

### いつ使う
- 「操作を繰り返すときの回数の期待値」
- 確率の用語は → [math_geometry_other.md](math_geometry_other.md#8-期待値)

### 考え方
`E[状態] = 1 + Σ p * E[次の状態]` のような方程式／メモ化再帰。

---

## 遷移を書くときのチェックリスト

1. **状態**は何を覚えるか（何が決まれば残りが計算できるか）  
2. **遷移**はどこから来るか／どこへ行くか  
3. **初期値**と **答えの取り出し位置**  
4. 制約的に `O(状態数 × 遷移)` が間に合うか → [complexity.md](complexity.md)

---

## 問題を見たら

| ヒント | 開く場所 |
|---|---|
| 重さ・価値・容量 | [#1](#1-ナップサック部分和) |
| 区間をまとめる・分割 | [#2](#2-区間-dp) |
| N が 20 以下で集合 | [#3](#3-bit-dp) |
| 「N 以下の整数の個数」 | [#4](#4-桁-dpイメージ) |
| 最長増加 | [#5](#5-lis最長増加部分列) |
| 期待値 | [#6](#6-期待値-dp) |
