---
topic: "Linked List"
difficulty: Medium
leetcode: https://leetcode.com/problems/reverse-linked-list-ii/
neetcode: https://neetcode.io/problems/reverse-linked-list-ii
---
# Reverse Linked List II - Solution

**Question:** [[Reverse Linked List II - Question]] · **Difficulty:** Medium

## Intuition

Locate the node just before position `left` (a dummy head makes this exist even when `left = 1`). Then reverse the next `right - left + 1` nodes with the usual pointer reversal, and finally stitch the reversed segment back between its predecessor and the first node after the segment.

## Approach

1. Create `dummy -> head`; walk `left - 1` steps to get `before` (the node preceding the segment).
2. Reverse `right - left + 1` nodes starting at `before.next` using `prev/cur`. Afterwards `prev` is the new segment head and `cur` is the first node after the segment.
3. The old segment head (`before.next`) is now the segment tail: set its `next` to `cur`, then set `before.next = prev`.
4. Return `dummy.next`.

## Code

```python
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before = dummy
        for _ in range(left - 1):
            before = before.next

        prev, cur = None, before.next
        for _ in range(right - left + 1):   # standard reversal of the segment
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt

        before.next.next = cur   # old segment head is now its tail
        before.next = prev       # connect predecessor to new segment head
        return dummy.next
```

## Complexity

- **Time:** `O(n)` — at most one pass to `right`.
- **Space:** `O(1)` — in-place pointer changes.

## Other Approaches

- **Head insertion:** repeatedly move the node after the segment's original head to the front of the segment (`right - left` times) — Time `O(n)`, Space `O(1)`.
- **Copy values to an array, reverse the slice, write back** — Time `O(n)`, Space `O(n)`.

## Key Takeaway

Reversing a sub-list = reverse with a bounded counter, then reconnect two boundaries: predecessor → new head and old head → successor. A dummy node handles `left = 1`.
