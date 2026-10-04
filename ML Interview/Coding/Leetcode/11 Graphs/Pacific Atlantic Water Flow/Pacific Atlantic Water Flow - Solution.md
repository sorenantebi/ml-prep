---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/pacific-atlantic-water-flow/
neetcode: https://neetcode.io/problems/pacific-atlantic-water-flow
---
# Pacific Atlantic Water Flow - Solution

**Question:** [[Pacific Atlantic Water Flow - Question]] · **Difficulty:** Medium

## Intuition

Checking every cell's downhill paths separately is expensive. Reverse the flow: start from the ocean borders and move **uphill** (to neighbors with height `>=` the current one). Every cell reached from the Pacific border can drain into the Pacific, and likewise for the Atlantic. The answer is the intersection of the two reachable sets.

## Approach

1. Seed a BFS with all Pacific border cells (top row + left column) and find all cells reachable by moving to neighbors of equal or greater height.
2. Do the same from the Atlantic border cells (bottom row + right column).
3. Return the cells present in both reachable sets.

## Code

```python
from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def reachable(starts) -> set:
            seen = set(starts)
            q = deque(starts)
            while q:
                r, c = q.popleft()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen
                            and heights[nr][nc] >= heights[r][c]):  # reverse flow: go uphill
                        seen.add((nr, nc))
                        q.append((nr, nc))
            return seen

        pacific = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]
        both = reachable(pacific) & reachable(atlantic)
        return [[r, c] for r, c in both]
```

## Complexity

- **Time:** `O(m * n)` — each BFS visits every cell at most once.
- **Space:** `O(m * n)` — the two visited sets and the queue.

## Other Approaches

- **DFS from every cell:** for each cell, search downhill to see whether both oceans are reachable — Time `O((m * n)^2)`, Space `O(m * n)`.

## Key Takeaway

When asking "which cells can reach target X", reverse the edges and search once from X — turning many searches into one.
