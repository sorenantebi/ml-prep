---
topic: "Linked List"
difficulty: Hard
leetcode: https://leetcode.com/problems/reverse-nodes-in-k-group/
neetcode: https://neetcode.io/problems/reverse-nodes-in-k-group
---
# Reverse Nodes In K Group

**Topic:** [[06 Linked List|Linked List]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/) · [NeetCode](https://neetcode.io/problems/reverse-nodes-in-k-group)

**Solve it in:** [[Reverse Nodes In K Group]] · **Answer:** [[Reverse Nodes In K Group - Solution]]

## Problem

Given the `head` of a linked list and a positive integer `k`, reverse the nodes of the list in consecutive groups of `k` and return the new head. If the number of remaining nodes at the end is less than `k`, leave that final partial group in its original order. You must relink the nodes, not just change their values.

## Examples

**Example 1**
```text
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

**Example 2**
```text
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

## Constraints

- The number of nodes is `n`, with `1 <= k <= n <= 5000`
- `0 <= Node.val <= 1000`
- Follow-up: solve it with `O(1)` extra memory

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
	def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()

	def run(vals, k):
		return to_list(s.reverseKGroup(build_list(vals), k))

	assert run([1, 2, 3, 4, 5], 2) == [2, 1, 4, 3, 5]
	assert run([1, 2, 3, 4, 5], 3) == [3, 2, 1, 4, 5]
	assert run([1, 2, 3, 4, 5], 1) == [1, 2, 3, 4, 5]
	assert run([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1]
	assert run([1, 2, 3, 4, 5, 6], 3) == [3, 2, 1, 6, 5, 4]
	assert run([7], 1) == [7]
	vals = list(range(10))
	expected = [3, 2, 1, 0, 7, 6, 5, 4, 8, 9]
	assert run(vals, 4) == expected
	print("All tests passed!")
```
