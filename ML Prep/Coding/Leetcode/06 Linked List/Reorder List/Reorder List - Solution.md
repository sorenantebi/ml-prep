---
topic: "Linked List"
difficulty: Medium
leetcode: https://leetcode.com/problems/reorder-list/
neetcode: https://neetcode.io/problems/reorder-linked-list
---
# Reorder List - Solution

**Question:** [[Reorder List - Question]] · **Difficulty:** Medium

## Intuition

The target order interleaves the first half with the *reversed* second half. So the problem decomposes into three classic linked-list primitives: find the middle (fast/slow pointers), reverse the second half, and merge two lists alternately.

## Approach

1. Find the middle with `slow`/`fast` pointers (`fast` starts at `head.next` so `slow` ends at the end of the first half).
2. Cut the list after `slow` and reverse the second half.
3. Merge alternately: take one node from the first half, then one from the reversed second half, until the second half is exhausted (the first half is equal or one longer).

## Code

```python
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def reorderList(self, head: Optional[ListNode]) -> None:
		# 1. find end of first half
		slow, fast = head, head.next
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		# 2. split and reverse the second half
		second = slow.next
		slow.next = None
		prev = None
		while second:
			nxt = second.next
			second.next = prev
			prev, second = second, nxt
		second = prev

		# 3. weave the two halves together
		first = head
		while second:
			n1, n2 = first.next, second.next
			first.next = second
			second.next = n1
			first, second = n1, n2
```

## Complexity

- **Time:** `O(n)` — three linear passes (middle, reverse, merge).
- **Space:** `O(1)` — all re-linking is done in place.

## Other Approaches

- **Array of nodes + two pointers:** store nodes in a list, then link `i` and `j` from both ends inward — Time `O(n)`, Space `O(n)`.
- **Stack / deque:** push nodes onto a deque and pop alternately from both ends — Time `O(n)`, Space `O(n)`.

## Key Takeaway

Many "hard-looking" list problems are compositions of three primitives: find middle, reverse, merge. Recognize the decomposition and reuse the standard snippets.
