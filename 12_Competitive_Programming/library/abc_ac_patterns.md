# ABC A〜C 典型パターン早見表（B/C帯向け）

茶色〜水色手前の人が、**まずここを見て型を当てる**ための表です。  
D以降の重いデータ構造は、ここでは使いません。

## 関連リンク

| 行きたい内容 | リンク |
|---|---|
| 目次 | [README.md](README.md) |
| 問題文の読み方 | [how_to_read.md](how_to_read.md) |
| WA/TLE 対策 | [checklist_wa_tle.md](checklist_wa_tle.md) |
| Python 頻出テク | [python_tips.md](python_tips.md) |
| グリッド・迷路 | [grid_intro.md](grid_intro.md) |
| 計算量の目安 | [complexity.md](complexity.md) |

---

## いちばん大事な早見表

| 問題文のヒント | 型 | よく使うもの |
|---|---|---|
| 「すべて試せ」「Nが小さい（≤10〜12）」 | 全探索 | `for` / `itertools` / bit（N≤20） |
| 「小さい順／大きい順に選ぶと得」 | 貪欲 | `sort` して前から |
| 「並べ替えてもよい」「順番」 | ソート | `sorted` / `sort(key=...)` |
| 「マス」「上下左右」「壁 `#`」 | グリッド | → [grid_intro.md](grid_intro.md) |
| 「書いてある手順どおりに進める」 | シミュレーション | 変数を更新しながら追う |
| 「何回できるか」「何個取れるか」 | 数え上げ・ループ | 条件を満たすものを数える |
| 「最大／最小の答え」＋単調そう | 二分探索の芽 | → [search_patterns.md](search_patterns.md)（C後半〜） |
| 「合計がちょうど」「選ぶ／選ばない」 | 部分和の芽 | → [dp_patterns.md](dp_patterns.md)（C〜D） |

---

## 1. 全探索

### いつ使う
制約が小さい。`N≤10` なら順列、`N≤20` なら bit も視野。

```text
【入力例】（3整数の最大）
3 1 4
【出力例】
4
```

```python
A = list(map(int, input().split()))
print(max(A))  # 全部見て最大
```

順列の例（N小さいとき）:

```python
from itertools import permutations
N = int(input())
P = list(map(int, input().split()))
ans = 0
for order in permutations(P):
    # order を使ってスコア計算
    ...
```

---

## 2. 貪欲（greedy）

### いつ使う
「毎回いちばん得な選択をしてよい」と証明できそう／サンプルで筋が通る。

```text
【問題】差の絶対値の和を最小にしたい → ソートして隣同士、が典型の入口
【入力例】
3
3 1 2
【出力例】（ソート後のイメージ）
1 2 3
```

```python
N = int(input())
A = list(map(int, input().split()))
A.sort()
print(*A)
```

【注意】貪欲はハマると WA になる。サンプル以外でも「反例がないか」を考える。

---

## 3. ソート＋何か

```text
【入力例】（2番目に大きい数）
4
4 1 3 2
【出力例】
3
```

```python
N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
print(A[1])
```

複数キー:

```python
# (第1キー昇順, 第2キー降順)
rows.sort(key=lambda x: (x[0], -x[1]))
```

---

## 4. シミュレーション

問題文の操作を、そのまま変数で再現する。

```text
【問題】初期 X。操作: 「偶数なら /2、奇数なら +1」を K 回
（デモ用の単純例）
【入力例】
5 2
【出力例】
3
（5→6→3）
```

```python
X, K = map(int, input().split())
for _ in range(K):
    if X % 2 == 0:
        X //= 2
    else:
        X += 1
print(X)
```

---

## 5. グリッド（Cで頻出）

→ 専用ページ [grid_intro.md](grid_intro.md)

---

## 6. 「Yes/No」判定

条件を全部満たすか。1つでもダメなら No。

```python
# 例: すべて正か
A = list(map(int, input().split()))
print("Yes" if all(x > 0 for x in A) else "No")
```

---

## A→B→C で詰まったら

1. [how_to_read.md](how_to_read.md) で制約と入出力を再確認  
2. この表で型を当てる  
3. [checklist_wa_tle.md](checklist_wa_tle.md) でバグを潰す  
4. まだ無理なら、同じ型の公式解説・他者解説を1本読む  

Dに進む準備ができたら → [complexity.md](complexity.md) / [imos_prefix.md](imos_prefix.md)
