---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/surrounded-regions/
neetcode: https://neetcode.io/problems/surrounded-regions
---
# Surrounded Regions - Solution

**Question:** [[Surrounded Regions - Question]] · **Difficulty:** Medium

## Intuition

It is hard to tell directly whether a region is surrounded, but it is easy to find the regions that are **not**: exactly those connected to a border `'O'`. Mark everything reachable from border `'O'`s as safe; every other `'O'` must be captured.

## Approach

1. For every `'O'` on the border, flood-fill (BFS) its region and temporarily mark those cells as `'T'` (safe).
2. Scan the whole board:
   - Remaining `'O'` cells are surrounded → flip to `'X'`.
   - `'T'` cells are safe → restore to `'O'`.

## Code

```python
from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        # 1) mark border-connected 'O's as safe ('T')
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows - 1) or c in (0, cols - 1)) and board[r][c] == "O":
                    board[r][c] = "T"
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "T"
                    q.append((nr, nc))

        # 2) capture the rest, restore the safe cells
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
```

## Complexity

- **Time:** `O(m * n)` — each cell is visited a constant number of times.
- **Space:** `O(m * n)` — the BFS queue in the worst case; marking is done in place.

## Other Approaches

- **Union-Find with a virtual border node:** union border `'O'`s with a dummy node and adjacent `'O'`s with each other; flip any `'O'` not connected to the dummy — Time `O(m * n * α(mn))`, Space `O(m * n)`.

## Key Takeaway

Invert the question: instead of finding enclosed regions, find the ones that escape to the border and treat everything else as captured.
