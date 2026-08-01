# AtCoder データ構造の選び方（初学者向け）

「何を使うか」で迷ったら、**問題が要求する操作**で選びます。

## 関連リンク

| 行きたい内容 | リンク |
|---|---|
| 目次 | [README.md](README.md) |
| Union-Find | [lib/union_find.py](lib/union_find.py) |
| Fenwick | [lib/fenwick.py](lib/fenwick.py) |
| セグメント木 | [lib/segment_tree.py](lib/segment_tree.py) |
| 遅延セグ木 | [lib/lazy_segtree.py](lib/lazy_segtree.py) |
| 累積和・座標圧縮 | [lib/utils.py](lib/utils.py) / [imos_prefix.md](imos_prefix.md) |
| グラフ | [graph_terms.md](graph_terms.md) |
| 計算量 | [complexity.md](complexity.md) |

---

## 早見表（操作 → 構造）

| やりたい操作 | 第一候補 | 多い難易度 |
|---|---|---|
| 区間の和を **静的に**（更新なし）何度も | [累積和](imos_prefix.md) | C〜D |
| 区間に一括加算（あとでまとめて見る） | [いもす法](imos_prefix.md) | C〜D |
| 点更新 ＋ 区間和 | Fenwick / セグ木 | D〜E |
| 点更新 ＋ 区間 min/max | セグ木 | D〜E |
| 区間更新 ＋ 区間取得 | 遅延セグ木 | E〜F |
| 同じグループ？ 辺を追加 | Union-Find | D〜E |
| 常に最小／最大を取り出す | `heapq` | C〜E |
| ソート済み列への挿入位置 | `bisect` | C〜E |
| 座標が大きすぎる | 座標圧縮 → 上記 | D〜E |

---

## 1. 配列・累積和で足りる？

更新がなく、「区間の和／長方形の和」だけならデータ構造は不要です。

→ [imos_prefix.md](imos_prefix.md) / [lib/utils.py](lib/utils.py)

---

## 2. Union-Find（互いに素集合）

### 向いている操作
- 辺を **追加** する
- 「同じ連結成分？」を聞く
- 成分サイズ・成分数

### 向いていない操作
- 辺の削除
- グラフ上の最短路

→ [lib/union_find.py](lib/union_find.py) / [graph_terms.md](graph_terms.md#5-連結連結成分)

---

## 3. Fenwick Tree（BIT）

### 向いている操作
- `A[i] += x`（点更新）
- `A[l]+...+A[r-1]`（区間和）
- 転倒数

### 向かない操作
- 区間 min（普通の Fenwick では面倒）
- 区間への一括代入

→ [lib/fenwick.py](lib/fenwick.py)

---

## 4. セグメント木

### 向いている操作
- 点更新
- 区間の **min / max / 和 / gcd** など（結合法則がある演算）

Fenwick より汎用。区間和だけなら Fenwick の方が短いことも多いです。

→ [lib/segment_tree.py](lib/segment_tree.py)

---

## 5. 遅延セグ木

### 向いている操作
- 「区間 `[l,r)` に全部 +x」＋「区間の和／min」
- 「区間を全部 y に書き換え」＋区間クエリ

標準セグ木で **区間更新が必要なとき** の上位互換です。

→ [lib/lazy_segtree.py](lib/lazy_segtree.py)

---

## 6. ヒープ（優先度付きキュー）

### 向いている操作
- 常に最小（または最大）を取り出す
- Dijkstra、スケジューリング

```python
import heapq
h = []
heapq.heappush(h, 3)
heapq.heappush(h, 1)
print(heapq.heappop(h))  # 1
```

最大ヒープは符号反転。メモ → [lib/utils.py](lib/utils.py)

---

## 7. bisect（ソート済み配列）

### 向いている操作
- 「x 以上の最初の位置」
- ソート済み列での個数カウント

動的に挿入削除を高速にしたいなら、より高度な集合が必要（ABC の D までは bisect＋配列で足りることが多い）。

→ [search_patterns.md](search_patterns.md) / [lib/binary_search.py](lib/binary_search.py)

---

## 8. 選び方フローチャート

```text
更新はある？
  No  → 累積和・いもす・ソート＋bisect
  Yes → どんな更新？
          辺の追加だけ → Union-Find
          1点だけ変える → Fenwick（和） or セグ木（min等）
          区間をまとめて変える → 遅延セグ木
          最小を何度も取り出す → ヒープ
```

---

## 座標が 10^9 のとき

値そのものを添字にできません。  
**座標圧縮**してから Fenwick / セグ木に載せます。

→ [lib/utils.py](lib/utils.py) の `compress` / [math_geometry_other.md](math_geometry_other.md#10-座標圧縮へのつなぎ)
