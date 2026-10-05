---
topic: "Linked List"
difficulty: Medium
leetcode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
neetcode: https://neetcode.io/problems/remove-node-from-end-of-linked-list
---
# Remove Nth Node From End of List

**Topic:** [[06 Linked List|Linked List]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) · [NeetCode](https://neetcode.io/problems/remove-node-from-end-of-linked-list)

**Solve it in:** [[Remove Nth Node From End of List]] · **Answer:** [[Remove Nth Node From End of List - Solution]]

## Problem

Given the `head` of a singly linked list and an integer `n`, delete the `n`-th node counting from the end of the list (`n = 1` is the last node) and return the head of the resulting list. `n` is always valid. If the list had a single node, the result is empty.

## Examples

**Example 1**
```text
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

**Example 2**
```text
Input: head = [1], n = 1
Output: []
```

**Example 3**
```text
Input: head = [1,2], n = 1
Output: [1]
```

## Constraints

- The number of nodes `sz` is in the range `[1, 30]`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`
- Follow-up: do it in a single pass

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
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert to_list(s.removeNthFromEnd(build_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
	assert to_list(s.removeNthFromEnd(build_list([1]), 1)) == []
	assert to_list(s.removeNthFromEnd(build_list([1, 2]), 1)) == [1]
	assert to_list(s.removeNthFromEnd(build_list([1, 2]), 2)) == [2]
	assert to_list(s.removeNthFromEnd(build_list([1, 2, 3, 4, 5]), 5)) == [2, 3, 4, 5]
	assert to_list(s.removeNthFromEnd(build_list([1, 2, 3, 4, 5]), 1)) == [1, 2, 3, 4]
	assert to_list(s.removeNthFromEnd(build_list([7, 7, 7]), 2)) == [7, 7]
	print("All tests passed!")
```
