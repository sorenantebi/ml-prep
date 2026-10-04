---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/word-search/
neetcode: https://neetcode.io/problems/search-for-word
---
# Word Search - Solution

**Question:** [[Word Search - Question]] · **Difficulty:** Medium

## Intuition

Try every cell as a starting point and run a DFS that matches `word` one character at a time, moving to the four neighbors. Mark a cell as visited while it is on the current path (temporarily overwrite it) and restore it when backtracking, so it can be used by other paths.

## Approach

1. Quick prune: if the board lacks enough copies of some letter in `word`, return `false`. Optionally reverse `word` if its last letter is rarer than its first, to cut branching early.
2. `dfs(r, c, i)`: return `true` if `i == len(word)`; return `false` if out of bounds or `board[r][c] != word[i]`.
3. Temporarily set `board[r][c] = "#"`, recurse into the four neighbors with `i + 1`, then restore the cell.
4. Return `true` if any start cell's DFS succeeds.

## Code

```python
from typing import List
from collections import Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        have = Counter(ch for row in board for ch in row)
        need = Counter(word)
        if any(have[ch] < cnt for ch, cnt in need.items()):
            return False  # not enough letters on the board
        if have[word[0]] > have[word[-1]]:
            word = word[::-1]  # start from the rarer end to prune sooner

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
            board[r][c] = "#"  # mark as used on the current path
            found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1)
                     or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            board[r][c] = word[i]  # restore (backtrack)
            return found

        return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))
```

## Complexity

- **Time:** `O(m * n * 3^L)` — each of the `m*n` starts explores at most 3 new directions per step for `L = len(word)` steps.
- **Space:** `O(L)` — recursion depth (the board is marked in place).

## Other Approaches

- **Visited set instead of in-place marking:** store `(r, c)` on the path in a set — same time, `O(L)` extra space, leaves the board untouched throughout.

## Key Takeaway

Grid path search = DFS from every cell with in-place "visited" marking that is undone on return; frequency checks and starting from the rarer end are cheap, powerful prunes.
