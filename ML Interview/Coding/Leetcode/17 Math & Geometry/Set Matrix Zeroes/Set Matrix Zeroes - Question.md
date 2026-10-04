---
topic: "Math & Geometry"
difficulty: Medium
leetcode: https://leetcode.com/problems/set-matrix-zeroes/
neetcode: https://neetcode.io/problems/set-zeroes-in-matrix
---
# Set Matrix Zeroes

**Topic:** [[17 Math & Geometry|Math & Geometry]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/set-matrix-zeroes/) · [NeetCode](https://neetcode.io/problems/set-zeroes-in-matrix)

**Solve it in:** [[Set Matrix Zeroes]] · **Answer:** [[Set Matrix Zeroes - Solution]]

## Problem

You are given an `m x n` integer `matrix`. Wherever an element is `0`, set its **entire row and entire column** to `0`.

Only zeros that were in the original matrix count; zeros created by this process must not spread further. The update must be done **in place**. As a follow-up, try to use only constant extra space.

## Examples

**Example 1**
```text
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Example 2**
```text
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

## Constraints

- `m == matrix.length`, `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pass  # your code here


if __name__ == "__main__":
    s = Solution()

    def run(m):
        s.setZeroes(m)
        return m

    assert run([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    assert run([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]) == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    assert run([[5]]) == [[5]]
    assert run([[0]]) == [[0]]
    assert run([[1, 2, 3]]) == [[1, 2, 3]]
    assert run([[1, 0, 3]]) == [[0, 0, 0]]
    assert run([[1], [0], [3]]) == [[0], [0], [0]]
    # zero only in first column of a later row; first row must survive except col 0
    assert run([[1, 2, 3], [0, 5, 6], [7, 8, 9]]) == [[0, 2, 3], [0, 0, 0], [0, 8, 9]]
    # zero only in first row (not col 0)
    assert run([[1, 0], [2, 3]]) == [[0, 0], [2, 0]]
    print("All tests passed!")
```
