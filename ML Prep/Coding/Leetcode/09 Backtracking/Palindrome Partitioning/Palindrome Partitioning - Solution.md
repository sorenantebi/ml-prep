---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/palindrome-partitioning/
neetcode: https://neetcode.io/problems/palindrome-partitioning
---
# Palindrome Partitioning - Solution

**Question:** [[Palindrome Partitioning - Question]] · **Difficulty:** Medium

## Intuition

Choose the first piece, then recursively partition the rest: from position `start`, try every end index `end` such that `s[start:end+1]` is a palindrome, add it to the path, and recurse from `end + 1`. Precomputing a palindrome table with DP makes each check `O(1)`.

## Approach

1. Build `pal[i][j]` = whether `s[i..j]` is a palindrome: `s[i] == s[j]` and (`j - i < 2` or `pal[i+1][j-1]`), filling `i` from the end.
2. `dfs(start)`: if `start == n`, record a copy of `path`.
3. For each `end` from `start` to `n - 1` with `pal[start][end]`: append `s[start:end+1]`, recurse with `dfs(end + 1)`, pop.

## Code

```python
from typing import List


class Solution:
	def partition(self, s: str) -> List[List[str]]:
		n = len(s)
		pal = [[False] * n for _ in range(n)]
		for i in range(n - 1, -1, -1):
			for j in range(i, n):
				# outer chars match and the inside (if any) is a palindrome
				pal[i][j] = s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1])

		res, path = [], []

		def dfs(start: int) -> None:
			if start == n:
				res.append(path[:])
				return
			for end in range(start, n):
				if pal[start][end]:
					path.append(s[start:end + 1])
					dfs(end + 1)
					path.pop()

		dfs(0)
		return res
```

## Complexity

- **Time:** `O(n * 2^n)` — up to `2^(n-1)` partitions, each copied/built in `O(n)`; the DP table is `O(n^2)`.
- **Space:** `O(n^2)` for the palindrome table plus `O(n)` recursion (output excluded).

## Other Approaches

- **Check palindromes on the fly:** test `sub == sub[::-1]` inside the DFS instead of a table — Time `O(n^2 * 2^n)` worst case, Space `O(n)`.

## Key Takeaway

"All ways to split a string" = backtracking over the end of the first piece; precompute validity of substrings (here palindromes) so each branch check is `O(1)`.
