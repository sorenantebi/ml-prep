---
topic: "Heap / Priority Queue"
difficulty: Hard
leetcode: https://leetcode.com/problems/find-median-from-data-stream/
neetcode: https://neetcode.io/problems/find-median-in-a-data-stream
---
# Find Median From Data Stream - Solution

**Question:** [[Find Median From Data Stream - Question]] · **Difficulty:** Hard

## Intuition

Split the numbers into a **lower half** and an **upper half**. If the lower half is a max-heap and the upper half a min-heap, the median only depends on their two roots. Keep every element of `low` `<=` every element of `high`, and keep the sizes balanced (`low` may have one extra), so the median is `low`'s root (odd count) or the average of both roots (even count).

## Approach

1. `low` is a max-heap (store negatives), `high` is a min-heap.
2. `addNum`: push `num` into `low`, then move `low`'s max into `high` — this keeps the ordering invariant.
3. If `high` now has more elements than `low`, move `high`'s min back into `low` — this keeps the size invariant.
4. `findMedian`: if `low` is larger, return its root; otherwise return the average of the two roots.

## Code

```python
import heapq


class MedianFinder:
	def __init__(self):
		self.low = []   # max-heap (negated) holding the smaller half
		self.high = []  # min-heap holding the larger half

	def addNum(self, num: int) -> None:
		# route through low so the largest of the small half moves up
		heapq.heappush(self.high, -heapq.heappushpop(self.low, -num))
		if len(self.high) > len(self.low):  # rebalance: low keeps the extra element
			heapq.heappush(self.low, -heapq.heappop(self.high))

	def findMedian(self) -> float:
		if len(self.low) > len(self.high):
			return float(-self.low[0])
		return (-self.low[0] + self.high[0]) / 2.0
```

## Complexity

- **Time:** `O(log n)` per `addNum` (a constant number of heap ops), `O(1)` per `findMedian`.
- **Space:** `O(n)` — all numbers are stored across the two heaps.

## Other Approaches

- **Sorted list with binary insertion:** `bisect.insort` then index the middle — Time `O(n)` per add, `O(1)` median, Space `O(n)`.
- **Counting buckets (follow-up for values in `[0, 100]`):** keep 101 counters and walk them to the middle — Time `O(1)` add, `O(100)` median, Space `O(1)`.

## Key Takeaway

Running median = two heaps (max-heap for the lower half, min-heap for the upper half) kept balanced; the median lives at the roots.
