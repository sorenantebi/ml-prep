---
topic: "Stack"
difficulty: Medium
leetcode: https://leetcode.com/problems/online-stock-span/
neetcode: https://neetcode.io/problems/online-stock-span
---
# Online Stock Span - Solution

**Question:** [[Online Stock Span - Question]] · **Difficulty:** Medium

## Intuition

Once a day is "covered" by a later day with a higher-or-equal price, it can never be the blocking day for any future price, so it can be merged into that later day. A monotonic decreasing stack of `(price, span)` pairs stores only the potential blockers, each carrying the size of the block it absorbed.

## Approach

1. Keep a stack of `(price, span)` with strictly decreasing prices from bottom to top.
2. On `next(price)`: start with `span = 1`.
3. While the top price is `<= price`, pop it and add its span to `span`.
4. Push `(price, span)` and return `span`.

## Code

```python
class StockSpanner:
	def __init__(self):
		self.stack = []  # (price, span), prices strictly decreasing

	def next(self, price: int) -> int:
		span = 1
		# absorb all previous days that are not higher than today
		while self.stack and self.stack[-1][0] <= price:
			span += self.stack.pop()[1]
		self.stack.append((price, span))
		return span
```

## Complexity

- **Time:** amortized `O(1)` per call — each price is pushed and popped at most once overall.
- **Space:** `O(n)` — the stack in the worst case (strictly decreasing prices).

## Other Approaches

- **Brute force:** store all prices and walk backwards from today until a higher price is found — Time `O(n)` per call (`O(n^2)` total), Space `O(n)`.

## Key Takeaway

Monotonic stack with aggregated counts: when popping dominated elements, carry their accumulated "width" forward so you never re-scan them.
