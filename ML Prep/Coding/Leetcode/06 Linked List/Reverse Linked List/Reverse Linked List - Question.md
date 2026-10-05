---
topic: "Linked List"
difficulty: Easy
leetcode: https://leetcode.com/problems/reverse-linked-list/
neetcode: https://neetcode.io/problems/reverse-a-linked-list
---
# Reverse Linked List

**Topic:** [[06 Linked List|Linked List]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/reverse-linked-list/) · [NeetCode](https://neetcode.io/problems/reverse-a-linked-list)

**Solve it in:** [[Reverse Linked List]] · **Answer:** [[Reverse Linked List - Solution]]

## Problem

You are given the `head` of a singly linked list. Reverse the list so that every `next` pointer points to the previous node instead of the following one, and return the head of the reversed list (the original tail). An empty list stays empty.

## Examples

**Example 1**
```text
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2**
```text
Input: head = [1,2]
Output: [2,1]
```

**Example 3**
```text
Input: head = []
Output: []
```

## Constraints

- The number of nodes is in the range `[0, 5000]`
- `-5000 <= Node.val <= 5000`
- Follow-up: can you do it both iteratively and recursively?

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
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert to_list(s.reverseList(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
	assert to_list(s.reverseList(build_list([1, 2]))) == [2, 1]
	assert to_list(s.reverseList(build_list([]))) == []
	assert to_list(s.reverseList(build_list([7]))) == [7]
	assert to_list(s.reverseList(build_list([1, 1, 2, 2]))) == [2, 2, 1, 1]
	assert to_list(s.reverseList(build_list([-5, 0, 5]))) == [5, 0, -5]
	assert to_list(s.reverseList(build_list(list(range(5000))))) == list(range(4999, -1, -1))
	print("All tests passed!")
```
