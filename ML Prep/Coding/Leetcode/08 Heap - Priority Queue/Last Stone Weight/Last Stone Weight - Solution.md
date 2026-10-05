---
topic: "Heap / Priority Queue"
difficulty: Easy
leetcode: https://leetcode.com/problems/last-stone-weight/
neetcode: https://neetcode.io/problems/last-stone-weight
---
# Last Stone Weight - Solution

**Question:** [[Last Stone Weight - Question]] · **Difficulty:** Easy

## Intuition

Each round needs the two current maximums, and the result (if any) goes back into the pool. That "repeatedly extract max and re-insert" pattern is exactly what a **max-heap** does efficiently. Python only has a min-heap, so store negated weights.

## Approach

1. Build a max-heap by negating every weight and heapifying.
2. While at least two stones remain, pop the heaviest `y` and the next `x`.
3. If `y > x`, push `y - x` back.
4. Return the remaining stone's weight, or `0` if the heap is empty.

## Code

```python
from typing import List
import heapq


class Solution:
	def lastStoneWeight(self, stones: List[int]) -> int:
		heap = [-s for s in stones]  # negate to simulate a max-heap
		heapq.heapify(heap)
		while len(heap) > 1:
			y = -heapq.heappop(heap)
			x = -heapq.heappop(heap)
			if y != x:
				heapq.heappush(heap, -(y - x))
		return -heap[0] if heap else 0
```

## Complexity

- **Time:** `O(n log n)` — at most `n - 1` rounds, each with `O(log n)` heap operations.
- **Space:** `O(n)` — the heap (a copy of the input).

## Other Approaches

- **Sort every round:** re-sort the list and take the last two — Time `O(n^2 log n)`, Space `O(1)` extra.
- **Bucket / counting by weight:** since weights are `<= 1000`, walk a count array from the top — Time `O(n + W)`, Space `O(W)`.

## Key Takeaway

"Repeatedly take the largest items and put a result back" is a max-heap simulation; in Python, negate values to use `heapq` as a max-heap.
