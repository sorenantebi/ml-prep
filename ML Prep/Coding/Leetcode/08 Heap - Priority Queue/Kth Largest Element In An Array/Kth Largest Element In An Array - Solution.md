---
topic: "Heap / Priority Queue"
difficulty: Medium
leetcode: https://leetcode.com/problems/kth-largest-element-in-an-array/
neetcode: https://neetcode.io/problems/kth-largest-element-in-an-array
---
# Kth Largest Element In An Array - Solution

**Question:** [[Kth Largest Element In An Array - Question]] · **Difficulty:** Medium

## Intuition

Only the `k` largest values matter. Maintain a **min-heap of size `k`** while scanning: after processing all elements, the heap holds exactly the `k` largest, and its root is the smallest of them — the `k`-th largest overall.

## Approach

1. Heapify the first `k` elements into a min-heap.
2. For every remaining element, if it is larger than the heap root, replace the root with it (`heapreplace`).
3. Return the heap root.

## Code

```python
from typing import List
import heapq


class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		heap = nums[:k]
		heapq.heapify(heap)
		for x in nums[k:]:
			if x > heap[0]:
				heapq.heapreplace(heap, x)  # pop smallest and push x in one step
		return heap[0]
```

## Complexity

- **Time:** `O(n log k)` — each element triggers at most one `O(log k)` heap operation.
- **Space:** `O(k)` — the heap.

## Other Approaches

- **Quickselect (Hoare / Lomuto partition with random pivot):** partition around a pivot and recurse into the side containing index `n - k` — Time `O(n)` average / `O(n^2)` worst, Space `O(1)` extra.
- **Sort:** `sorted(nums)[-k]` — Time `O(n log n)`, Space `O(n)`.

## Key Takeaway

k-th largest = root of a size-`k` min-heap (`O(n log k)`); mention quickselect for `O(n)` average if the interviewer pushes for better.
