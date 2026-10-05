---
topic: "Stack"
difficulty: Easy
leetcode: https://leetcode.com/problems/implement-stack-using-queues/
neetcode: https://neetcode.io/problems/implement-stack-using-queues
---
# Implement Stack Using Queues - Solution

**Question:** [[Implement Stack Using Queues - Question]] · **Difficulty:** Easy

## Intuition

A queue gives elements back in insertion order, but a stack needs the newest element first. If, right after every push, we rotate the queue so the new element moves to the front, the queue's front is always the stack's top — using just one queue.

## Approach

1. Store elements in a single queue `q`.
2. `push(x)`: append `x` to the back, then move the `len(q) - 1` older elements from the front to the back one by one, so `x` ends up at the front.
3. `pop()`: remove and return the front element.
4. `top()`: return the front element.
5. `empty()`: return whether the queue is empty.

## Code

```python
from collections import deque


class MyStack:
	def __init__(self):
		self.q = deque()

	def push(self, x: int) -> None:
		self.q.append(x)
		# rotate older elements behind x so x is at the front
		for _ in range(len(self.q) - 1):
			self.q.append(self.q.popleft())

	def pop(self) -> int:
		return self.q.popleft()

	def top(self) -> int:
		return self.q[0]

	def empty(self) -> bool:
		return not self.q
```

## Complexity

- **Time:** `O(n)` for `push`, `O(1)` for `pop`, `top`, `empty` — push rotates the whole queue.
- **Space:** `O(n)` — one queue holding all elements.

## Other Approaches

- **Two queues, cheap push:** push to `q1`; on `pop`, move all but the last element to `q2`, take the last, then swap queues — push `O(1)`, pop/top `O(n)`, Space `O(n)`.

## Key Takeaway

You can reverse a queue's order for the newest element by rotating it `size - 1` times after insertion — pay the cost on the write side so reads are O(1).
