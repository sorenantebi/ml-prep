---
topic: "Linked List"
difficulty: Medium
leetcode: https://leetcode.com/problems/reverse-linked-list-ii/
neetcode: https://neetcode.io/problems/reverse-linked-list-ii
---
# Reverse Linked List II

**Topic:** [[06 Linked List|Linked List]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/reverse-linked-list-ii/) · [NeetCode](https://neetcode.io/problems/reverse-linked-list-ii)

**Solve it in:** [[Reverse Linked List II]] · **Answer:** [[Reverse Linked List II - Solution]]

## Problem

Given the `head` of a singly linked list and two 1-indexed positions `left <= right`, reverse only the nodes from position `left` through position `right` (inclusive), leaving the rest of the list in its original order. Return the head of the modified list.

## Examples

**Example 1**
```text
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
```

**Example 2**
```text
Input: head = [5], left = 1, right = 1
Output: [5]
```

## Constraints

- The number of nodes is `n`, with `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`
- Follow-up: do it in one pass

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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()

    def run(vals, l, r):
        return to_list(s.reverseBetween(build_list(vals), l, r))

    assert run([1, 2, 3, 4, 5], 2, 4) == [1, 4, 3, 2, 5]
    assert run([5], 1, 1) == [5]
    assert run([1, 2, 3, 4, 5], 1, 5) == [5, 4, 3, 2, 1]
    assert run([1, 2, 3, 4, 5], 1, 2) == [2, 1, 3, 4, 5]
    assert run([1, 2, 3, 4, 5], 4, 5) == [1, 2, 3, 5, 4]
    assert run([3, 5], 1, 2) == [5, 3]
    assert run([1, 2, 3], 2, 2) == [1, 2, 3]
    print("All tests passed!")
```
