# AtCoder D〜H 向け 競技プログラミングライブラリ（Python）

既存の学習メモ（入力・基本文法など）とは別に、**提出用コード**と**頻出用語・型の解説**です。

- 想定言語: **Python / PyPy**（AtCoder）
- 想定難易度: **ABC の D〜H**（A〜C の基礎は親フォルダのメモへ）
- 使い方: 用語メモで方針を決め → `lib/` から必要なコードをコピペ
- 各 `lib/*.py` の末尾に **ミニ問題（入力例・出力例・どこを変えるか）** 付きの使用例あり
  - ローカルではそのまま実行可（`StringIO` で入力例を流している）
  - 提出時は `demo = """..."""` 部分を消し、普通の `input()` だけにする

---

## まず読む（用語・型メモ）

### 考え方・選び方

| ファイル | 内容 | 多い難易度 |
|---|---|---|
| [complexity.md](complexity.md) | 計算量・制約 → 許されるアルゴリズム | **全般** |
| [dp_patterns.md](dp_patterns.md) | DP の型の見分け方 | **C〜E** |
| [digit_dp.md](digit_dp.md) | 桁 DP | **E〜H** |
| [rerooting.md](rerooting.md) | 全方位木 DP | **F〜H** |
| [mo.md](mo.md) | Mo's algorithm / オフラインクエリ | **F〜H** |
| [graph_terms.md](graph_terms.md) | グラフ用語とアルゴリズム対応 | **C〜H** |
| [data_structures_guide.md](data_structures_guide.md) | UF / Fenwick / セグ木などの選び方 | **C〜H** |
| [search_patterns.md](search_patterns.md) | 二分探索・しゃくとりの型 | **C〜E** |
| [imos_prefix.md](imos_prefix.md) | 累積和・いもす法・差分 | **C〜D** |

### 分野別用語

| ファイル | 内容 | 多い難易度 |
|---|---|---|
| [substring.md](substring.md) | 部分文字列／部分列／回文／ハッシュ | **C〜E** |
| [math_basics.md](math_basics.md) | 素数・約数・GCD・剰余・組合せ・逆元 | **C〜E** |
| [math_number_theory.md](math_number_theory.md) | 素因数分解・φ・CRT・包除・floor | **D〜E** |
| [math_geometry_other.md](math_geometry_other.md) | 距離・ベクトル・ビット・期待値・確率 | **C〜E** |

---

## 提出用コード（lib）

### D〜E 定番

| ファイル | 主な用途 | 多い難易度 |
|---|---|---|
| [template.py](template.py) | 提出テンプレ | 全難易度 |
| [lib/utils.py](lib/utils.py) | 累積和・座標圧縮 | **C〜D** |
| [lib/binary_search.py](lib/binary_search.py) | めぐる式二分探索 | **C〜E** |
| [lib/bit.py](lib/bit.py) | bit 全探索 | **C〜E** |
| [lib/modint.py](lib/modint.py) | 剰余・nCr | **D〜E** |
| [lib/dp_utils.py](lib/dp_utils.py) | ナップサック等 | **C〜E** |
| [lib/union_find.py](lib/union_find.py) | 連結・グループ | **D〜E** |
| [lib/fenwick.py](lib/fenwick.py) | 区間和・転倒数 | **D〜E** |
| [lib/segment_tree.py](lib/segment_tree.py) | 点更新・区間取得 | **D〜E** |
| [lib/sparse_table.py](lib/sparse_table.py) | 更新なし RMQ | **E〜F** |

### F〜H で特に効く

| ファイル | 主な用途 | 多い難易度 |
|---|---|---|
| [lib/lazy_segtree.py](lib/lazy_segtree.py) | 区間更新＋区間取得 | **E〜H** |
| [lib/graph.py](lib/graph.py) | BFS/Dijkstra/Floyd/Bellman/橋 | **C〜H** |
| [lib/scc.py](lib/scc.py) | 強連結成分 | **F〜H** |
| [lib/lca.py](lib/lca.py) | LCA・木上距離 | **E〜H** |
| [lib/maxflow.py](lib/maxflow.py) | 最大流・二部マッチング | **E〜H** |
| [lib/mincostflow.py](lib/mincostflow.py) | 最小費用流 | **F〜H** |
| [lib/twosat.py](lib/twosat.py) | 2-SAT | **F〜H** |
| [lib/matrix.py](lib/matrix.py) | 行列累乗 | **E〜H** |
| [lib/convolution.py](lib/convolution.py) | 畳み込み（NTT） | **E〜H** |

---

## 問題タイプ別の探し方

| 問題の言い回し・キーワード | 見るファイル |
|---|---|
| 「間に合う？」「N=10^5」 | [complexity.md](complexity.md) |
| 「N 以下の整数の個数」「桁」 | [digit_dp.md](digit_dp.md) |
| 「各頂点を根にした答え」 | [rerooting.md](rerooting.md) |
| 「区間の種類数」オフライン | [mo.md](mo.md) |
| 「強連結」「縮約して DP」 | [lib/scc.py](lib/scc.py) |
| 「木上の距離」「LCA」 | [lib/lca.py](lib/lca.py) |
| 「割当の最小コスト」「ちょうど F 流す」 | [lib/mincostflow.py](lib/mincostflow.py) |
| 「真偽を決めて条件を満たす」 | [lib/twosat.py](lib/twosat.py) |
| 「漸化式の第 N 項」「K 歩の通り数」 | [lib/matrix.py](lib/matrix.py) |
| 「負の辺」「全点対最短」「橋」 | [lib/graph.py](lib/graph.py) |
| 「部分文字列」「部分列」 | [substring.md](substring.md) |
| 「素数」「GCD」「nCr」 | [math_basics.md](math_basics.md) |

---

## おすすめの読み順

1. D〜E: [complexity.md](complexity.md) → [imos_prefix.md](imos_prefix.md) → [search_patterns.md](search_patterns.md) → [dp_patterns.md](dp_patterns.md) / [graph_terms.md](graph_terms.md)  
2. E〜F: [data_structures_guide.md](data_structures_guide.md)（遅延セグ木・Sparse Table）  
3. F〜H: [scc](lib/scc.py) / [lca](lib/lca.py) / [digit_dp.md](digit_dp.md) / [rerooting.md](rerooting.md) / [mo.md](mo.md) / 流・2-SAT・行列  

---

## 提出時の注意

1. コンテスト規約を確認  
2. **PyPy** 提出を基本（再帰が多いときだけおまじない）  
3. 必要なクラスだけコピペ  
4. 0-index / 1-index を問題文と合わせる  

---

## 既存メモとの関係

- 文法・入力・環境: [12_Competitive_Programming](https://github.com/neko-rr/00-Study-notes/tree/main/12_Competitive_Programming)  
- D〜H 向けの部品・用語: **この `library/` フォルダ**  
- Python 基礎: [Python.md](https://github.com/neko-rr/00-Study-notes/blob/main/30_programming/Python/Python.md)  
