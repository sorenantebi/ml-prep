---
topic: "Linked List"
difficulty: Medium
leetcode: https://leetcode.com/problems/copy-list-with-random-pointer/
neetcode: https://neetcode.io/problems/copy-linked-list-with-random-pointer
---
# Copy List With Random Pointer

**Topic:** [[06 Linked List|Linked List]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/copy-list-with-random-pointer/) · [NeetCode](https://neetcode.io/problems/copy-linked-list-with-random-pointer)

**Solve it in:** [[Copy List With Random Pointer]] · **Answer:** [[Copy List With Random Pointer - Solution]]

## Problem

A linked list of length `n` is given where every node has a `val`, a `next` pointer, and an extra `random` pointer that may point to any node in the list or be `null`. Build a **deep copy** of the list: `n` brand-new nodes such that for every original node, its copy has the same value, and the copy's `next` and `random` pointers point to the copies of the corresponding original targets. No pointer in the copy may reference an original node. Return the head of the copy.

(LeetCode serializes each node as `[val, random_index]`, where `random_index` is the index of the node `random` points to, or `null`.)

## Examples

**Example 1**
```text
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

**Example 2**
```text
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

**Example 3**
```text
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

## Constraints

- `0 <= n <= 1000`
- `-10^4 <= Node.val <= 10^4`
- `Node.random` is `null` or points to a node in the list

## Starter Code & Test Cases

```python
from typing import Optional


class Node:
	def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
		self.val = int(x)
		self.next = next
		self.random = random


def build_random_list(pairs):
	nodes = [Node(v) for v, _ in pairs]
	for i, (_, r) in enumerate(pairs):
		if i + 1 < len(nodes):
			nodes[i].next = nodes[i + 1]
		if r is not None:
			nodes[i].random = nodes[r]
	return nodes[0] if nodes else None


def serialize(head):
	nodes = []
	cur = head
	while cur:
		nodes.append(cur)
		cur = cur.next
	index = {id(node): i for i, node in enumerate(nodes)}
	return [[node.val, index[id(node.random)] if node.random else None] for node in nodes]


def collect_ids(head):
	ids = set()
	while head:
		ids.add(id(head))
		head = head.next
	return ids


class Solution:
	def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	cases = [
		[[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
		[[1, 1], [2, 1]],
		[[3, None], [3, 0], [3, None]],
		[],
		[[5, 0]],
		[[1, None], [2, None], [3, None]],
		[[i, (i * 7) % 50] for i in range(50)],
	]
	for pairs in cases:
		original = build_random_list(pairs)
		copy = s.copyRandomList(original)
		assert serialize(copy) == pairs
		assert serialize(original) == pairs                     # original untouched
		assert not (collect_ids(copy) & collect_ids(original))  # truly deep copy
	print("All tests passed!")
```
