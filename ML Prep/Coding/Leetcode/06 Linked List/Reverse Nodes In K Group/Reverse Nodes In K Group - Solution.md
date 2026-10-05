---
topic: "Linked List"
difficulty: Hard
leetcode: https://leetcode.com/problems/reverse-nodes-in-k-group/
neetcode: https://neetcode.io/problems/reverse-nodes-in-k-group
---
# Reverse Nodes In K Group - Solution

**Question:** [[Reverse Nodes In K Group - Question]] · **Difficulty:** Hard

## Intuition

Process the list group by group. Before reversing, check that `k` nodes actually remain (find the `k`-th node from the current group's predecessor); if not, stop. Reverse the group in place and reconnect it between the previous group's tail and the next group's head. A dummy node gives the first group a predecessor.

## Approach

1. `dummy -> head`; `group_prev = dummy`.
2. Find `kth`, the node `k` steps after `group_prev`. If it doesn't exist, break.
3. Let `group_next = kth.next`. Reverse the nodes from `group_prev.next` up to `kth`, initializing `prev = group_next` so the reversed group's tail automatically links to the next group.
4. Reconnect: the old group head (`group_prev.next`) is the new tail; set `group_prev.next = kth` and move `group_prev` to the old head.
5. Return `dummy.next`.

## Code

```python
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		dummy = ListNode(0, head)
		group_prev = dummy
		while True:
			kth = group_prev
			for _ in range(k):          # make sure k nodes remain
				kth = kth.next
				if not kth:
					return dummy.next
			group_next = kth.next

			prev, cur = group_next, group_prev.next   # reversed tail links to next group
			while cur is not group_next:
				nxt = cur.next
				cur.next = prev
				prev, cur = cur, nxt

			old_head = group_prev.next   # becomes the tail of this group
			group_prev.next = kth        # kth is the new head of this group
			group_prev = old_head
```

## Complexity

- **Time:** `O(n)` — each node is visited a constant number of times (once to count, once to reverse).
- **Space:** `O(1)` — in-place pointer manipulation.

## Other Approaches

- **Recursive:** reverse the first `k` nodes and set the original head's `next` to the recursive result on the rest — Time `O(n)`, Space `O(n/k)` recursion stack.
- **Array of nodes / values:** reverse chunks in an array and rebuild — Time `O(n)`, Space `O(n)`.

## Key Takeaway

For segment reversals, track `group_prev` and `group_next`; initializing `prev = group_next` before reversing stitches the segment's tail for free.
