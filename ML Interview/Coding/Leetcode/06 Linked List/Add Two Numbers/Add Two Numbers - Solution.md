---
topic: "Linked List"
difficulty: Medium
leetcode: https://leetcode.com/problems/add-two-numbers/
neetcode: https://neetcode.io/problems/add-two-numbers
---
# Add Two Numbers - Solution

**Question:** [[Add Two Numbers - Question]] · **Difficulty:** Medium

## Intuition

Since the digits are stored least-significant first, we can simulate grade-school addition directly while walking both lists: add the two digits plus the carry, emit `sum % 10`, carry `sum // 10`. Continue while either list has nodes or a carry remains.

## Approach

1. Create a `dummy` head and `tail`; set `carry = 0`.
2. While `l1`, `l2`, or `carry` is non-zero: take each digit (0 if that list is exhausted), compute `total = d1 + d2 + carry`.
3. Append `ListNode(total % 10)`, set `carry = total // 10`, advance the pointers.
4. Return `dummy.next`.

## Code

```python
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        carry = 0
        while l1 or l2 or carry:        # final carry may create an extra node
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry, digit = divmod(total, 10)
            tail.next = ListNode(digit)
            tail = tail.next
        return dummy.next
```

## Complexity

- **Time:** `O(max(m, n))` — one pass over the longer list.
- **Space:** `O(1)` extra — the output list of length `max(m, n) + 1` is not counted.

## Other Approaches

- **Convert to integers:** read both numbers into Python ints, add, then rebuild the list — Time `O(m + n)`, Space `O(m + n)`; works in Python thanks to big ints but defeats the purpose (overflows in fixed-width languages).

## Key Takeaway

Simulate digit-by-digit arithmetic with a carry and loop condition `while l1 or l2 or carry` — it handles unequal lengths and the trailing carry uniformly.
