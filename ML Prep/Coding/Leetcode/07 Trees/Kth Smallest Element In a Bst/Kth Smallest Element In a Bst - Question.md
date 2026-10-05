---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
neetcode: https://neetcode.io/problems/kth-smallest-integer-in-bst
---
# Kth Smallest Element In a Bst

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) · [NeetCode](https://neetcode.io/problems/kth-smallest-integer-in-bst)

**Solve it in:** [[Kth Smallest Element In a Bst]] · **Answer:** [[Kth Smallest Element In a Bst - Solution]]

## Problem

Given the `root` of a binary search tree and an integer `k`, return the `k`-th smallest value among all nodes (1-indexed).

Follow-up: if the BST is modified often (inserts/deletes) and you need the k-th smallest frequently, how would you optimize?

## Examples

**Example 1**
```text
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

**Example 2**
```text
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

## Constraints

- The number of nodes is `n`, with `1 <= k <= n <= 10^4`
- `0 <= Node.val <= 10^4`

## Starter Code & Test Cases

```python
from typing import List, Optional
from collections import deque


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
	"""Build a tree from a LeetCode-style level-order list (None = missing child)."""
	if not values or values[0] is None:
		return None
	root = TreeNode(values[0])
	queue = deque([root])
	i = 1
	while queue and i < len(values):
		node = queue.popleft()
		if i < len(values) and values[i] is not None:
			node.left = TreeNode(values[i])
			queue.append(node.left)
		i += 1
		if i < len(values) and values[i] is not None:
			node.right = TreeNode(values[i])
			queue.append(node.right)
		i += 1
	return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
	"""Serialize a tree to a LeetCode-style level-order list (trailing Nones trimmed)."""
	if not root:
		return []
	out, queue = [], deque([root])
	while queue:
		node = queue.popleft()
		if node:
			out.append(node.val)
			queue.append(node.left)
			queue.append(node.right)
		else:
			out.append(None)
	while out and out[-1] is None:
		out.pop()
	return out


class Solution:
	def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.kthSmallest(build_tree([3, 1, 4, None, 2]), 1) == 1
	assert s.kthSmallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3) == 3
	assert s.kthSmallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 6) == 6  # k = n
	assert s.kthSmallest(build_tree([1]), 1) == 1
	assert s.kthSmallest(build_tree([2, 1, 3]), 3) == 3
	assert s.kthSmallest(build_tree([3, 1, 4, None, 2]), 2) == 2
	print("All tests passed!")
```
