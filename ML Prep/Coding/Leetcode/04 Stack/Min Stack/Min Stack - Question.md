---
topic: "Stack"
difficulty: Medium
leetcode: https://leetcode.com/problems/min-stack/
neetcode: https://neetcode.io/problems/minimum-stack
---
# Min Stack

**Topic:** [[04 Stack|Stack]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/min-stack/) · [NeetCode](https://neetcode.io/problems/minimum-stack)

**Solve it in:** [[Min Stack]] · **Answer:** [[Min Stack - Solution]]

## Problem

Design a stack that, in addition to the usual operations, can report its smallest element in constant time. Implement the class `MinStack`:

- `MinStack()` — initializes an empty stack.
- `push(val)` — pushes `val` onto the stack.
- `pop()` — removes the top element.
- `top()` — returns the top element.
- `getMin()` — returns the minimum element currently in the stack.

Every method must run in `O(1)` time. `pop`, `top` and `getMin` are only called when the stack is non-empty.

## Examples

**Example 1**
```text
Input:  ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]
Output: [null,null,null,null,-3,null,0,-2]
```

**Example 2**
```text
Input:  ["MinStack","push","push","getMin","pop","getMin"]
        [[],[1],[1],[],[],[]]
Output: [null,null,null,1,null,1]
Explanation: duplicate minimums must survive a pop
```

## Constraints

- `-2^31 <= val <= 2^31 - 1`
- `pop`, `top`, `getMin` are always called on a non-empty stack
- At most `3 * 10^4` calls in total

## Starter Code & Test Cases

```python
class MinStack:
	def __init__(self):
		pass  # your code here

	def push(self, val: int) -> None:
		pass

	def pop(self) -> None:
		pass

	def top(self) -> int:
		pass

	def getMin(self) -> int:
		pass


if __name__ == "__main__":
	ms = MinStack()
	ms.push(-2)
	ms.push(0)
	ms.push(-3)
	assert ms.getMin() == -3
	ms.pop()
	assert ms.top() == 0
	assert ms.getMin() == -2

	ms2 = MinStack()
	ms2.push(1)
	ms2.push(1)
	assert ms2.getMin() == 1
	ms2.pop()
	assert ms2.getMin() == 1

	ms3 = MinStack()
	for v in [5, 3, 7, 3, 2, 8]:
		ms3.push(v)
	mins = []
	for _ in range(6):
		mins.append(ms3.getMin())
		ms3.pop()
	assert mins == [2, 2, 3, 3, 3, 5]

	ms4 = MinStack()
	ms4.push(2**31 - 1)
	ms4.push(-2**31)
	assert ms4.getMin() == -2**31
	assert ms4.top() == -2**31
	ms4.pop()
	assert ms4.getMin() == 2**31 - 1
	print("All tests passed!")
```
