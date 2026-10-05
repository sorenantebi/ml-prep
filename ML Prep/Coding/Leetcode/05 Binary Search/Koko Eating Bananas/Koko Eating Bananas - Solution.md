---
topic: "Binary Search"
difficulty: Medium
leetcode: https://leetcode.com/problems/koko-eating-bananas/
neetcode: https://neetcode.io/problems/eating-bananas
---
# Koko Eating Bananas - Solution

**Question:** [[Koko Eating Bananas - Question]] · **Difficulty:** Medium

## Intuition

If Koko can finish at speed `k`, she can also finish at any faster speed, so feasibility is monotone in `k`. Binary search the smallest feasible `k` in `[1, max(piles)]`, where checking a speed costs one pass: hours needed = `sum(ceil(p / k))`.

## Approach

1. Search `lo = 1`, `hi = max(piles)` (eating the largest pile in one hour always works since `h >= n`).
2. While `lo < hi`: `mid = (lo + hi) // 2`; compute `hours = sum((p + mid - 1) // mid)`.
3. If `hours <= h`, `mid` works — try slower: `hi = mid`; else `lo = mid + 1`.
4. Return `lo`.

## Code

```python
from typing import List


class Solution:
	def minEatingSpeed(self, piles: List[int], h: int) -> int:
		lo, hi = 1, max(piles)
		while lo < hi:
			mid = (lo + hi) // 2
			hours = sum((p + mid - 1) // mid for p in piles)  # ceil division
			if hours <= h:
				hi = mid        # feasible, look for a smaller speed
			else:
				lo = mid + 1
		return lo
```

## Complexity

- **Time:** `O(n log M)` where `M = max(piles)` — `log M` feasibility checks, each `O(n)`.
- **Space:** `O(1)`.

## Other Approaches

- **Linear search on speed:** try `k = 1, 2, …` until feasible — Time `O(n · M)`, Space `O(1)`.

## Key Takeaway

"Minimize a value such that a monotone feasibility check passes" → binary search on the answer space with an O(n) check.
