---
topic: "Stack"
difficulty: Easy
leetcode: https://leetcode.com/problems/implement-queue-using-stacks/
neetcode: https://neetcode.io/problems/implement-queue-using-stacks
---
# Implement Queue using Stacks

**Topic:** [[04 Stack|Stack]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/) · [NeetCode](https://neetcode.io/problems/implement-queue-using-stacks)

**Solve it in:** [[Implement Queue using Stacks]] · **Answer:** [[Implement Queue using Stacks - Solution]]

## Problem

Build a first-in-first-out (FIFO) queue using only two stacks. Implement the class `MyQueue` with:

- `MyQueue()` — creates an empty queue.
- `push(x)` — adds element `x` to the back of the queue.
- `pop()` — removes the element at the front of the queue and returns it.
- `peek()` — returns the front element without removing it.
- `empty()` — returns `true` if the queue is empty, `false` otherwise.

Only standard stack operations are allowed: push to top, peek/pop from top, size, and is-empty (a Python list used strictly as a stack is fine). `pop` and `peek` are only called on a non-empty queue.

**Follow-up:** make every operation amortized `O(1)`.

## Examples

**Example 1**
```text
Input:  ["MyQueue","push","push","peek","pop","empty"]
        [[],[1],[2],[],[],[]]
Output: [null,null,null,1,1,false]
```

**Example 2**
```text
Input:  ["MyQueue","push","pop","empty"]
        [[],[7],[],[]]
Output: [null,null,7,true]
```

## Constraints

- `1 <= x <= 9`
- At most `100` calls in total to `push`, `pop`, `peek` and `empty`
- `pop` and `peek` are only called on a non-empty queue

## Starter Code & Test Cases

```python
class MyQueue:
	def __init__(self):
		pass  # your code here

	def push(self, x: int) -> None:
		pass

	def pop(self) -> int:
		pass

	def peek(self) -> int:
		pass

	def empty(self) -> bool:
		pass


if __name__ == "__main__":
	q = MyQueue()
	assert q.empty() is True
	q.push(1)
	q.push(2)
	assert q.peek() == 1
	assert q.pop() == 1
	assert q.empty() is False
	q.push(3)
	assert q.peek() == 2
	assert q.pop() == 2
	assert q.pop() == 3
	assert q.empty() is True

	q2 = MyQueue()
	for v in range(1, 10):
		q2.push(v)
	out = [q2.pop() for _ in range(4)]
	q2.push(5)
	out += [q2.pop() for _ in range(6)]
	assert out == [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
	assert q2.empty() is True
	print("All tests passed!")
```
