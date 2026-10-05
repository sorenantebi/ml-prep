---
topic: "Trees"
difficulty: Easy
leetcode: https://leetcode.com/problems/binary-tree-preorder-traversal/
neetcode: https://neetcode.io/problems/binary-tree-preorder-traversal
---
# Binary Tree Preorder Traversal

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/binary-tree-preorder-traversal/) · [NeetCode](https://neetcode.io/problems/binary-tree-preorder-traversal)

**Solve it in:** [[Binary Tree Preorder Traversal]] · **Answer:** [[Binary Tree Preorder Traversal - Solution]]

## Problem

Given the `root` of a binary tree, return the values of its nodes in **preorder** order: visit the node itself first, then its entire left subtree, then its entire right subtree. An empty tree yields an empty list.

Follow-up: solve it iteratively.

## Examples

**Example 1**
```text
Input: root = [1,null,2,3]
Output: [1,2,3]
```

**Example 2**
```text
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [1,2,4,5,6,7,3,8,9]
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
	def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.preorderTraversal(build_tree([1, None, 2, 3])) == [1, 2, 3]
	assert s.preorderTraversal(build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])) == [1, 2, 4, 5, 6, 7, 3, 8, 9]
	assert s.preorderTraversal(build_tree([])) == []
	assert s.preorderTraversal(build_tree([1])) == [1]
	assert s.preorderTraversal(build_tree([3, 2, None, 1])) == [3, 2, 1]
	assert s.preorderTraversal(build_tree([4, 2, 6, 1, 3, 5, 7])) == [4, 2, 1, 3, 6, 5, 7]
	print("All tests passed!")
```
