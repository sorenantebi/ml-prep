---
topic: "Binary Search"
difficulty: Medium
leetcode: https://leetcode.com/problems/search-a-2d-matrix/
neetcode: https://neetcode.io/problems/search-2d-matrix
---
# Search a 2D Matrix - Solution

**Question:** [[Search a 2D Matrix - Question]] · **Difficulty:** Medium

## Intuition

Reading the rows one after another produces a single sorted list of length `m * n`. We can binary search that virtual list directly, converting a flat index `k` into the cell `(k // n, k % n)`.

## Approach

1. Let `lo = 0`, `hi = m * n - 1`.
2. While `lo <= hi`: `mid = (lo + hi) // 2`, read `val = matrix[mid // n][mid % n]`.
3. If `val == target` return `True`; if `val < target` set `lo = mid + 1`; else `hi = mid - 1`.
4. Return `False`.

## Code

```python
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            val = matrix[mid // n][mid % n]  # flat index -> (row, col)
            if val == target:
                return True
            if val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
```

## Complexity

- **Time:** `O(log(m * n))` — binary search over all cells.
- **Space:** `O(1)`.

## Other Approaches

- **Two binary searches:** first find the row whose range contains `target`, then binary search inside that row — Time `O(log m + log n)`, Space `O(1)`.
- **Staircase search:** start top-right, move left if too big, down if too small — Time `O(m + n)`, Space `O(1)` (works even for the weaker "rows and columns sorted" variant).

## Key Takeaway

A row-major sorted matrix is just a sorted 1D array in disguise — map indices with `divmod(k, n)`.
