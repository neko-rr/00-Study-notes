"""
【提出用テンプレート】
多い難易度: 全難易度（特に C 以降）
適する問題: ほぼ全ての AtCoder 提出の土台

使い方:
  1. このファイルをコピーして main を書く
  2. 必要なライブラリ部品を lib/ から追加コピペ

------------------------------------------------------------
【入力・出力の書き方の例】（提出前に main を問題に合わせて書き換える）

入力例:
3 2
1 2 3

出力例:
6

意味: 1行目 N M、2行目 A1..AN。A の総和を出力するだけのサンプル。
------------------------------------------------------------
"""

import sys
import math
import heapq
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from itertools import combinations, permutations, product, accumulate
from typing import List, Optional, Tuple

# ---- 高速入力（入力が多いクエリ・グラフで有効）----
input = sys.stdin.readline

# ---- 再帰上限（DFS・木DP などで必要になることがある）----
sys.setrecursionlimit(1 << 25)

# ---- PyPy で再帰が遅いときの対策（再帰を使う問題だけのとき付ける）----
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")

INF = 10**18
MOD = 998244353
# MOD = 10**9 + 7


def read_ints():
    """1行の整数列を list[int] で受け取る"""
    return list(map(int, input().split()))


def main():
    # ---- ここを問題ごとに書き換える ----
    # 入力例: 3 2 / 1 2 3 → 出力例: 6
    N, M = read_ints()
    A = read_ints()
    print(sum(A))
    # --------------------------------


if __name__ == "__main__":
    # ローカルで入力例を試すとき（提出時はこのブロックを消すかコメントアウト）
    # from io import StringIO
    # sys.stdin = StringIO("3 2\n1 2 3\n")
    main()
