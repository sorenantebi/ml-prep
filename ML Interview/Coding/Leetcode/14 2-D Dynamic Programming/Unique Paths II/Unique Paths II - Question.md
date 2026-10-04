---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/unique-paths-ii/
neetcode: https://neetcode.io/problems/unique-paths-ii
---
# Unique Paths II

**Topic:** [[14 2-D Dynamic Programming|2-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/unique-paths-ii/) · [NeetCode](https://neetcode.io/problems/unique-paths-ii)

**Solve it in:** [[Unique Paths II]] · **Answer:** [[Unique Paths II - Solution]]

## Problem

You are given an `m x n` grid `obstacleGrid` where `1` marks an obstacle and `0` marks a free cell. A robot starts in the top-left corner and must reach the bottom-right corner, moving only **right** or **down** one cell at a time. The robot cannot step on an obstacle.

Return the number of distinct paths from start to finish. If the start or finish cell is itself an obstacle, the answer is `0`. The answer fits in a 32-bit signed integer.

## Examples

**Example 1**
```text
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: The obstacle in the middle leaves only Right-Right-Down-Down and Down-Down-Right-Right.
```

**Example 2**
```text
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
```

**Example 3**
```text
Input: obstacleGrid = [[1]]
Output: 0
```

## Constraints

- `m == obstacleGrid.length`, `n == obstacleGrid[i].length`
- `1 <= m, n <= 100`
- `obstacleGrid[i][j]` is `0` or `1`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert s.uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1
    assert s.uniquePathsWithObstacles([[1]]) == 0
    assert s.uniquePathsWithObstacles([[0]]) == 1
    assert s.uniquePathsWithObstacles([[0, 0], [0, 1]]) == 0  # finish blocked
    assert s.uniquePathsWithObstacles([[0, 0, 0, 0]]) == 1
    assert s.uniquePathsWithObstacles([[0], [1], [0]]) == 0
    assert s.uniquePathsWithObstacles([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 6
    assert s.uniquePathsWithObstacles([[0, 0], [1, 1], [0, 0]]) == 0
    print("All tests passed!")
```
