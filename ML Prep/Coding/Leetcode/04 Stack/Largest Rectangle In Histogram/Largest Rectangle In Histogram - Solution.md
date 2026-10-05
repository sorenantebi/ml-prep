---
topic: "Stack"
difficulty: Hard
leetcode: https://leetcode.com/problems/largest-rectangle-in-histogram/
neetcode: https://neetcode.io/problems/largest-rectangle-in-histogram
---
# Largest Rectangle In Histogram - Solution

**Question:** [[Largest Rectangle In Histogram - Question]] · **Difficulty:** Hard

## Intuition

The best rectangle that uses bar `i` as its shortest bar extends left and right until it hits a strictly shorter bar. A monotonic increasing stack finds both boundaries: when a shorter bar arrives, each taller bar popped from the stack has its right boundary at the current index and its left boundary at the new stack top.

## Approach

1. Keep a stack of `(start_index, height)` with increasing heights.
2. For each index `i` with height `h`: set `start = i`. While the top height is `> h`, pop `(j, hj)`, update the answer with `hj * (i - j)`, and set `start = j` (the current bar can extend back to `j`).
3. Push `(start, h)`.
4. After the loop, every remaining `(j, hj)` extends to the end: area `hj * (n - j)`.

## Code

```python
from typing import List


class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		best = 0
		stack = []  # (start index, height), heights increasing
		for i, h in enumerate(heights):
			start = i
			while stack and stack[-1][1] > h:
				j, hj = stack.pop()
				best = max(best, hj * (i - j))  # bar hj spans [j, i)
				start = j                       # h can extend back to j
			stack.append((start, h))
		n = len(heights)
		for j, hj in stack:                     # these extend to the end
			best = max(best, hj * (n - j))
		return best
```

## Complexity

- **Time:** `O(n)` — each bar is pushed and popped at most once.
- **Space:** `O(n)` — the stack.

## Other Approaches

- **Brute force:** for every bar expand left/right while neighbours are at least as tall — Time `O(n^2)`, Space `O(1)`.
- **Divide and conquer:** the best rectangle either spans the minimum bar or lies entirely on one side of it — Time `O(n log n)` average (`O(n^2)` worst), Space `O(n)` recursion.

## Key Takeaway

For "largest area bounded by the minimum" problems, a monotonic increasing stack gives each bar's left and right smaller boundaries in one pass; remember to flush the stack at the end.
