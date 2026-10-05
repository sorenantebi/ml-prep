---
topic: "Linked List"
difficulty: Hard
leetcode: https://leetcode.com/problems/merge-k-sorted-lists/
neetcode: https://neetcode.io/problems/merge-k-sorted-linked-lists
---
# Merge K Sorted Lists

**Topic:** [[06 Linked List|Linked List]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/) · [NeetCode](https://neetcode.io/problems/merge-k-sorted-linked-lists)

**Solve it in:** [[Merge K Sorted Lists]] · **Answer:** [[Merge K Sorted Lists - Solution]]

## Problem

You are given an array `lists` of `k` linked lists, each sorted in ascending order. Merge them all into a single sorted linked list and return its head. `lists` may be empty, and individual lists may be empty.

## Examples

**Example 1**
```text
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

**Example 2**
```text
Input: lists = []
Output: []
```

**Example 3**
```text
Input: lists = [[]]
Output: []
```

## Constraints

- `k == lists.length`, `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- Each `lists[i]` is sorted in ascending order
- The total number of nodes does not exceed `10^4`

## Starter Code & Test Cases

```python
from typing import List, Optional
import heapq


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
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()

	def run(arrs):
		return to_list(s.mergeKLists([build_list(a) for a in arrs]))

	assert run([[1, 4, 5], [1, 3, 4], [2, 6]]) == [1, 1, 2, 3, 4, 4, 5, 6]
	assert run([]) == []
	assert run([[]]) == []
	assert run([[], [1], []]) == [1]
	assert run([[2, 2, 2], [2, 2]]) == [2, 2, 2, 2, 2]
	assert run([[-10, -5, 0], [-7, 3], [10]]) == [-10, -7, -5, 0, 3, 10]
	import random
	random.seed(4)
	arrs = [sorted(random.randint(-100, 100) for _ in range(random.randint(0, 30))) for _ in range(50)]
	assert run(arrs) == sorted(x for a in arrs for x in a)
	print("All tests passed!")
```
