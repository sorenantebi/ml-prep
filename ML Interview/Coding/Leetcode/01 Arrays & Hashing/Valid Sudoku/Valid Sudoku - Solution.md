---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/valid-sudoku/
neetcode: https://neetcode.io/problems/valid-sudoku
---
# Valid Sudoku - Solution

**Question:** [[Valid Sudoku - Question]] · **Difficulty:** Medium

## Intuition

Each filled cell belongs to exactly one row, one column, and one `3 x 3` box (box index `(r // 3, c // 3)`). Keep a set of seen digits for every row, column, and box; scanning the board once, a digit already present in any of its three sets means the board is invalid.

## Approach

1. Create 9 sets for rows, 9 for columns, and 9 for boxes.
2. For each cell `(r, c)` with digit `d` (skip `"."`):
   - Compute `b = (r // 3) * 3 + c // 3`.
   - If `d` is in `rows[r]`, `cols[c]`, or `boxes[b]`, return `False`.
   - Otherwise add `d` to all three sets.
3. Return `True` after the scan.

## Code

```python
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                d = board[r][c]
                if d == ".":
                    continue
                b = (r // 3) * 3 + c // 3  # index of the 3x3 box
                if d in rows[r] or d in cols[c] or d in boxes[b]:
                    return False
                rows[r].add(d)
                cols[c].add(d)
                boxes[b].add(d)
        return True
```

## Complexity

- **Time:** `O(1)` — the board is fixed at 81 cells (`O(n^2)` for a general `n x n` board).
- **Space:** `O(1)` — 27 sets of at most 9 digits each (`O(n^2)` in general).

## Other Approaches

- **Three separate passes:** validate all rows, then all columns, then all boxes — same complexity, more code.
- **Bitmasks:** replace each set with a 9-bit integer and test `mask & (1 << d)` — Time `O(1)`, Space `O(1)`, faster constants.

## Key Takeaway

Map each cell to its constraint groups with simple index arithmetic (`(r // 3) * 3 + c // 3` for the box) and use one hash set per group to detect conflicts in a single pass.
