---
topic: "Linked List"
difficulty: Medium
leetcode: https://leetcode.com/problems/add-two-numbers/
neetcode: https://neetcode.io/problems/add-two-numbers
---
# Add Two Numbers

**Topic:** [[06 Linked List|Linked List]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/add-two-numbers/) · [NeetCode](https://neetcode.io/problems/add-two-numbers)

**Solve it in:** [[Add Two Numbers]] · **Answer:** [[Add Two Numbers - Solution]]

## Problem

Two non-negative integers are stored as non-empty linked lists, one digit per node, with the digits in **reverse order** (the head holds the ones digit). Add the two numbers and return their sum as a linked list in the same reversed-digit format. Apart from the number 0 itself, the inputs have no leading zeros.

## Examples

**Example 1**
```text
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
```

**Example 2**
```text
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3**
```text
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

## Constraints

- The number of nodes in each list is in the range `[1, 100]`
- `0 <= Node.val <= 9`
- No leading zeros except for the number 0

## Starter Code & Test Cases

```python
from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


def build_list(values):
	dummy = ListNode()
	cur = dummy
	for v in values:
		cur.next = ListNode(v)
		cur = cur.next
	return dummy.next


def to_list(head):
	out = []
	while head:
		out.append(head.val)
		head = head.next
	return out


class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()

	def add(a, b):
		return to_list(s.addTwoNumbers(build_list(a), build_list(b)))

	assert add([2, 4, 3], [5, 6, 4]) == [7, 0, 8]
	assert add([0], [0]) == [0]
	assert add([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]) == [8, 9, 9, 9, 0, 0, 0, 1]
	assert add([5], [5]) == [0, 1]
	assert add([1], [9, 9]) == [0, 0, 1]
	assert add([0], [7, 3]) == [7, 3]
	big_a, big_b = [9] * 100, [1]
	assert add(big_a, big_b) == [0] * 100 + [1]
	print("All tests passed!")
```
