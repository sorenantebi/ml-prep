---
topic: "Math & Geometry"
difficulty: Easy
leetcode: https://leetcode.com/problems/transpose-matrix/
neetcode: https://neetcode.io/problems/transpose-matrix
---
# Transpose Matrix - Solution

**Question:** [[Transpose Matrix - Question]] · **Difficulty:** Easy

## Intuition

When the matrix is not square, its shape changes, so it can't be transposed in place. Allocate an `n x m` result and copy each `matrix[r][c]` into `res[c][r]`.

## Approach

1. Let `m, n = len(matrix), len(matrix[0])`.
2. Create `res` as an `n x m` grid of zeros.
3. For each `(r, c)`, set `res[c][r] = matrix[r][c]`.
4. Return `res`.

## Code

```python
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = [[0] * m for _ in range(n)]  # shape flips to n x m
        for r in range(m):
            for c in range(n):
                res[c][r] = matrix[r][c]
        return res
```

## Complexity

- **Time:** `O(m * n)`: every cell is copied once.
- **Space:** `O(m * n)`: for the output matrix, with `O(1)` extra beyond that.

## Other Approaches

- **Pythonic `zip`:** `[list(row) for row in zip(*matrix)]` unpacks the rows and groups them column by column. Time `O(m * n)`, Space `O(m * n)`.
- **In-place swap (square only):** swap `matrix[i][j]` with `matrix[j][i]` for `j > i`. Time `O(n^2)`, Space `O(1)`.

## Key Takeaway

A transpose is just the index swap `[r][c] -> [c][r]`. Only square matrices can be transposed in place; any other shape needs a new array.
