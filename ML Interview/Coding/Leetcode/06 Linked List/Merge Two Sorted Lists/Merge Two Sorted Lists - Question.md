---
topic: "Linked List"
difficulty: Easy
leetcode: https://leetcode.com/problems/merge-two-sorted-lists/
neetcode: https://neetcode.io/problems/merge-two-sorted-linked-lists
---
# Merge Two Sorted Lists

**Topic:** [[06 Linked List|Linked List]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/) · [NeetCode](https://neetcode.io/problems/merge-two-sorted-linked-lists)

**Solve it in:** [[Merge Two Sorted Lists]] · **Answer:** [[Merge Two Sorted Lists - Solution]]

## Problem

You are given the heads of two singly linked lists, `list1` and `list2`, each already sorted in non-decreasing order. Combine them into one sorted linked list by re-linking (splicing) the existing nodes, and return the head of the merged list. Either input may be empty.

## Examples

**Example 1**
```text
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2**
```text
Input: list1 = [], list2 = []
Output: []
```

**Example 3**
```text
Input: list1 = [], list2 = [0]
Output: [0]
```

## Constraints

- The number of nodes in each list is in the range `[0, 50]`
- `-100 <= Node.val <= 100`
- Both lists are sorted in non-decreasing order

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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.mergeTwoLists(build_list([1, 2, 4]), build_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(s.mergeTwoLists(build_list([]), build_list([]))) == []
    assert to_list(s.mergeTwoLists(build_list([]), build_list([0]))) == [0]
    assert to_list(s.mergeTwoLists(build_list([5]), build_list([]))) == [5]
    assert to_list(s.mergeTwoLists(build_list([1, 2, 3]), build_list([4, 5, 6]))) == [1, 2, 3, 4, 5, 6]
    assert to_list(s.mergeTwoLists(build_list([-3, 0, 0]), build_list([-5, 0, 7]))) == [-5, -3, 0, 0, 0, 7]
    assert to_list(s.mergeTwoLists(build_list([2, 2]), build_list([2]))) == [2, 2, 2]
    print("All tests passed!")
```
