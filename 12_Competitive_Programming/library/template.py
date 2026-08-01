"""
【提出用テンプレート】
多い難易度: 全難易度（特に C 以降）
適する問題: ほぼ全ての AtCoder 提出の土台

使い方:
  1. このファイルをコピーして main を書く
  2. 必要なライブラリ部品を lib/ から追加コピペ
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
    # 例: N, M = read_ints()
    pass


if __name__ == "__main__":
    main()
