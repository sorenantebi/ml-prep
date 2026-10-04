---
topic: "2-D Dynamic Programming"
difficulty: Hard
leetcode: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
neetcode: https://neetcode.io/problems/longest-increasing-path-in-matrix
---
# Longest Increasing Path In a Matrix

**Topic:** [[14 2-D Dynamic Programming|2-D Dynamic Programming]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) · [NeetCode](https://neetcode.io/problems/longest-increasing-path-in-matrix)

**Solve it in:** [[Longest Increasing Path In a Matrix]] · **Answer:** [[Longest Increasing Path In a Matrix - Solution]]

## Problem

Given an `m x n` integer matrix, return the length of the longest **strictly increasing** path in it. From any cell you can move to one of its four neighbours (up, down, left, right); diagonal moves and wrapping around the border are not allowed. The path length counts cells.

## Examples

**Example 1**
```text
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: 1 -> 2 -> 6 -> 9
```

**Example 2**
```text
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: 3 -> 4 -> 5 -> 6
```

**Example 3**
```text
Input: matrix = [[1]]
Output: 1
```

## Constraints

- `m == matrix.length`, `n == matrix[i].length`
- `1 <= m, n <= 200`
- `0 <= matrix[i][j] <= 2^31 - 1`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
    assert s.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
    assert s.longestIncreasingPath([[1]]) == 1
    assert s.longestIncreasingPath([[7, 7], [7, 7]]) == 1
    assert s.longestIncreasingPath([[1, 2, 3, 4, 5]]) == 5
    assert s.longestIncreasingPath([[1, 2, 3], [6, 5, 4], [7, 8, 9]]) == 9  # snake
    big = [[r * 50 + (c if r % 2 == 0 else 49 - c) for c in range(50)] for r in range(50)]
    assert s.longestIncreasingPath(big) == 2500  # full snake, no recursion-limit issues
    print("All tests passed!")
```
