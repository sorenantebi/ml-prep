---
topic: "Graphs"
difficulty: Easy
leetcode: https://leetcode.com/problems/island-perimeter/
neetcode: https://neetcode.io/problems/island-perimeter
---
# Island Perimeter - Solution

**Question:** [[Island Perimeter - Question]] · **Difficulty:** Easy

## Intuition

Every land cell contributes 4 edges. Each time two land cells are adjacent, they share one edge, which removes 2 from the total (one from each cell). So we only need to count land cells and adjacent land pairs; no traversal is necessary.

## Approach

1. Iterate over every cell of the grid.
2. For each land cell, add 4 to the perimeter.
3. If the cell above is also land, subtract 2 (shared edge). Do the same for the cell to the left.
4. Checking only up and left counts each shared edge exactly once.
5. Return the total.

## Code

```python
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    # each shared edge with an earlier neighbor removes 2 sides
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2
        return perimeter
```

## Complexity

- **Time:** `O(rows * cols)` — every cell is visited once.
- **Space:** `O(1)` — only a counter is used.

## Other Approaches

- **DFS/BFS from a land cell:** traverse the island and add 1 for every neighbor that is water or out of bounds — Time `O(rows * cols)`, Space `O(rows * cols)` for the visited set / recursion stack.

## Key Takeaway

For perimeter/edge counting on grids, count "4 per cell minus 2 per shared edge" — a simple scan beats a graph traversal when the answer is a local property.
