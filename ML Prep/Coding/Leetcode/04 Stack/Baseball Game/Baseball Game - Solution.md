---
topic: "Stack"
difficulty: Easy
leetcode: https://leetcode.com/problems/baseball-game/
neetcode: https://neetcode.io/problems/baseball-game
---
# Baseball Game - Solution

**Question:** [[Baseball Game - Question]] · **Difficulty:** Easy

## Intuition

The operations only ever look at or remove the most recent scores, which is exactly last-in-first-out behaviour. A stack holding the valid scores lets every operation run in constant time.

## Approach

1. Keep a list `stack` of currently valid scores.
2. For each operation: `"+"` pushes `stack[-1] + stack[-2]`, `"D"` pushes `2 * stack[-1]`, `"C"` pops, otherwise push `int(op)`.
3. Return `sum(stack)`.

## Code

```python
from typing import List


class Solution:
	def calPoints(self, operations: List[str]) -> int:
		stack = []
		for op in operations:
			if op == "+":
				stack.append(stack[-1] + stack[-2])
			elif op == "D":
				stack.append(2 * stack[-1])
			elif op == "C":
				stack.pop()
			else:
				stack.append(int(op))  # handles negative numbers too
		return sum(stack)
```

## Complexity

- **Time:** `O(n)` — each operation is O(1), plus one final sum.
- **Space:** `O(n)` — the stack can hold up to one score per operation.

## Other Approaches

- **Running total:** maintain the sum incrementally (add on push, subtract on pop) to avoid the final pass — same `O(n)` time and `O(n)` space, just a constant-factor tweak.

## Key Takeaway

Whenever operations refer to "the previous" item(s) and can undo the last item, reach for a stack.
