---
topic: "Trees"
difficulty: Easy
leetcode: https://leetcode.com/problems/invert-binary-tree/
neetcode: https://neetcode.io/problems/invert-a-binary-tree
---
# Invert Binary Tree

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/invert-binary-tree/) · [NeetCode](https://neetcode.io/problems/invert-a-binary-tree)

**Solve it in:** [[Invert Binary Tree]] · **Answer:** [[Invert Binary Tree - Solution]]

## Problem

Given the `root` of a binary tree, mirror it: for every node, swap its left and right subtrees. Return the root of the inverted tree. An empty tree stays empty.

## Examples

**Example 1**
```text
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

**Example 2**
```text
Input: root = [2,1,3]
Output: [2,3,1]
```

**Example 3**
```text
Input: root = []
Output: []
```

## Constraints

- The number of nodes is in the range `[0, 100]`
- `-100 <= Node.val <= 100`

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
	def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert tree_to_list(s.invertTree(build_tree([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
	assert tree_to_list(s.invertTree(build_tree([2, 1, 3]))) == [2, 3, 1]
	assert tree_to_list(s.invertTree(build_tree([]))) == []
	assert tree_to_list(s.invertTree(build_tree([1]))) == [1]
	assert tree_to_list(s.invertTree(build_tree([1, 2]))) == [1, None, 2]
	assert tree_to_list(s.invertTree(build_tree([1, 2, None, 3]))) == [1, None, 2, None, 3]
	print("All tests passed!")
```
