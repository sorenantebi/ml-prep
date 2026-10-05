---
topic: "Greedy"
difficulty: Medium
leetcode: https://leetcode.com/problems/valid-parenthesis-string/
neetcode: https://neetcode.io/problems/valid-parenthesis-string
---
# Valid Parenthesis String - Solution

**Question:** [[Valid Parenthesis String - Question]] · **Difficulty:** Medium

## Intuition

Instead of trying all choices for each `'*'`, track the **range** of possible open-paren counts: `lo` (fewest opens, treating stars as `')'` when possible) and `hi` (most opens, treating stars as `'('`). If `hi` ever drops below 0, there are too many `')'`. Clamp `lo` at 0 (we never need negative opens). The string is valid iff `lo == 0` at the end.

## Approach

1. `lo = hi = 0`.
2. For each char:
   - `'('`: `lo += 1`, `hi += 1`.
   - `')'`: `lo -= 1`, `hi -= 1`.
   - `'*'`: `lo -= 1`, `hi += 1`.
   - If `hi < 0`, return `False`. Set `lo = max(lo, 0)`.
3. Return `lo == 0`.

## Code

```python
class Solution:
	def checkValidString(self, s: str) -> bool:
		lo = hi = 0  # min / max possible number of unmatched '('
		for c in s:
			if c == "(":
				lo, hi = lo + 1, hi + 1
			elif c == ")":
				lo, hi = lo - 1, hi - 1
			else:  # '*' could be ')', '' or '('
				lo, hi = lo - 1, hi + 1
			if hi < 0:  # even with every '*' as '(', too many ')'
				return False
			lo = max(lo, 0)  # can't have negative open count
		return lo == 0
```

## Complexity

- **Time:** `O(n)` — single pass.
- **Space:** `O(1)` — two counters.

## Other Approaches

- **Two stacks:** stack of `'('` indices and of `'*'` indices; match `')'` with `'('` first, then `'*'`; finally match leftover `'('` with later `'*'` — Time `O(n)`, Space `O(n)`.
- **DP / memoized DFS on `(i, open_count)`:** try all three meanings for `'*'` — Time `O(n^2)`, Space `O(n^2)`.

## Key Takeaway

When wildcards create many possibilities for a counter, track the feasible interval `[lo, hi]` instead of each possibility.
