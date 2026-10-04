---
topic: "Backtracking"
difficulty: Hard
leetcode: https://leetcode.com/problems/n-queens/
neetcode: https://neetcode.io/problems/n-queens
---
# N Queens

**Topic:** [[09 Backtracking|Backtracking]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/n-queens/) · [NeetCode](https://neetcode.io/problems/n-queens)

**Solve it in:** [[N Queens]] · **Answer:** [[N Queens - Solution]]

## Problem

Place `n` queens on an `n x n` chessboard so that no two queens attack each other — no two share a row, a column, or a diagonal.

Given `n`, return **all** distinct solutions in any order. Each solution is a list of `n` strings representing the rows of the board, where `'Q'` marks a queen and `'.'` an empty square.

## Examples

**Example 1**
```text
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
```

**Example 2**
```text
Input: n = 1
Output: [["Q"]]
```

## Constraints

- `1 <= n <= 9`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pass  # your code here


def is_valid_board(board: List[str]) -> bool:
    n = len(board)
    queens = [(r, row.index("Q")) for r, row in enumerate(board)]
    if any(row.count("Q") != 1 or len(row) != n for row in board):
        return False
    cols = {c for _, c in queens}
    diag = {r - c for r, c in queens}
    anti = {r + c for r, c in queens}
    return len(cols) == len(diag) == len(anti) == n


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.solveNQueens(4)) == sorted([[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])
    assert s.solveNQueens(1) == [["Q"]]
    assert s.solveNQueens(2) == []
    assert s.solveNQueens(3) == []
    counts = {5: 10, 6: 4, 7: 40, 8: 92}
    for n, cnt in counts.items():
        res = s.solveNQueens(n)
        assert len(res) == cnt and len({tuple(b) for b in res}) == cnt
        assert all(is_valid_board(b) for b in res)
    print("All tests passed!")
```
