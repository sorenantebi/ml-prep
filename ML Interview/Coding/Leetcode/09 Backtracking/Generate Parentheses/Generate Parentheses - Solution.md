---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/generate-parentheses/
neetcode: https://neetcode.io/problems/generate-parentheses
---
# Generate Parentheses - Solution

**Question:** [[Generate Parentheses - Question]] · **Difficulty:** Medium

## Intuition

Build the string one character at a time and only make moves that can still lead to a valid string: add `'('` while fewer than `n` have been used, and add `')'` only while it would close an open parenthesis (`close < open`). Every leaf of this pruned tree is a valid string, so no filtering is needed.

## Approach

1. `dfs(open, close)` with a shared `path` list.
2. If `len(path) == 2n`, record `"".join(path)`.
3. If `open < n`: append `'('`, recurse with `open + 1`, pop.
4. If `close < open`: append `')'`, recurse with `close + 1`, pop.

## Code

```python
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, path = [], []

        def dfs(open_: int, close: int) -> None:
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            if open_ < n:             # can still open a new pair
                path.append("(")
                dfs(open_ + 1, close)
                path.pop()
            if close < open_:         # only close what is open
                path.append(")")
                dfs(open_, close + 1)
                path.pop()

        dfs(0, 0)
        return res
```

## Complexity

- **Time:** `O(4^n / sqrt(n))` — the number of results is the `n`-th Catalan number, each built in `O(n)`.
- **Space:** `O(n)` — recursion depth and path (output excluded).

## Other Approaches

- **Brute force:** generate all `2^(2n)` strings and keep the valid ones — Time `O(n * 4^n)`, Space `O(n)`.
- **DP by closure number:** every valid string is `"(" + A + ")" + B` with `|A| + |B| = n - 1` pairs; combine smaller results — same output-bound complexity.

## Key Takeaway

Backtrack with constraints that keep every partial state valid (`open <= n`, `close <= open`) so you never generate invalid candidates.
