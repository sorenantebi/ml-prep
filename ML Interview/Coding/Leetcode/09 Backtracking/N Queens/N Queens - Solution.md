---
topic: "Backtracking"
difficulty: Hard
leetcode: https://leetcode.com/problems/n-queens/
neetcode: https://neetcode.io/problems/n-queens
---
# N Queens - Solution

**Question:** [[N Queens - Question]] · **Difficulty:** Hard

## Intuition

Exactly one queen goes in each row, so place queens row by row and only choose a column that is not attacked. A square `(r, c)` is attacked if its column, its diagonal (`r - c` constant), or its anti-diagonal (`r + c` constant) already has a queen — three sets give `O(1)` checks, and backtracking removes the queen when a branch is done.

## Approach

1. Keep sets `cols`, `diag` (`r - c`), `anti` (`r + c`) and an array `queen_col[r]`.
2. `dfs(r)`: if `r == n`, convert `queen_col` into board strings and record them.
3. For each column `c`: skip if `c`, `r - c`, or `r + c` is taken; otherwise add to all three sets, set `queen_col[r] = c`, recurse on `r + 1`, then remove from the sets.

## Code

```python
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queen_col = [0] * n
        cols, diag, anti = set(), set(), set()

        def dfs(r: int) -> None:
            if r == n:
                res.append(["." * c + "Q" + "." * (n - c - 1) for c in queen_col])
                return
            for c in range(n):
                if c in cols or (r - c) in diag or (r + c) in anti:
                    continue  # square is attacked
                cols.add(c); diag.add(r - c); anti.add(r + c)
                queen_col[r] = c
                dfs(r + 1)
                cols.remove(c); diag.remove(r - c); anti.remove(r + c)

        dfs(0)
        return res
```

## Complexity

- **Time:** `O(n!)` — row `r` has at most `n - r` free columns; building each board adds `O(n^2)` per solution.
- **Space:** `O(n)` — sets, column array, and recursion depth (output excluded).

## Other Approaches

- **Validate by scanning the board:** for each candidate square, scan its column and diagonals on a char grid — Time `O(n! * n)`, Space `O(n^2)`.
- **Bitmasks:** represent `cols`, `diag`, `anti` as integers and iterate available bits — same asymptotic bound, much faster constants.

## Key Takeaway

For N-Queens, index diagonals by `r - c` and anti-diagonals by `r + c`; place one queen per row and backtrack with three "occupied" sets.
