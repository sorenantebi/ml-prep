---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/valid-sudoku/
neetcode: https://neetcode.io/problems/valid-sudoku
---
# Valid Sudoku

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/valid-sudoku/) · [NeetCode](https://neetcode.io/problems/valid-sudoku)

**Solve it in:** [[Valid Sudoku]] · **Answer:** [[Valid Sudoku - Solution]]

## Problem

You are given a partially filled `9 x 9` Sudoku board as a grid of strings, where each cell is a digit `"1"`–`"9"` or `"."` for an empty cell. Decide whether the board is **valid** so far, meaning that among the filled cells:

1. No row contains the same digit twice.
2. No column contains the same digit twice.
3. None of the nine `3 x 3` sub-boxes contains the same digit twice.

Only the filled cells need to be checked. A valid board does not have to be solvable.

## Examples

**Example 1**
```text
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

**Example 2**
```text
Input: the same board, but with the top-left "5" replaced by "8"
Output: false
Explanation: column 0 (and the top-left box) now contains two 8s.
```

## Constraints

- `board.length == 9` and `board[i].length == 9`
- `board[i][j]` is a digit `"1"`–`"9"` or `"."`.

## Starter Code & Test Cases

```python
import copy
from typing import List


class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		pass  # your code here


BASE = [
	["5", "3", ".", ".", "7", ".", ".", ".", "."],
	["6", ".", ".", "1", "9", "5", ".", ".", "."],
	[".", "9", "8", ".", ".", ".", ".", "6", "."],
	["8", ".", ".", ".", "6", ".", ".", ".", "3"],
	["4", ".", ".", "8", ".", "3", ".", ".", "1"],
	["7", ".", ".", ".", "2", ".", ".", ".", "6"],
	[".", "6", ".", ".", ".", ".", "2", "8", "."],
	[".", ".", ".", "4", "1", "9", ".", ".", "5"],
	[".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


def with_cells(*changes):
	b = copy.deepcopy(BASE)
	for r, c, v in changes:
		b[r][c] = v
	return b


if __name__ == "__main__":
	s = Solution()
	assert s.isValidSudoku(copy.deepcopy(BASE)) is True
	assert s.isValidSudoku(with_cells((0, 0, "8"))) is False           # column + box clash
	assert s.isValidSudoku([["."] * 9 for _ in range(9)]) is True      # empty board
	assert s.isValidSudoku(with_cells((0, 6, "5"))) is False           # row clash only
	assert s.isValidSudoku(with_cells((8, 0, "4"))) is False           # column clash only
	assert s.isValidSudoku(with_cells((2, 2, "5"))) is False           # box clash only
	full = [[str((r * 3 + r // 3 + c) % 9 + 1) for c in range(9)] for r in range(9)]
	assert s.isValidSudoku(full) is True                               # a complete valid grid
	print("All tests passed!")
```
