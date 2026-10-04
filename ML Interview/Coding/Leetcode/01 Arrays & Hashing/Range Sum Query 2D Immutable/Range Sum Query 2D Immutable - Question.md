---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/range-sum-query-2d-immutable/
neetcode: https://neetcode.io/problems/range-sum-query-2d-immutable
---
# Range Sum Query 2D Immutable

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/range-sum-query-2d-immutable/) · [NeetCode](https://neetcode.io/problems/range-sum-query-2d-immutable)

**Solve it in:** [[Range Sum Query 2D Immutable]] · **Answer:** [[Range Sum Query 2D Immutable - Solution]]

## Problem

You are given a 2D integer matrix `matrix`. Build a class `NumMatrix` that answers many queries of the form: what is the sum of all elements inside the rectangle whose upper-left corner is `(row1, col1)` and lower-right corner is `(row2, col2)` (both corners inclusive)?

- `NumMatrix(matrix)` preprocesses the matrix.
- `sumRegion(row1, col1, row2, col2)` returns the rectangle sum.

Each `sumRegion` call must run in `O(1)` time.

## Examples

**Example 1**
```text
Input:  ["NumMatrix","sumRegion","sumRegion","sumRegion"]
        [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],
         [2,1,4,3],[1,1,2,2],[1,2,2,4]]
Output: [null,8,11,12]
Explanation: e.g. rows 1..2, cols 1..2 contain 6+3+2+0 = 11.
```

**Example 2**
```text
Input:  ["NumMatrix","sumRegion","sumRegion"]
        [[[[1,2],[3,4]]],[0,0,1,1],[1,0,1,1]]
Output: [null,10,7]
```

## Constraints

- `1 <= m, n <= 200` (matrix is `m x n`)
- `-10^4 <= matrix[i][j] <= 10^4`
- `0 <= row1 <= row2 < m`, `0 <= col1 <= col2 < n`
- At most `10^4` calls to `sumRegion`.

## Starter Code & Test Cases

```python
import random
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        pass  # your code here

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pass  # your code here


def brute(matrix, r1, c1, r2, c2):
    return sum(matrix[r][c] for r in range(r1, r2 + 1) for c in range(c1, c2 + 1))


if __name__ == "__main__":
    grid = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    nm = NumMatrix(grid)
    assert nm.sumRegion(2, 1, 4, 3) == 8
    assert nm.sumRegion(1, 1, 2, 2) == 11
    assert nm.sumRegion(1, 2, 2, 4) == 12
    assert nm.sumRegion(0, 0, 4, 4) == sum(map(sum, grid))

    nm2 = NumMatrix([[1, 2], [3, 4]])
    assert nm2.sumRegion(0, 0, 1, 1) == 10
    assert nm2.sumRegion(1, 0, 1, 1) == 7
    assert nm2.sumRegion(0, 1, 0, 1) == 2

    assert NumMatrix([[-5]]).sumRegion(0, 0, 0, 0) == -5

    rng = random.Random(1)
    m, n = 30, 17
    big = [[rng.randint(-10**4, 10**4) for _ in range(n)] for _ in range(m)]
    nm3 = NumMatrix(big)
    for _ in range(300):
        r1, r2 = sorted(rng.randrange(m) for _ in range(2))
        c1, c2 = sorted(rng.randrange(n) for _ in range(2))
        assert nm3.sumRegion(r1, c1, r2, c2) == brute(big, r1, c1, r2, c2)
    print("All tests passed!")
```
