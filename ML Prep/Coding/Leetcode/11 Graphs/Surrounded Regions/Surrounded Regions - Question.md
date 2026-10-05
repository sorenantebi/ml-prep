---
topic: "Graphs"
difficulty: Medium
leetcode: https://leetcode.com/problems/surrounded-regions/
neetcode: https://neetcode.io/problems/surrounded-regions
---
# Surrounded Regions

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/surrounded-regions/) · [NeetCode](https://neetcode.io/problems/surrounded-regions)

**Solve it in:** [[Surrounded Regions]] · **Answer:** [[Surrounded Regions - Solution]]

## Problem

You are given an `m x n` board of characters `'X'` and `'O'`. A **region** is a group of `'O'` cells connected 4-directionally. A region is **surrounded** if none of its cells lie on the border of the board (i.e. it is completely enclosed by `'X'` cells).

Capture every surrounded region by flipping all of its `'O'` cells to `'X'`. Modify the board **in place**; the function returns nothing. Regions touching the border remain unchanged.

## Examples

**Example 1**
```text
Input: board = [["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","O","X"],
                ["X","O","X","X"]]
Output:        [["X","X","X","X"],
                ["X","X","X","X"],
                ["X","X","X","X"],
                ["X","O","X","X"]]
Explanation: The bottom 'O' is on the border, so it is not captured.
```

**Example 2**
```text
Input: board = [["X"]]
Output: [["X"]]
```

## Constraints

- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def solve(self, board: List[List[str]]) -> None:
		"""Do not return anything, modify board in-place instead."""
		pass  # your code here


def g(rows):
	return [list(r) for r in rows]


if __name__ == "__main__":
	s = Solution()
	cases = [
		(["XXXX", "XOOX", "XXOX", "XOXX"], ["XXXX", "XXXX", "XXXX", "XOXX"]),
		(["X"], ["X"]),
		(["O"], ["O"]),
		(["OOO", "OOO", "OOO"], ["OOO", "OOO", "OOO"]),
		(["XXX", "XOX", "XXX"], ["XXX", "XXX", "XXX"]),
		(["XOXX", "XOOX", "XXXX", "XOOX"], ["XOXX", "XOOX", "XXXX", "XOOX"]),
		(["XXXXX", "XOOOX", "XOXOX", "XOOOX", "XXXXX"], ["XXXXX"] * 5),
	]
	for board_in, expected in cases:
		board = g(board_in)
		s.solve(board)
		assert board == g(expected), (board_in, board)
	print("All tests passed!")
```
