# Mo's algorithm / オフラインクエリ（初学者向け・F〜H 対策）

区間クエリを **オンラインで高速に解けないとき**、クエリを並べ替えて処理する技法です。

## 関連リンク

| 行きたい内容 | リンク |
|---|---|
| 目次 | [README.md](README.md) |
| 区間データ構造 | [data_structures_guide.md](data_structures_guide.md) |
| 計算量 | [complexity.md](complexity.md) |
| Fenwick / セグ木 | [lib/fenwick.py](lib/fenwick.py) / [lib/segment_tree.py](lib/segment_tree.py) |

---

## いつ使う（多い難易度: F〜H）

| 状況 | 向く手法 |
|---|---|
| 区間の「種類数」など、加減が局所的にできる | **Mo's algorithm** |
| 更新がなく、区間クエリだけ | 累積和・Sparse Table・セグ木も検討 |
| 更新あり区間クエリ | Fenwick / セグ木 / 遅延セグ木 |
| 「時間」と「区間」を同時にオフライン | タイムラインソート + UF など別解法 |

**先にデータ構造で解けないか**を考え、だめなら Mo を検討します。

---

## Mo's algorithm の考え方

1. クエリ `[L,R]` をすべて読む（オフライン）  
2. ブロックサイズ `B ≈ √N` で、`(L//B, R)` の順にソート  
3. 今見ている区間を伸縮しながら答えを更新（`add` / `remove`）

計算量の目安: `O((N+Q) √N * (addのコスト))`

---

## 入力例・出力例つき雛形（区間の種類数）

```text
【問題】数列 A。クエリ [L,R]（1-index 閉区間）に現れる値の種類数。
【入力例】
5 3
1 2 1 3 2
1 3
2 5
1 5
【出力例】
2
3
3
```

```python
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
qs = []
for i in range(Q):
    L, R = map(int, input().split())
    qs.append((L - 1, R, i))  # 半開 [L,R)

B = max(1, int(N**0.5))
qs.sort(key=lambda x: (x[0] // B, x[1] if (x[0] // B) % 2 == 0 else -x[1]))

# 値の出現回数（座標圧縮してもよい）
freq = {}
cur = 0  # 種類数
ans = [0] * Q

def add(i):
    global cur
    v = A[i]
    freq[v] = freq.get(v, 0) + 1
    if freq[v] == 1:
        cur += 1

def remove(i):
    global cur
    v = A[i]
    freq[v] -= 1
    if freq[v] == 0:
        cur -= 1
        del freq[v]

l = r = 0  # 現在の半開区間 [l,r)
for L, R, idx in qs:
    while r < R:
        add(r)
        r += 1
    while l > L:
        l -= 1
        add(l)
    while r > R:
        r -= 1
        remove(r)
    while l < L:
        remove(l)
        l += 1
    ans[idx] = cur

print("\n".join(map(str, ans)))
```

【どこを変えるか】
- 「種類数」以外なら `add`/`remove` と `cur` の意味を変える
- 値が大きい → 座標圧縮して配列 `freq` にする（dict より速い）
- 更新クエリが混ざる → Mo だけでは足りない（別手法）

---

## オフラインのその他パターン（名前だけ）

| 手法 | 典型 |
|---|---|
| クエリを右端でソート + Fenwick | 「転倒・小さい値の個数」系 |
| 時間で戻せるUF（rollback） | 辺の追加削除を時間で分割 |
| 並列二分探索 | 「いつ条件を満たすか」を一括 |

まずは **Mo** と **右端ソート+Fenwick** を押さえると F〜H で効きます。
