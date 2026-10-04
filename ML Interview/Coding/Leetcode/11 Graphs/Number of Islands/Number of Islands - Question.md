---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/number-of-islands/
neetcode: https://neetcode.io/problems/count-number-of-islands
---
# Number of Islands

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/number-of-islands/) · [NeetCode](https://neetcode.io/problems/count-number-of-islands)

**Solve it in:** [[Number of Islands]] · **Answer:** [[Number of Islands - Solution]]

## Problem

You are given an `m x n` grid of characters where `'1'` is land and `'0'` is water. An island is a group of land cells connected horizontally or vertically (not diagonally). Everything outside the grid is water.

Return the number of islands in the grid.

## Examples

**Example 1**
```text
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2**
```text
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## Constraints

- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        pass  # your code here


def g(rows):
    """Helper: build a char grid from a list of strings like ["110", "001"]."""
    return [list(r) for r in rows]


if __name__ == "__main__":
    s = Solution()
    assert s.numIslands(g(["11110", "11010", "11000", "00000"])) == 1
    assert s.numIslands(g(["11000", "11000", "00100", "00011"])) == 3
    assert s.numIslands(g(["0"])) == 0
    assert s.numIslands(g(["1"])) == 1
    assert s.numIslands(g(["101", "010", "101"])) == 5
    assert s.numIslands(g(["111", "101", "111"])) == 1
    assert s.numIslands(g(["1" * 200] * 200)) == 1
    print("All tests passed!")
```
