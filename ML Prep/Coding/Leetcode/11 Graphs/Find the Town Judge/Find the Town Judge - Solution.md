---
topic: "Graphs"
difficulty: Easy
leetcode: https://leetcode.com/problems/find-the-town-judge/
neetcode: https://neetcode.io/problems/find-the-town-judge
---
# Find the Town Judge - Solution

**Question:** [[Find the Town Judge - Question]] · **Difficulty:** Easy

## Intuition

Model trust as a directed graph. The judge has out-degree 0 and in-degree `n - 1`. Combine both into one score: `in-degree - out-degree`. Only the judge can reach exactly `n - 1`, since anyone with an outgoing edge loses at least 1 and nobody can have in-degree above `n - 1`.

## Approach

1. Create an array `score` of size `n + 1`.
2. For every pair `[a, b]`: decrement `score[a]` (a trusts someone) and increment `score[b]` (b is trusted).
3. Return the person `i` with `score[i] == n - 1`, or `-1` if none exists.

## Code

```python
from typing import List


class Solution:
	def findJudge(self, n: int, trust: List[List[int]]) -> int:
		score = [0] * (n + 1)  # in-degree minus out-degree
		for a, b in trust:
			score[a] -= 1
			score[b] += 1
		for person in range(1, n + 1):
			if score[person] == n - 1:
				return person
		return -1
```

## Complexity

- **Time:** `O(n + t)` — one pass over the `t` trust pairs and one over the people.
- **Space:** `O(n)` — the score array.

## Other Approaches

- **Two degree arrays:** keep separate `indeg` and `outdeg` arrays and look for `indeg == n-1 and outdeg == 0` — Time `O(n + t)`, Space `O(n)`.

## Key Takeaway

Many "special node" graph questions reduce to degree counting; folding in- and out-degree into one net score is a neat space-saving trick.
