---
topic: "Binary Search"
difficulty: Medium
leetcode: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
neetcode: https://neetcode.io/problems/capacity-to-ship-packages-within-d-days
---
# Capacity to Ship Packages Within D Days - Solution

**Question:** [[Capacity to Ship Packages Within D Days - Question]] · **Difficulty:** Medium

## Intuition

A larger capacity never needs more days, so "can ship within `days` at capacity `c`" is monotone in `c`. The answer lies between `max(weights)` (every package must fit) and `sum(weights)` (one day), and a greedy day-by-day simulation checks any candidate capacity in linear time.

## Approach

1. Search `lo = max(weights)`, `hi = sum(weights)`.
2. Feasibility for capacity `c`: greedily fill the current day; when the next package would overflow, start a new day. Count the days used.
3. If days needed `<= days`, try smaller (`hi = mid`); else `lo = mid + 1`.
4. Return `lo`.

## Code

```python
from typing import List


class Solution:
	def shipWithinDays(self, weights: List[int], days: int) -> int:
		def days_needed(cap: int) -> int:
			used, load = 1, 0
			for w in weights:
				if load + w > cap:   # start a new day
					used += 1
					load = 0
				load += w
			return used

		lo, hi = max(weights), sum(weights)
		while lo < hi:
			mid = (lo + hi) // 2
			if days_needed(mid) <= days:
				hi = mid
			else:
				lo = mid + 1
		return lo
```

## Complexity

- **Time:** `O(n log S)` where `S = sum(weights)` — `log S` greedy checks of `O(n)` each.
- **Space:** `O(1)`.

## Other Approaches

- **Linear scan on capacity:** try capacities from `max(weights)` upwards until feasible — Time `O(n · S)`, Space `O(1)`.
- **DP over partitions:** minimize the max segment sum with `days` segments — Time `O(n^2 · days)`, Space `O(n · days)`.

## Key Takeaway

Same template as Koko / Split Array Largest Sum: binary search on the answer with a greedy feasibility check; choose bounds `[max, sum]`.
