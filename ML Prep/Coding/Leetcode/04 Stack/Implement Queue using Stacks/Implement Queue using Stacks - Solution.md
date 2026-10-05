---
topic: "Stack"
difficulty: Easy
leetcode: https://leetcode.com/problems/implement-queue-using-stacks/
neetcode: https://neetcode.io/problems/implement-queue-using-stacks
---
# Implement Queue using Stacks - Solution

**Question:** [[Implement Queue using Stacks - Question]] · **Difficulty:** Easy

## Intuition

Pouring one stack into another reverses its order, turning newest-on-top into oldest-on-top. Use an `inbox` stack for pushes and an `outbox` stack for pops; only refill the outbox when it is empty, so each element is moved at most once.

## Approach

1. `push(x)`: push onto `inbox`.
2. Helper `_shift()`: if `outbox` is empty, pop everything from `inbox` onto `outbox` (reversing order).
3. `pop()` / `peek()`: call `_shift()`, then pop / read the top of `outbox`.
4. `empty()`: both stacks are empty.

## Code

```python
class MyQueue:
	def __init__(self):
		self.inbox = []   # receives new elements
		self.outbox = []  # holds elements in FIFO order (front on top)

	def push(self, x: int) -> None:
		self.inbox.append(x)

	def _shift(self) -> None:
		# only refill when outbox is empty, otherwise order would break
		if not self.outbox:
			while self.inbox:
				self.outbox.append(self.inbox.pop())

	def pop(self) -> int:
		self._shift()
		return self.outbox.pop()

	def peek(self) -> int:
		self._shift()
		return self.outbox[-1]

	def empty(self) -> bool:
		return not self.inbox and not self.outbox
```

## Complexity

- **Time:** amortized `O(1)` per operation — each element is pushed and popped at most twice in total (worst-case single `pop` is `O(n)`).
- **Space:** `O(n)` — elements are split across the two stacks.

## Other Approaches

- **Transfer on every push:** move everything to a helper stack, push the new element, move everything back so the main stack's top is always the front — push `O(n)`, pop/peek `O(1)`, Space `O(n)`.

## Key Takeaway

Two stacks make a queue with amortized O(1) operations: lazily transfer from input to output stack only when the output stack is empty.
