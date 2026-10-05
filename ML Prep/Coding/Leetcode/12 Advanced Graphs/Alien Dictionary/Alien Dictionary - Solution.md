---
topic: "Advanced Graphs"
difficulty: Hard
leetcode: https://leetcode.com/problems/alien-dictionary/
neetcode: https://neetcode.io/problems/foreign-dictionary
---
# Alien Dictionary - Solution

**Question:** [[Alien Dictionary - Question]] · **Difficulty:** Hard

## Intuition

Each adjacent pair of words gives at most one ordering fact: at the first differing position, the letter in the first word precedes the letter in the second. These facts form a directed graph over letters, and any **topological order** of it is a valid alphabet. A cycle — or a longer word placed before its own prefix — makes the input invalid.

## Approach

1. Create a node (with in-degree 0) for every letter that appears.
2. For each adjacent pair `(w1, w2)`: if `w1` is longer and `w2` is a prefix of it, return `""`. Otherwise find the first differing letters `a != b` and add edge `a -> b` (once).
3. Run Kahn's algorithm: start with in-degree-0 letters, pop, append to the result, and decrement neighbours' in-degrees.
4. If the result doesn't contain every letter, there was a cycle: return `""`.

## Code

```python
from typing import List
from collections import deque


class Solution:
	def alienOrder(self, words: List[str]) -> str:
		adj = {ch: set() for w in words for ch in w}
		indeg = {ch: 0 for ch in adj}

		for w1, w2 in zip(words, words[1:]):
			min_len = min(len(w1), len(w2))
			if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
				return ""  # longer word before its own prefix -> invalid
			for a, b in zip(w1, w2):
				if a != b:
					if b not in adj[a]:  # avoid double-counting in-degree
						adj[a].add(b)
						indeg[b] += 1
					break  # only the first difference carries information

		queue = deque(ch for ch in indeg if indeg[ch] == 0)
		order = []
		while queue:
			ch = queue.popleft()
			order.append(ch)
			for nxt in adj[ch]:
				indeg[nxt] -= 1
				if indeg[nxt] == 0:
					queue.append(nxt)

		return "".join(order) if len(order) == len(adj) else ""  # cycle -> ""
```

## Complexity

- **Time:** `O(C)` — `C` is the total number of characters across all words (building edges), plus `O(U + E)` for the topological sort with `U <= 26` letters.
- **Space:** `O(U + E)` — at most `26` nodes and `26^2` edges, i.e. `O(1)` relative to input size.

## Other Approaches

- **DFS topological sort with 3-colour cycle detection:** post-order DFS, reverse at the end, return `""` on a back edge — Time `O(C)`, Space `O(U + E)`.

## Key Takeaway

Turn "sorted list under an unknown order" into pairwise precedence edges (only the first difference matters), then topologically sort; remember the prefix edge case.
