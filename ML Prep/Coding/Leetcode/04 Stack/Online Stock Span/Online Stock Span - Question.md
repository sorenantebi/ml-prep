---
topic: "Stack"
difficulty: Medium
leetcode: https://leetcode.com/problems/online-stock-span/
neetcode: https://neetcode.io/problems/online-stock-span
---
# Online Stock Span

**Topic:** [[04 Stack|Stack]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/online-stock-span/) · [NeetCode](https://neetcode.io/problems/online-stock-span)

**Solve it in:** [[Online Stock Span]] · **Answer:** [[Online Stock Span - Solution]]

## Problem

Design a class `StockSpanner` that receives a stock's price one day at a time and, for each new price, returns that day's **span**: the number of consecutive days, ending with today and going backwards, on which the price was less than or equal to today's price.

- `StockSpanner()` — initializes the object.
- `next(price)` — records today's `price` and returns its span.

For example, if the last prices were `[7, 2, 1, 2]` and today's price is `2`, the span is `4` (today plus the previous three days at or below `2`); if today's price were `8`, the span would be `5`.

## Examples

**Example 1**
```text
Input:  ["StockSpanner","next","next","next","next","next","next","next"]
        [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
```

**Example 2**
```text
Input:  ["StockSpanner","next","next","next"]
        [[],[10],[10],[10]]
Output: [null,1,2,3]
Explanation: equal prices count toward the span
```

## Constraints

- `1 <= price <= 10^5`
- At most `10^4` calls to `next`

## Starter Code & Test Cases

```python
class StockSpanner:
	def __init__(self):
		pass  # your code here

	def next(self, price: int) -> int:
		pass


if __name__ == "__main__":
	sp = StockSpanner()
	assert [sp.next(p) for p in [100, 80, 60, 70, 60, 75, 85]] == [1, 1, 1, 2, 1, 4, 6]

	sp = StockSpanner()
	assert [sp.next(p) for p in [10, 10, 10]] == [1, 2, 3]

	sp = StockSpanner()
	assert [sp.next(p) for p in [1, 2, 3, 4, 5]] == [1, 2, 3, 4, 5]

	sp = StockSpanner()
	assert [sp.next(p) for p in [5, 4, 3, 2, 1]] == [1, 1, 1, 1, 1]

	sp = StockSpanner()
	assert [sp.next(p) for p in [7, 2, 1, 2, 8]] == [1, 1, 1, 3, 5]

	sp = StockSpanner()
	assert sp.next(42) == 1
	print("All tests passed!")
```
