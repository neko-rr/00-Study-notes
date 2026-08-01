# 有用リンク集（困ったときに開く）

AtCoder・競プロで詰まったとき用のリンク集です。  
**上から「今の困りごと」に合う節**を見てください。

このライブラリ内のメモへも飛ばします。

## このライブラリ内の入口

| 状況 | 開くメモ |
|---|---|
| B/C帯の最初 | [README.md](README.md) の「B/C帯はここから」 |
| 問題の読み方 | [how_to_read.md](how_to_read.md) |
| A〜C の型 | [abc_ac_patterns.md](abc_ac_patterns.md) |
| WA/TLE/RE | [checklist_wa_tle.md](checklist_wa_tle.md) |
| Python の書き方 | [python_tips.md](python_tips.md) |
| グリッド | [grid_intro.md](grid_intro.md) |
| 計算量 | [complexity.md](complexity.md) |
| データ構造の選び方 | [data_structures_guide.md](data_structures_guide.md) |
| 提出用コード | [lib/](lib/) |

---

## 1. これから始める・環境

| 内容 | リンク |
|---|---|
| AtCoder トップ | https://atcoder.jp/home |
| 練習コンテスト（入出力の練習） | https://atcoder.jp/contests/practice |
| AtCoder Beginners Selection（ABS） | https://atcoder.jp/contests/abs |
| Python 入門（APG4bPython） | https://atcoder.jp/contests/APG4bPython |
| C++ 入門（APG4b） | https://atcoder.jp/contests/APG4b |
| 使える言語・ライブラリ一覧 | https://img.atcoder.jp/file/language-update/language-list.html |
| レーティングとは | https://atcoder.jp/posts/82 |

**このライブラリ:** [how_to_read.md](how_to_read.md) → [python_tips.md](python_tips.md)

---

## 2. 問題を探す・練習する

| 内容 | リンク | 使い方 |
|---|---|---|
| AtCoder Problems | https://kenkoooo.com/atcoder/ | 解いた問題・推奨セット・精進管理 |
| 競プロ典型 90 問（ジャッジ） | https://atcoder.jp/contests/typical90 | C〜D 相当の典型を体系的に |
| 典型 90 問 解説 | https://atcoder.jp/contests/typical90/editorial | 解説一覧 |
| 典型 90 問 GitHub | https://github.com/E869120/kyopro_educational_90 | 解説・想定コード |
| AtCoder Categories | https://atcoder-categories.github.io/ | 分野別に弱点強化 |
| AtCoder Tags | https://atcoder-tags.herokuapp.com/ | タグ付き問題探し |
| ABC コンテスト一覧 | https://atcoder.jp/contests/archive?ratedType=1 | 過去問を選ぶ |

**このライブラリ:** [abc_ac_patterns.md](abc_ac_patterns.md) → 型が分かったら過去 ABC の A→C

---

## 3. コンテスト中・公式解説

| 内容 | リンク |
|---|---|
| 開催中・予定のコンテスト | https://atcoder.jp/contests/ |
| 各コンテストの「Editorial / 解説」 | コンテストページ → Editorial |
| 質問・Clarification | コンテストページ → Clarifications |
| 提出結果の見方 | コンテスト → Submissions / 自分の提出 |

解説の読み方のコツ: まず自分の型が合っているか確認 → [abc_ac_patterns.md](abc_ac_patterns.md) / [dp_patterns.md](dp_patterns.md) / [graph_terms.md](graph_terms.md)

---

## 4. アルゴリズム・データ構造の学習

| 内容 | リンク | 向く帯 |
|---|---|---|
| AtCoder Library（ACL）公式 | https://github.com/atcoder/ac-library | D〜 |
| ACL 公式ドキュメント（日本語） | https://tumoiyorozu.github.io/single-file-ac-library/document_ja/ | D〜 |
| ACL 練習コンテスト | https://atcoder.jp/contests/practice2 | D〜 |
| ac-library-python ドキュメント | https://ac-library-python.readthedocs.io/en/latest/ | D〜（ジャッジで import 可） |
| APG4bPython・サードパーティ | https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_aj | 環境確認 |

**このライブラリ（対応表）:**

