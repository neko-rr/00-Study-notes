# グリッド・迷路入門（B/C帯向け）

ABC の C でよく出る「マス目」問題の基本です。  
慣れたら [lib/graph.py](lib/graph.py) の `bfs_grid` に進めます。

## 関連リンク

| 行きたい内容 | リンク |
|---|---|
| 目次 | [README.md](README.md) |
| A〜C の型 | [abc_ac_patterns.md](abc_ac_patterns.md) |
| Python テク | [python_tips.md](python_tips.md) |
| BFS 実装 | [lib/graph.py](lib/graph.py) |
| グラフ用語 | [graph_terms.md](graph_terms.md) |

---

## 1. グリッドの持ち方

```text
【入力例】
3 4
.#..
.#.#
....
```

```python
H, W = map(int, input().split())
S = [input().rstrip() for _ in range(H)]
# S[i][j] … i行 j列（0-index）
# '#' が壁、'.' が通路、など問題ごとに違う
```

座標は `(行, 列)` = `(y, x)` と決めて統一するとミスが減ります。

---

## 2. 上下左右の4方向

```python
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右

def neighbors(i, j, H, W):
    for di, dj in DIRS:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W:
            yield ni, nj
```

8方向なら斜めも足す:

```python
DIRS8 = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
```

---

## 3. 全マスを見る（探索なし）

```text
【問題】'#' の個数を数えよ
【入力例】
2 3
#.#
.##
【出力例】
3
```

```python
H, W = map(int, input().split())
S = [input().rstrip() for _ in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            ans += 1
print(ans)
```

---

## 4. 迷路の最短手数（BFS）

重みなし（1マス＝1手）なら **BFS** が定石。

```text
【問題】左上 (1,1) から右下 (H,W) への最短手数。壁は '#'。到達不能は -1。
【入力例】
3 4
..#.
.#..
....
【出力例】
6
```

```python
from collections import deque

H, W = map(int, input().split())
S = [input().rstrip() for _ in range(H)]
sy, sx = 0, 0
gy, gx = H - 1, W - 1

dist = [[-1] * W for _ in range(H)]
dist[sy][sx] = 0
q = deque([(sy, sx)])
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    y, x = q.popleft()
    for dy, dx in DIRS:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < H and 0 <= nx < W):
            continue
        if S[ny][nx] == "#":
            continue
        if dist[ny][nx] != -1:
            continue
        dist[ny][nx] = dist[y][x] + 1
        q.append((ny, nx))

print(dist[gy][gx])
```

【どこを変えるか】
- スタート／ゴール位置が入力で来る → `sy,sx` を読む
- 壁文字が違う → `"#"` を変える
- 「到達できるか」だけ → `dist[gy][gx] != -1`

ライブラリ版 → [lib/graph.py](lib/graph.py) の `bfs_grid`

---

## 5. つながっているマスのかたまり（連結成分）

`'#'` のかたまりの個数、など。DFS/BFS で塗る。

```python
seen = [[False] * W for _ in range(H)]

def dfs(y, x):
    stack = [(y, x)]
    seen[y][x] = True
    while stack:
        cy, cx = stack.pop()
        for ny, nx in neighbors(cy, cx, H, W):
            if S[ny][nx] != "#":
                continue
            if seen[ny][nx]:
                continue
            seen[ny][nx] = True
            stack.append((ny, nx))

parts = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#" and not seen[i][j]:
            dfs(i, j)
            parts += 1
print(parts)
```

---

## よくあるバグ

| バグ | 対策 |
|---|---|
| 範囲外アクセス | `0 <= ni < H and 0 <= nj < W` を先に |
| 訪問忘れ | `dist` や `seen` を必ず更新してからキューへ |
| 壁の判定忘れ | 移動前に壁チェック |
| 二次元初期化ミス | `[[0]*W for _ in range(H)]`（`*` だけは NG） |

→ [checklist_wa_tle.md](checklist_wa_tle.md) / [python_tips.md](python_tips.md)
