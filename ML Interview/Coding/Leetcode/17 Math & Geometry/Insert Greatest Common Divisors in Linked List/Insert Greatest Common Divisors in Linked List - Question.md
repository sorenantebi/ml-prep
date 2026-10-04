---
topic: "Math & Geometry"
difficulty: Medium
leetcode: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
neetcode: https://neetcode.io/problems/insert-greatest-common-divisors-in-linked-list
---
# Insert Greatest Common Divisors in Linked List

**Topic:** [[17 Math & Geometry|Math & Geometry]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/) · [NeetCode](https://neetcode.io/problems/insert-greatest-common-divisors-in-linked-list)

**Solve it in:** [[Insert Greatest Common Divisors in Linked List]] · **Answer:** [[Insert Greatest Common Divisors in Linked List - Solution]]

## Problem

You are given the `head` of a singly linked list of positive integers.

Between **every pair of adjacent nodes**, insert a new node whose value is the greatest common divisor (GCD) of the two neighbours' values. Return the head of the modified list.

The GCD of two numbers is the largest positive integer that divides both of them evenly.

## Examples

**Example 1**
```text
Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation: gcd(18,6)=6, gcd(6,10)=2, gcd(10,3)=1 are inserted between the pairs.
```

**Example 2**
```text
Input: head = [7]
Output: [7]
Explanation: There are no adjacent pairs, so nothing is inserted.
```

## Constraints

- The number of nodes is in the range `[1, 5000]`.
- `1 <= Node.val <= 1000`

## Starter Code & Test Cases

```python
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.insertGreatestCommonDivisors(build_list([18, 6, 10, 3]))) == [18, 6, 6, 2, 10, 1, 3]
    assert to_list(s.insertGreatestCommonDivisors(build_list([7]))) == [7]
    assert to_list(s.insertGreatestCommonDivisors(build_list([2, 4]))) == [2, 2, 4]
    assert to_list(s.insertGreatestCommonDivisors(build_list([1, 1]))) == [1, 1, 1]
    assert to_list(s.insertGreatestCommonDivisors(build_list([5, 10, 15]))) == [5, 5, 10, 5, 15]
    assert to_list(s.insertGreatestCommonDivisors(build_list([7, 13, 1000]))) == [7, 1, 13, 1, 1000]
    assert to_list(s.insertGreatestCommonDivisors(build_list([12, 18, 24]))) == [12, 6, 18, 6, 24]
    print("All tests passed!")
```
