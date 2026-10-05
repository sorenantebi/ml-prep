---
topic: "Backtracking"
difficulty: Hard
leetcode: https://leetcode.com/problems/word-break-ii/
neetcode: https://neetcode.io/problems/word-break-ii
---
# Word Break II - Solution

**Question:** [[Word Break II - Question]] · **Difficulty:** Hard

## Intuition

Backtrack over the first word: for every dictionary word that is a prefix of the remaining string, recurse on the rest and prepend that word to each sentence returned. Many suffixes are reached through different prefixes, so **memoize by start index** — each suffix's list of sentences is computed once (and an unbreakable suffix returns `[]` immediately on later visits).

## Approach

1. Put the words in a set and note the maximum word length.
2. `dfs(i)` returns all sentences for `s[i:]`; `dfs(len(s)) = [""]` (one empty sentence).
3. For each `j` from `i + 1` to `min(n, i + maxLen)`: if `s[i:j]` is a word, combine it with every sentence of `dfs(j)` (joining with a space unless the tail is empty).
4. Cache results per `i`; return `dfs(0)`.

## Code

```python
from typing import List
from functools import lru_cache


class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
		words = set(wordDict)
		max_len = max(map(len, words))
		n = len(s)

		@lru_cache(maxsize=None)
		def dfs(i: int) -> List[str]:
			if i == n:
				return [""]  # one way to segment the empty suffix
			out = []
			for j in range(i + 1, min(n, i + max_len) + 1):
				w = s[i:j]
				if w in words:
					for tail in dfs(j):
						out.append(w + " " + tail if tail else w)
			return out

		return dfs(0)
```

## Complexity

- **Time:** `O(n * 2^n)` worst case — there can be up to `2^(n-1)` sentences, each of length `O(n)`; memoization ensures each suffix is solved once.
- **Space:** `O(n * 2^n)` for the memoized sentence lists in the worst case (output-sized), plus `O(n)` recursion.

## Other Approaches

- **Plain backtracking without memo:** same DFS with a shared path — Time `O(n * 2^n)` worst case but re-explores dead-end suffixes repeatedly (e.g. `"aaa...ab"`).
- **Word Break I DP first:** compute `canBreak[i]` bottom-up and only backtrack into reachable suffixes — prunes dead branches, same worst-case output bound.

## Key Takeaway

"Return all segmentations" = backtracking over the next word + memoization by start index; the output can be exponential, so the goal is to avoid redundant work, not to beat the output size.
