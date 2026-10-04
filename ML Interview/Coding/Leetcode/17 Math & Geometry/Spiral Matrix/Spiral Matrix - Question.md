---
topic: "Math & Geometry"
difficulty: Medium
leetcode: https://leetcode.com/problems/spiral-matrix/
neetcode: https://neetcode.io/problems/spiral-matrix
---
# Spiral Matrix

**Topic:** [[17 Math & Geometry|Math & Geometry]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/spiral-matrix/) · [NeetCode](https://neetcode.io/problems/spiral-matrix)

**Solve it in:** [[Spiral Matrix]] · **Answer:** [[Spiral Matrix - Solution]]

## Problem

Given an `m x n` `matrix`, return all of its elements in **spiral order**. Start at the top-left corner, go right along the top row, down the right column, left along the bottom row, up the left column, and keep spiralling inward until every element has been visited exactly once.

## Examples

**Example 1**
```text
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2**
```text
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Constraints

- `m == matrix.length`, `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert s.spiralOrder([[7]]) == [7]
    assert s.spiralOrder([[1, 2, 3, 4]]) == [1, 2, 3, 4]
    assert s.spiralOrder([[1], [2], [3]]) == [1, 2, 3]
    assert s.spiralOrder([[1, 2], [3, 4], [5, 6]]) == [1, 2, 4, 6, 5, 3]
    assert s.spiralOrder([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 6, 5, 4]
    assert s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == \
        [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    print("All tests passed!")
```
