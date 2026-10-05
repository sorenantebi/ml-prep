---
topic: "Linked List"
difficulty: Medium
leetcode: https://leetcode.com/problems/design-circular-queue/
neetcode: https://neetcode.io/problems/design-circular-queue
---
# Design Circular Queue

**Topic:** [[06 Linked List|Linked List]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/design-circular-queue/) · [NeetCode](https://neetcode.io/problems/design-circular-queue)

**Solve it in:** [[Design Circular Queue]] · **Answer:** [[Design Circular Queue - Solution]]

## Problem

Design a fixed-capacity circular (ring-buffer) FIFO queue, where the slot after the last position wraps around to the first. Implement the class `MyCircularQueue`:

- `MyCircularQueue(k)` — create a queue that can hold at most `k` elements.
- `enQueue(value)` — add `value` to the rear; return `True` on success, `False` if full.
- `deQueue()` — remove the front element; return `True` on success, `False` if empty.
- `Front()` — return the front element, or `-1` if empty.
- `Rear()` — return the last element, or `-1` if empty.
- `isEmpty()` / `isFull()` — report whether the queue is empty / full.

Do not use a built-in queue type.

## Examples

**Example 1**
```text
Input:  ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]
        [[3],[1],[2],[3],[4],[],[],[],[4],[]]
Output: [null,true,true,true,false,3,true,true,true,4]
```

**Example 2**
```text
Input:  ["MyCircularQueue","Front","Rear","isEmpty","enQueue","Front"]
        [[1],[],[],[],[9],[]]
Output: [null,-1,-1,true,true,9]
```

## Constraints

- `1 <= k <= 1000`
- `0 <= value <= 1000`
- At most `3000` calls in total

## Starter Code & Test Cases

```python
class MyCircularQueue:
	def __init__(self, k: int):
		pass  # your code here

	def enQueue(self, value: int) -> bool:
		pass

	def deQueue(self) -> bool:
		pass

	def Front(self) -> int:
		pass

	def Rear(self) -> int:
		pass

	def isEmpty(self) -> bool:
		pass

	def isFull(self) -> bool:
		pass


if __name__ == "__main__":
	def run(ops, args):
		obj = None
		out = []
		for op, a in zip(ops, args):
			if op == "MyCircularQueue":
				obj = MyCircularQueue(*a)
				out.append(None)
			else:
				out.append(getattr(obj, op)(*a))
		return out

	assert run(
		["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"],
		[[3], [1], [2], [3], [4], [], [], [], [4], []],
	) == [None, True, True, True, False, 3, True, True, True, 4]

	assert run(
		["MyCircularQueue", "Front", "Rear", "isEmpty", "enQueue", "Front"],
		[[1], [], [], [], [9], []],
	) == [None, -1, -1, True, True, 9]

	# deQueue on empty, wrap-around behaviour
	q = MyCircularQueue(2)
	assert q.deQueue() is False
	assert q.enQueue(1) and q.enQueue(2)
	assert q.isFull() and not q.enQueue(3)
	assert q.deQueue() and q.Front() == 2
	assert q.enQueue(3) and q.Rear() == 3 and q.Front() == 2
	assert q.deQueue() and q.deQueue() and q.isEmpty()
	assert q.Front() == -1 and q.Rear() == -1

	# many wrap-arounds with capacity 1
	q = MyCircularQueue(1)
	for v in range(100):
		assert q.enQueue(v) and q.Rear() == v and q.Front() == v
		assert not q.enQueue(v + 1)
		assert q.deQueue() and q.isEmpty()
	print("All tests passed!")
```
