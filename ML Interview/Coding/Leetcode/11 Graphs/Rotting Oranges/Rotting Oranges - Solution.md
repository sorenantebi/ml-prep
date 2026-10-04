---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/rotting-oranges/
neetcode: https://neetcode.io/problems/rotting-fruit
---
# Rotting Oranges - Solution

**Question:** [[Rotting Oranges - Question]] · **Difficulty:** Medium

## Intuition

Rot spreads from all rotten oranges simultaneously, one step per minute — exactly the layer-by-layer expansion of a **multi-source BFS**. The number of BFS levels needed to reach every fresh orange is the answer; if any fresh orange is left unreached, return `-1`.

## Approach

1. Scan the grid: enqueue all rotten oranges and count fresh ones.
2. While the queue is non-empty and fresh oranges remain:
   - Process exactly the current level (all oranges that rotted in the previous minute).
   - Rot each fresh neighbor, decrement the fresh count, enqueue it.
   - Increment `minutes` after the level.
3. Return `minutes` if `fresh == 0`, else `-1`.

## Code

```python
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while q and fresh > 0:  # stop once nothing is fresh to avoid an extra minute
            for _ in range(len(q)):  # one BFS level == one minute
                r, c = q.popleft()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1

        return minutes if fresh == 0 else -1
```

## Complexity

- **Time:** `O(m * n)` — each cell is enqueued at most once.
- **Space:** `O(m * n)` — the BFS queue.

## Other Approaches

- **Repeated simulation:** each minute scan the whole grid and rot neighbors of rotten cells until nothing changes — Time `O((m * n)^2)`, Space `O(m * n)` for the next-state copy.

## Key Takeaway

Simultaneous spreading over time = multi-source BFS processed level by level; track a "remaining" counter to detect unreachable targets.
