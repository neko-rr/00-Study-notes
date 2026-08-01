# AtCoder D・E 向け 競技プログラミングライブラリ（Python）

既存の学習メモ（入力・基本文法など）とは別に、**提出時にコピペして使う典型アルゴリズム集**と、**頻出用語の解説**です。

- 想定言語: **Python / PyPy**（AtCoder）
- 想定難易度: **ABC の D・E 中心**（一部は E 後半〜F）
- 使い方: 必要なファイルからクラス／関数をコピーし、`template.py` と組み合わせて提出

---

## まず読む（用語メモ）

困ったときの入口です。用語 → 意味 → 実装の順で書いてあります。

| ファイル | 内容 | 多い難易度 |
|---|---|---|
| [substring.md](substring.md) | 部分文字列／部分列／回文／ハッシュ など | **C〜E** |
| [math_basics.md](math_basics.md) | 素数・約数・GCD・剰余・組合せ・逆元 | **C〜E** |
| [math_number_theory.md](math_number_theory.md) | 素因数分解・φ・CRT・包除・floor 高速化 | **D〜E** |
| [math_geometry_other.md](math_geometry_other.md) | 距離・ベクトル・ビット・期待値・確率 | **C〜E** |

各メモの先頭に **関連リンク表** があり、用語メモ同士・`lib/` のコードへ飛べます。

---

## 提出用コード（lib）

| ファイル | 主な用途 | 多い難易度 |
|---|---|---|
| [template.py](template.py) | 提出テンプレ（高速入力・再帰） | 全難易度 |
| [lib/utils.py](lib/utils.py) | 累積和・座標圧縮・ヒープ | **C〜D** |
| [lib/binary_search.py](lib/binary_search.py) | めぐる式二分探索 | **C〜E** |
| [lib/bit.py](lib/bit.py) | bit 全探索・部分集合 | **C〜E** |
| [lib/modint.py](lib/modint.py) | 剰余・逆元・組合せ | **D〜E** |
| [lib/dp_utils.py](lib/dp_utils.py) | ナップサック等の典型 DP | **C〜E** |
| [lib/union_find.py](lib/union_find.py) | 連結成分・グループ分け | **D〜E** |
| [lib/fenwick.py](lib/fenwick.py) | 区間和・転倒数 | **D〜E** |
| [lib/segment_tree.py](lib/segment_tree.py) | 区間 min/max/和 | **D〜E** |
| [lib/lazy_segtree.py](lib/lazy_segtree.py) | 区間更新＋区間取得 | **E〜F** |
| [lib/graph.py](lib/graph.py) | BFS/DFS・Dijkstra・トポソ | **C〜E** |
| [lib/maxflow.py](lib/maxflow.py) | 最大流・最小カット | **E〜F** |
| [lib/convolution.py](lib/convolution.py) | 畳み込み（NTT） | **E〜F** |

---

## 問題タイプ別の探し方

| 問題の言い回し・キーワード | 見るファイル |
|---|---|
| 「部分文字列」「部分列」「回文」「出現」 | [substring.md](substring.md) |
| 「素数」「約数」「GCD」「998244353」「nCr」 | [math_basics.md](math_basics.md) / [lib/modint.py](lib/modint.py) |
| 「素因数分解」「互いに素」「包除」「CRT」 | [math_number_theory.md](math_number_theory.md) |
| 「マンハッタン」「XOR」「期待値」「確率」 | [math_geometry_other.md](math_geometry_other.md) |
| 「同じグループ？」「辺を追加して連結？」 | [lib/union_find.py](lib/union_find.py) |
| 「最小の X は？」「答えは単調」 | [lib/binary_search.py](lib/binary_search.py) |
| 「区間の和・最小」「点更新」 | [lib/fenwick.py](lib/fenwick.py) / [lib/segment_tree.py](lib/segment_tree.py) |
| 「区間に一括で加算／代入しつつ区間クエリ」 | [lib/lazy_segtree.py](lib/lazy_segtree.py) |
| 「最短距離」「到達できるか」「依存関係」 | [lib/graph.py](lib/graph.py) |
| 「最大で何個流せる？」「最小カット」 | [lib/maxflow.py](lib/maxflow.py) |
| 「N≤20 で全部試す」「ビットで集合」 | [lib/bit.py](lib/bit.py) / [math_geometry_other.md](math_geometry_other.md) |
| 「2 数列の畳み込み・多項式の積」 | [lib/convolution.py](lib/convolution.py) |
| 「部分和・ナップサック」 | [lib/dp_utils.py](lib/dp_utils.py) |
| 「累積和・座標が大きすぎる」 | [lib/utils.py](lib/utils.py) |

---

## 難易度の見方

各 `.py` の先頭コメント、および用語メモの表に次を書いてあります。

- **多い難易度**: ABC でよく出る帯（例: D〜E）
- **適する問題**: どんな文言・設定のときに使うか
- **計算量**: ざっくりの目安

※ あくまで目安です。

---

## 提出時の注意

1. コンテスト規約を確認（AI 禁止・ライブラリ持ち込み可否など）
2. **PyPy** 提出を基本にする（再帰が多いときだけ `template.py` のおまじない）
3. 必要なクラスだけコピペし、使わないコードは入れない
4. 0-index / 1-index を問題文と合わせる

---

## 既存メモとの関係

親フォルダのメモ（入力・基本文法・習慣）とは役割が違います。

- 文法・入力・環境: [12_Competitive_Programming](https://github.com/neko-rr/00-Study-notes/tree/main/12_Competitive_Programming) の `AtCoder.md` / `basic.md` など
- D・E 以降のアルゴリズム部品・用語: **この `library/` フォルダ**
- Python 基礎: [Python.md](https://github.com/neko-rr/00-Study-notes/blob/main/30_programming/Python/Python.md)
