---
topic: "Graphs"
difficulty: Easy
leetcode: https://leetcode.com/problems/island-perimeter/
neetcode: https://neetcode.io/problems/island-perimeter
---
# Island Perimeter

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/island-perimeter/) · [NeetCode](https://neetcode.io/problems/island-perimeter)

**Solve it in:** [[Island Perimeter]] · **Answer:** [[Island Perimeter - Solution]]

## Problem

You are given a `rows x cols` grid where `grid[r][c] == 1` marks a land cell and `0` marks water. Cells connect only horizontally and vertically (not diagonally). The grid contains exactly one island (one or more connected land cells), it is fully surrounded by water, and it has no "lakes" (no water enclosed inside the island that is disconnected from the outer water). Each cell is a square with side length 1.

Return the perimeter of the island.

## Examples

**Example 1**
```text
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
```

**Example 2**
```text
Input: grid = [[1]]
Output: 4
```

**Example 3**
```text
Input: grid = [[1,0]]
Output: 4
```

## Constraints

- `1 <= rows, cols <= 100`
- `grid[r][c]` is `0` or `1`
- There is exactly one island in `grid`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16
    assert s.islandPerimeter([[1]]) == 4
    assert s.islandPerimeter([[1,0]]) == 4
    assert s.islandPerimeter([[1,1]]) == 6
    assert s.islandPerimeter([[1,1],[1,1]]) == 8
    assert s.islandPerimeter([[0,0,0],[0,1,0],[0,0,0]]) == 4
    assert s.islandPerimeter([[1,1,1,1,1]]) == 12
    print("All tests passed!")
```
