---
topic: "Linked List"
difficulty: Medium
leetcode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
neetcode: https://neetcode.io/problems/remove-node-from-end-of-linked-list
---
# Remove Nth Node From End of List - Solution

**Question:** [[Remove Nth Node From End of List - Question]] · **Difficulty:** Medium

## Intuition

To delete a node we need the node *before* it. If a `right` pointer is `n` steps ahead of a `left` pointer, then when `right` reaches the end, `left` is exactly at the node to remove (or just before it). Starting `left` at a dummy node placed before `head` makes it land on the predecessor and also handles removing the head itself.

## Approach

1. Create `dummy` with `dummy.next = head`; set `left = dummy`, `right = head`.
2. Advance `right` by `n` nodes.
3. Move both pointers together until `right` is `None`; now `left.next` is the target.
4. Skip it: `left.next = left.next.next`. Return `dummy.next`.

## Code

```python
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head
        for _ in range(n):          # create a gap of n nodes
            right = right.next
        while right:
            left, right = left.next, right.next
        left.next = left.next.next  # left is the predecessor of the target
        return dummy.next
```

## Complexity

- **Time:** `O(sz)` — a single pass over the list.
- **Space:** `O(1)` — two pointers and a dummy node.

## Other Approaches

- **Two passes:** count the length `L`, then walk `L - n` steps to the predecessor — Time `O(sz)`, Space `O(1)`.

## Key Takeaway

A fixed-size gap between two pointers converts "k-th from the end" into a one-pass problem; a dummy head removes the "delete the head" edge case.
