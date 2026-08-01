# AtCoder D・E 向け 競技プログラミングライブラリ（Python）

既存の学習メモ（入力・基本文法など）とは別に、**提出用コード**と**頻出用語・型の解説**です。

- 想定言語: **Python / PyPy**（AtCoder）
- 想定難易度: **ABC の D・E 中心**（一部は E 後半〜F）
- 使い方: 用語メモで方針を決め → `lib/` から必要なコードをコピペ

---

## まず読む（用語・型メモ）

各メモ先頭に **関連リンク表** があり、メモ同士と `lib/` へ飛べます。

### 考え方・選び方

| ファイル | 内容 | 多い難易度 |
|---|---|---|
| [complexity.md](complexity.md) | 計算量・制約 → 許されるアルゴリズム | **全般** |
| [dp_patterns.md](dp_patterns.md) | DP の型の見分け方 | **C〜E** |
| [graph_terms.md](graph_terms.md) | グラフ用語とアルゴリズム対応 | **C〜E** |
| [data_structures_guide.md](data_structures_guide.md) | UF / Fenwick / セグ木などの選び方 | **C〜E** |
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
| 「間に合う？」「N=10^5」 | [complexity.md](complexity.md) |
| 「選んで合計」「区間を分割」「N≤20」 | [dp_patterns.md](dp_patterns.md) / [lib/dp_utils.py](lib/dp_utils.py) |
| 「最短」「依存関係」「二部」「流す」 | [graph_terms.md](graph_terms.md) |
| 「点更新」「区間min」「同じグループ」 | [data_structures_guide.md](data_structures_guide.md) |
| 「最小のX」「最長の連続区間」 | [search_patterns.md](search_patterns.md) |
| 「区間の和」「区間に加算をたくさん」 | [imos_prefix.md](imos_prefix.md) |
| 「部分文字列」「部分列」「回文」 | [substring.md](substring.md) |
| 「素数」「GCD」「998244353」「nCr」 | [math_basics.md](math_basics.md) / [lib/modint.py](lib/modint.py) |
| 「素因数分解」「包除」「CRT」 | [math_number_theory.md](math_number_theory.md) |
| 「マンハッタン」「XOR」「期待値」 | [math_geometry_other.md](math_geometry_other.md) |

---

## おすすめの読み順（初学者）

1. [complexity.md](complexity.md) … 制約の見方  
2. [imos_prefix.md](imos_prefix.md) / [search_patterns.md](search_patterns.md) … すぐ使える型  
3. [dp_patterns.md](dp_patterns.md) / [graph_terms.md](graph_terms.md)  
4. [data_structures_guide.md](data_structures_guide.md) … D〜E の武器選び  
5. 数学・文字列メモは、問題で用語が出たときに参照  

---

## 提出時の注意

1. コンテスト規約を確認（AI 禁止・ライブラリ持ち込み可否など）  
2. **PyPy** 提出を基本にする（再帰が多いときだけ `template.py` のおまじない）  
3. 必要なクラスだけコピペする  
4. 0-index / 1-index を問題文と合わせる  

---

## 既存メモとの関係

親フォルダのメモ（入力・基本文法・習慣）とは役割が違います。

- 文法・入力・環境: [12_Competitive_Programming](https://github.com/neko-rr/00-Study-notes/tree/main/12_Competitive_Programming) の `AtCoder.md` / `basic.md` など  
- D・E 向けの部品・用語: **この `library/` フォルダ**  
- Python 基礎: [Python.md](https://github.com/neko-rr/00-Study-notes/blob/main/30_programming/Python/Python.md)  
