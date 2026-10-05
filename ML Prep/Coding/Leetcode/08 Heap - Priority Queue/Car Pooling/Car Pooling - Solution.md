---
topic: "Heap / Priority Queue"
difficulty: Medium
leetcode: https://leetcode.com/problems/car-pooling/
neetcode: https://neetcode.io/problems/car-pooling
---
# Car Pooling - Solution

**Question:** [[Car Pooling - Question]] · **Difficulty:** Medium

## Intuition

Process pickups in order of location; before boarding a group at `from`, drop off everyone whose trip ended at or before `from`. A **min-heap keyed by drop-off location** tells us exactly which riders leave next, so we can maintain the current load and check it against capacity after each pickup.

## Approach

1. Sort trips by start location.
2. Keep a min-heap of `(to, numPassengers)` for passengers currently in the car and a running `load`.
3. For each trip `(num, start, end)`: pop all heap entries with `to <= start`, subtracting their passengers from `load`.
4. Add `num` to `load`; if `load > capacity`, return `false`. Push `(end, num)`.
5. If all trips are processed, return `true`.

## Code

```python
from typing import List
import heapq


class Solution:
	def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
		trips.sort(key=lambda t: t[1])
		heap = []  # (dropoff location, passengers) of riders currently onboard
		load = 0
		for num, start, end in trips:
			while heap and heap[0][0] <= start:  # drop-offs happen before pickups
				load -= heapq.heappop(heap)[1]
			load += num
			if load > capacity:
				return False
			heapq.heappush(heap, (end, num))
		return True
```

## Complexity

- **Time:** `O(n log n)` — sorting plus one push and one pop per trip.
- **Space:** `O(n)` — the heap.

## Other Approaches

- **Difference array / line sweep:** add `num` at `from`, subtract at `to` over the location range (`<= 1000`), then prefix-sum and check every point — Time `O(n + L)`, Space `O(L)`.

## Key Takeaway

Interval-overlap load problems: sort by start and use a min-heap of end times to expire finished intervals (same as Meeting Rooms II); with small coordinates, a difference array is even simpler.
