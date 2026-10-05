---
topic: "Intervals"
difficulty: Easy
leetcode: https://leetcode.com/problems/meeting-rooms/
neetcode: https://neetcode.io/problems/meeting-schedule
---
# Meeting Rooms - Solution

**Question:** [[Meeting Rooms - Question]] · **Difficulty:** Easy

## Intuition

If meetings are sorted by start time, any conflict must occur between two **adjacent** meetings: if meeting `i` doesn't overlap meeting `i + 1`, it cannot overlap any later one either, since they start even later. So sort and compare each meeting's start with the previous meeting's end.

## Approach

1. Sort intervals by start time.
2. For each consecutive pair, if `intervals[i][0] < intervals[i - 1][1]`, the meetings overlap → return `False`.
3. If no pair conflicts, return `True` (this also covers 0 or 1 meetings).

## Code

```python
from typing import List

class Solution:
	def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
		intervals.sort(key=lambda x: x[0])
		for i in range(1, len(intervals)):
			if intervals[i][0] < intervals[i - 1][1]:   # strict: back-to-back is OK
				return False
		return True
```

## Complexity

- **Time:** `O(n log n)` — sorting dominates.
- **Space:** `O(1)` extra (besides the sort's internal buffer).

## Other Approaches

- **Compare all pairs:** check every pair for overlap — Time `O(n^2)`, Space `O(1)`.

## Key Takeaway

After sorting intervals by start, overlap checks only need adjacent pairs — a recurring simplification in interval problems.
