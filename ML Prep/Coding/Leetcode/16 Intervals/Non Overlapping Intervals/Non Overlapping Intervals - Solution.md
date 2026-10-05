---
topic: "Intervals"
difficulty: Medium
leetcode: https://leetcode.com/problems/non-overlapping-intervals/
neetcode: https://neetcode.io/problems/non-overlapping-intervals
---
# Non Overlapping Intervals - Solution

**Question:** [[Non Overlapping Intervals - Question]] · **Difficulty:** Medium

## Intuition

Minimizing removals is the same as maximizing the number of intervals we keep without overlap — the classic activity-selection problem. Greedily keeping the interval that **ends earliest** leaves the most room for the rest, so sort by end time and keep every interval that starts at or after the last kept end.

## Approach

1. Sort intervals by end.
2. Track `prev_end` of the last kept interval (initially `-inf`) and a `removed` counter.
3. For each interval: if `start >= prev_end`, keep it (`prev_end = end`); otherwise it overlaps, so count it as removed.
4. Return `removed`.

## Code

```python
from typing import List

class Solution:
	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		intervals.sort(key=lambda x: x[1])   # earliest end first
		removed = 0
		prev_end = float("-inf")
		for start, end in intervals:
			if start >= prev_end:             # touching endpoints are fine
				prev_end = end
			else:
				removed += 1                  # overlaps the kept interval -> drop it
		return removed
```

## Complexity

- **Time:** `O(n log n)` — sorting dominates; the scan is `O(n)`.
- **Space:** `O(1)` extra (besides the sort's internal buffer).

## Other Approaches

- **Sort by start, and on overlap drop the one with the larger end:** keep `prev_end = min(prev_end, end)` when overlapping — Time `O(n log n)`, Space `O(1)`.
- **DP (longest chain of non-overlapping intervals):** `dp[i] = 1 + max(dp[j])` over compatible `j` — Time `O(n^2)` (or `O(n log n)` with binary search), Space `O(n)`.

## Key Takeaway

"Remove fewest to make non-overlapping" = "keep as many as possible" = activity selection: sort by end time and greedily keep compatible intervals.
