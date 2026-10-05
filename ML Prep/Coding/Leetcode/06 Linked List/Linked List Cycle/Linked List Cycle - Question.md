---
topic: "Linked List"
difficulty: Easy
leetcode: https://leetcode.com/problems/linked-list-cycle/
neetcode: https://neetcode.io/problems/linked-list-cycle-detection
---
# Linked List Cycle

**Topic:** [[06 Linked List|Linked List]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/linked-list-cycle/) · [NeetCode](https://neetcode.io/problems/linked-list-cycle-detection)

**Solve it in:** [[Linked List Cycle]] · **Answer:** [[Linked List Cycle - Solution]]

## Problem

Given the `head` of a singly linked list, decide whether the list contains a cycle — i.e. whether following `next` pointers from some node eventually leads back to that same node. Return `true` if a cycle exists, otherwise `false`. (Internally, LeetCode builds the cycle with an index `pos` that the tail connects to; `pos = -1` means no cycle. `pos` is not passed to your function.)

## Examples

**Example 1**
```text
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: the tail links back to the node at index 1.
```

**Example 2**
```text
Input: head = [1,2], pos = 0
Output: true
```

**Example 3**
```text
Input: head = [1], pos = -1
Output: false
```

## Constraints

- The number of nodes is in the range `[0, 10^4]`
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the list
- Follow-up: solve it with `O(1)` extra memory

## Starter Code & Test Cases

```python
from typing import Optional


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def build_cycle_list(values, pos):
	"""Build a list from values; connect the tail to index pos (-1 = no cycle)."""
	nodes = [ListNode(v) for v in values]
	for a, b in zip(nodes, nodes[1:]):
		a.next = b
	if nodes and pos != -1:
		nodes[-1].next = nodes[pos]
	return nodes[0] if nodes else None


class Solution:
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.hasCycle(build_cycle_list([3, 2, 0, -4], 1)) is True
	assert s.hasCycle(build_cycle_list([1, 2], 0)) is True
	assert s.hasCycle(build_cycle_list([1], -1)) is False
	assert s.hasCycle(build_cycle_list([], -1)) is False
	assert s.hasCycle(build_cycle_list([1], 0)) is True
	assert s.hasCycle(build_cycle_list([1, 2, 3, 4, 5], -1)) is False
	assert s.hasCycle(build_cycle_list(list(range(10000)), 9999)) is True
	print("All tests passed!")
```
