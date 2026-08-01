# WA / TLE / RE チェックリスト（B/C帯向け）

「ほぼ合ってるのに落ちる」ときの確認リストです。上から順に見るとよいです。

## 関連リンク

| 行きたい内容 | リンク |
|---|---|
| 目次 | [README.md](README.md) |
| 問題文の読み方 | [how_to_read.md](how_to_read.md) |
| A〜C の型 | [abc_ac_patterns.md](abc_ac_patterns.md) |
| Python テク | [python_tips.md](python_tips.md) |
| 計算量 | [complexity.md](complexity.md) |
| 入力の注意（親メモ） | [AtCoder.md](https://github.com/neko-rr/00-Study-notes/blob/main/12_Competitive_Programming/AtCoder.md) |

---

## 1. WA（答えが違う）

| チェック | よくある原因 | 対策 |
|---|---|---|
| ☐ サンプルを全部通したか | サンプル1だけ見て提出 | 全サンプル＋自分で作った端ケース |
| ☐ 1-index / 0-index | 配列のズレ | 問題が1始まりなら `a-1` を徹底 |
| ☐ 閉区間 / 半開区間 | `[L,R]` と `[L,R)` の取り違え | 紙に例を書いて確認 |
| ☐ 境界（0, 1, N, 空） | N=1 や空文字で壊れる | 最小ケースを手で実行 |
| ☐ Yes/No の大文字 | `YES` と `Yes` の違い | 問題文の出力形式をそのまま |
| ☐ 複数テストケース | 初期化忘れ | 各ケースで配列・変数を作り直す |
| ☐ 整数除算 | `/` と `//` | 競プロはだいたい `//` |
| ☐ 浮動小数 | 誤差で WA | 可能なら整数のまま比較 |
| ☐ 問題の「以上・以下」 | `>` と `>=` | 不等式を問題文と照合 |
| ☐ 破壊的ソート | `A.sort()` で元順が消える | 必要なら `sorted(A)` |

### すぐ試す端ケース

```text
N = 1
全部同じ値
全部 0
文字列が長さ1
グリッドが 1×1
```

---

## 2. TLE（時間切れ）

| チェック | よくある原因 | 対策 |
|---|---|---|
| ☐ 制約を見たか | `N=10^5` で二重ループ | → [complexity.md](complexity.md) |
| ☐ `O(N^2)` していないか | `for i / for j` | ソート・累積和・セットに変更 |
| ☐ 入力が遅い | 行が多い | `sys.stdin.readline`（[template.py](template.py)） |
| ☐ リスト先頭 `pop(0)` | `O(N)` が何度も | `collections.deque` |
| ☐ 文字列連結 | `s += c` を大量に | リストに溜めて `"".join` |
| ☐ PyPy にしたか | CPython でギリギリ | **C問題以降は PyPy 推奨** |

```python
import sys
input = sys.stdin.readline  # 行数が多いとき
```

---

## 3. RE（実行時エラー）

| チェック | よくある原因 | 対策 |
|---|---|---|
| ☐ 配列外参照 | `A[N]` など | 範囲 `0..N-1` を確認 |
| ☐ ゼロ除算 | `x % 0` / `// 0` | 割る前に 0 チェック |
| ☐ 再帰の深さ | DFS で千以上 | `sys.setrecursionlimit` またはループ実装 |
| ☐ 辞書に無いキー | `d[k]` | `d.get(k, 0)` / `defaultdict` |
| ☐ 空リストに `max`/`min` | 要素なし | 空かどうか先に判定 |
| ☐ アンパック失敗 | 行の列数が違う | 入力形式の読み飛ばし・余り |

```python
# 安全な例
if A:
    print(max(A))
else:
    print(0)

from collections import defaultdict
cnt = defaultdict(int)
cnt["a"] += 1
```

---

## 4. その他の結果

| 結果 | 意味 | まず疑うこと |
|---|---|---|
| MLE | メモリ不足 | 巨大な二次元配列 `N=10^4` 超など |
| CE | コンパイル／構文エラー | インデント・全角文字・括弧 |
| 終了コード 9 | 時間超過に近い／無限ループ | while の更新忘れ |

---

## 5. 提出前の30秒チェック

1. 問題の **出力形式**（空白区切り／改行／Yes）を再読  
2. **制約の最大**で計算量は大丈夫か  
3. **N=1** と **最大ケースの形**を頭で実行  
4. 言語は **PyPy** か（A/Bはどちらでも、C以降はPyPy寄り）  

まだ落ちる → 同じ問題の公式解説で「自分が取った型」が合っているか確認 → [abc_ac_patterns.md](abc_ac_patterns.md)
