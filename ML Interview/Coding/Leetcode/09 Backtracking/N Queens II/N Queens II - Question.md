---
topic: "Backtracking"
difficulty: Hard
leetcode: https://leetcode.com/problems/n-queens-ii/
neetcode: https://neetcode.io/problems/n-queens-ii
---
# N Queens II

**Topic:** [[09 Backtracking|Backtracking]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/n-queens-ii/) · [NeetCode](https://neetcode.io/problems/n-queens-ii)

**Solve it in:** [[N Queens II]] · **Answer:** [[N Queens II - Solution]]

## Problem

The n-queens puzzle asks to place `n` queens on an `n x n` chessboard so that no two queens share a row, column, or diagonal.

Given `n`, return the **number** of distinct valid placements (you do not need to return the boards themselves).

## Examples

**Example 1**
```text
Input: n = 4
Output: 2
```

**Example 2**
```text
Input: n = 1
Output: 1
```

## Constraints

- `1 <= n <= 9`

## Starter Code & Test Cases

```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.totalNQueens(4) == 2
    assert s.totalNQueens(1) == 1
    assert s.totalNQueens(2) == 0
    assert s.totalNQueens(3) == 0
    assert s.totalNQueens(5) == 10
    assert s.totalNQueens(6) == 4
    assert s.totalNQueens(8) == 92
    assert s.totalNQueens(9) == 352
    print("All tests passed!")
```
