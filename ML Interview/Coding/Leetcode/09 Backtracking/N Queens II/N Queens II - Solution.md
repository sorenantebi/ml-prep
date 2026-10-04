---
topic: "Backtracking"
difficulty: Hard
leetcode: https://leetcode.com/problems/n-queens-ii/
neetcode: https://neetcode.io/problems/n-queens-ii
---
# N Queens II - Solution

**Question:** [[N Queens II - Question]] · **Difficulty:** Hard

## Intuition

Same search as N-Queens — one queen per row, avoiding attacked columns and diagonals — but we only count leaves. Since no boards are built, represent the occupied columns, diagonals, and anti-diagonals as **bitmasks** relative to the current row: shifting the diagonal masks by one bit per row moves the attacks down the board, and `available = ~(cols | diag | anti) & full` lists safe columns in one operation.

## Approach

1. `full = (1 << n) - 1`.
2. `dfs(cols, diag, anti)`: if `cols == full`, a queen is in every column — count 1.
3. `avail = full & ~(cols | diag | anti)`. While `avail`: take the lowest set bit `bit = avail & -avail`, clear it, and recurse with `cols | bit`, `(diag | bit) << 1`, `(anti | bit) >> 1`.
4. Sum the counts.

## Code

```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        full = (1 << n) - 1

        def dfs(cols: int, diag: int, anti: int) -> int:
            if cols == full:
                return 1
            count = 0
            avail = full & ~(cols | diag | anti)  # safe columns in this row
            while avail:
                bit = avail & -avail             # lowest available column
                avail ^= bit
                # diagonals shift one column per row as we move down
                count += dfs(cols | bit, ((diag | bit) << 1) & full, (anti | bit) >> 1)
            return count

        return dfs(0, 0, 0)
```

## Complexity

- **Time:** `O(n!)` — at most `n - r` choices in row `r`, each step `O(1)` with bit operations.
- **Space:** `O(n)` — recursion depth.

## Other Approaches

- **Set-based backtracking:** identical to N-Queens with `cols`, `r - c`, `r + c` sets, incrementing a counter at `r == n` — Time `O(n!)`, Space `O(n)`.

## Key Takeaway

When only a count is needed, drop the board and encode constraints as bitmasks; `x & -x` extracts the lowest available choice.