| 学びたいこと | メモ / コード |
|---|---|
| 累積和・いもす | [imos_prefix.md](imos_prefix.md) |
| 二分探索・しゃくとり | [search_patterns.md](search_patterns.md) |
| DP | [dp_patterns.md](dp_patterns.md) / [digit_dp.md](digit_dp.md) |
| グラフ | [graph_terms.md](graph_terms.md) / [lib/graph.py](lib/graph.py) |
| UF / セグ木など | [data_structures_guide.md](data_structures_guide.md) |
| 数学 | [math_basics.md](math_basics.md) など |
| 文字列 | [substring.md](substring.md) |
| F〜H | [lib/scc.py](lib/scc.py) / [lib/lca.py](lib/lca.py) / [mo.md](mo.md) など |

---

## 5. Python・実装で困ったとき

| 内容 | リンク |
|---|---|
| 公式 Python チュートリアル（言語自体） | https://docs.python.org/ja/3/tutorial/ |
| collections 解説（公式） | https://docs.python.org/ja/3/library/collections.html |
| bisect（公式） | https://docs.python.org/ja/3/library/bisect.html |
| heapq（公式） | https://docs.python.org/ja/3/library/heapq.html |
| PyPy と CPython の差 | https://doc.pypy.org/en/latest/cpython_differences.html |

**このライブラリ:** [python_tips.md](python_tips.md) / [template.py](template.py) / [checklist_wa_tle.md](checklist_wa_tle.md)

入力パターンの詳細 → [AtCoder.md](https://github.com/neko-rr/00-Study-notes/blob/main/12_Competitive_Programming/AtCoder.md)  
Python 基礎メモ → [Python.md](https://github.com/neko-rr/00-Study-notes/blob/main/30_programming/Python/Python.md)

---

## 6. WA / TLE / RE のとき

| 見る順番 | リンク |
|---|---|
| 1. 自分用チェックリスト | [checklist_wa_tle.md](checklist_wa_tle.md) |
| 2. 計算量の目安 | [complexity.md](complexity.md) |
| 3. 公式解説（その問題） | コンテストの Editorial |
| 4. 同じ型の典型 | [競プロ典型 90 問](https://atcoder.jp/contests/typical90) |

よくある原因の早見:

| 結果 | まず疑うこと | ライブラリ内 |
|---|---|---|
| WA | 境界・Yes/No・1-index | [checklist_wa_tle.md](checklist_wa_tle.md) |
| TLE | 二重ループ・言語 | [complexity.md](complexity.md) |
| RE | 配列外・ゼロ割・再帰 | [checklist_wa_tle.md](checklist_wa_tle.md) |

---

## 7. 分野別（弱点強化）

外部で分野検索 → このライブラリで復習、の流れがおすすめです。

| 分野 | 外部 | このライブラリ |
|---|---|---|
| 全探索・実装 | ABS / 過去 ABC-A〜C | [abc_ac_patterns.md](abc_ac_patterns.md) |
| グリッド | [AtCoder Categories](https://atcoder-categories.github.io/) | [grid_intro.md](grid_intro.md) |
| 二分探索 | 典型 90 / Categories | [search_patterns.md](search_patterns.md) |
| DP | 典型 90 / Tags | [dp_patterns.md](dp_patterns.md) |
| グラフ | Categories / Tags | [graph_terms.md](graph_terms.md) |
| データ構造 | ACL Practice | [data_structures_guide.md](data_structures_guide.md) |
| 数学 | Categories | [math_basics.md](math_basics.md) |
| 文字列 | Tags | [substring.md](substring.md) |

---

## 8. コミュニティ・記事（参考）

| 内容 | リンク | 注意 |
|---|---|---|
| Qiita 競プロタグ | https://qiita.com/tags/%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0 | 質がまちまち。公式解説を優先 |
| Zenn 競プロ | https://zenn.dev/topics/competitiveprogramming | 同上 |
| ACL の紹介記事（公式） | https://atcoder.jp/posts/517 | ライブラリ概要 |

コンテスト規約・AI 利用可否は **そのコンテストの注意事項**を毎回確認してください。

---

## 9. 状況別フロー（まとめ）

```text
始め方わからない
  → §1 これから始める → how_to_read.md

どの問題を解く？
  → §2 AtCoder Problems / ABS / 典型90

解けない・WA
  → §6 checklist → 公式解説 → §7 分野別

アルゴリズム名が分からない
  → README の早見表 → §4 ACL / このライブラリの対応表

ライブラリの使い方（セグ木など）
  → このライブラリの lib/ → ACL Practice / ACL ドキュメント
```

---

更新メモ: 外部サイトは第三者運営のものが含まれます。リンク切れのときは AtCoder 公式とこの `library/` を優先してください。
