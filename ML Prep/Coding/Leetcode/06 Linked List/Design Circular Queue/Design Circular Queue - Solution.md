---
topic: "Linked List"
difficulty: Medium
leetcode: https://leetcode.com/problems/design-circular-queue/
neetcode: https://neetcode.io/problems/design-circular-queue
---
# Design Circular Queue - Solution

**Question:** [[Design Circular Queue - Question]] · **Difficulty:** Medium

## Intuition

A fixed-size array plus a `head` index and a `size` counter is enough: the rear position is computed as `(head + size - 1) % k`, and the next free slot as `(head + size) % k`. Modular arithmetic wraps indices around, and tracking `size` explicitly avoids the classic "is head == tail empty or full?" ambiguity.

## Approach

1. Store `buf = [0] * k`, `head = 0`, `size = 0`, capacity `k`.
2. `enQueue`: if full return `False`; else write to `buf[(head + size) % k]` and increment `size`.
3. `deQueue`: if empty return `False`; else `head = (head + 1) % k`, decrement `size`.
4. `Front` returns `buf[head]`, `Rear` returns `buf[(head + size - 1) % k]` (or `-1` when empty).
5. `isEmpty` is `size == 0`; `isFull` is `size == k`.

## Code

```python
class MyCircularQueue:
	def __init__(self, k: int):
		self.buf = [0] * k
		self.cap = k
		self.head = 0      # index of the front element
		self.size = 0      # number of stored elements

	def enQueue(self, value: int) -> bool:
		if self.isFull():
			return False
		self.buf[(self.head + self.size) % self.cap] = value
		self.size += 1
		return True

	def deQueue(self) -> bool:
		if self.isEmpty():
			return False
		self.head = (self.head + 1) % self.cap
		self.size -= 1
		return True

	def Front(self) -> int:
		return -1 if self.isEmpty() else self.buf[self.head]

	def Rear(self) -> int:
		return -1 if self.isEmpty() else self.buf[(self.head + self.size - 1) % self.cap]

	def isEmpty(self) -> bool:
		return self.size == 0

	def isFull(self) -> bool:
		return self.size == self.cap
```

## Complexity

- **Time:** `O(1)` per operation — only index arithmetic.
- **Space:** `O(k)` — the fixed buffer.

## Other Approaches

- **Doubly / singly linked list with a size counter:** append at the tail, remove from the head, reject when `size == k` — Time `O(1)` per op, Space `O(k)` (but extra node overhead).

## Key Takeaway

Ring buffers = array + head index + size, with `% capacity` for wrap-around. Keeping an explicit size (or leaving one slot empty) disambiguates empty vs. full.
