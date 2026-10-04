---
topic: "Linked List"
difficulty: Medium
leetcode: https://leetcode.com/problems/reorder-list/
neetcode: https://neetcode.io/problems/reorder-linked-list
---
# Reorder List

**Topic:** [[06 Linked List|Linked List]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/reorder-list/) · [NeetCode](https://neetcode.io/problems/reorder-linked-list)

**Solve it in:** [[Reorder List]] · **Answer:** [[Reorder List - Solution]]

## Problem

You are given the `head` of a singly linked list whose nodes are, in order, `L0 → L1 → … → Ln-1 → Ln`. Rearrange the nodes in place so the order becomes `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …` (alternately taking from the front and the back). You must re-link the nodes themselves, not just change their values. The function returns nothing.

## Examples

**Example 1**
```text
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

**Example 2**
```text
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

## Constraints

- The number of nodes is in the range `[1, 5 * 10^4]`
- `1 <= Node.val <= 1000`

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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Do not return anything, modify head in-place instead."""
        pass  # your code here


if __name__ == "__main__":
    s = Solution()

    def run(vals):
        head = build_list(vals)
        s.reorderList(head)
        return to_list(head)

    assert run([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert run([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert run([1]) == [1]
    assert run([1, 2]) == [1, 2]
    assert run([1, 2, 3]) == [1, 3, 2]
    assert run([5, 5, 6, 6]) == [5, 6, 5, 6]
    n = 1000
    expected = []
    for i in range(n // 2):
        expected += [i + 1, n - i]
    assert run(list(range(1, n + 1))) == expected
    print("All tests passed!")
```
