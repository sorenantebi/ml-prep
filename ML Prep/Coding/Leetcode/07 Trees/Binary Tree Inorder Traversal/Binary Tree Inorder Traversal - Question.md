---
topic: "Trees"
difficulty: Easy
leetcode: https://leetcode.com/problems/binary-tree-inorder-traversal/
neetcode: https://neetcode.io/problems/binary-tree-inorder-traversal
---
# Binary Tree Inorder Traversal

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/binary-tree-inorder-traversal/) · [NeetCode](https://neetcode.io/problems/binary-tree-inorder-traversal)

**Solve it in:** [[Binary Tree Inorder Traversal]] · **Answer:** [[Binary Tree Inorder Traversal - Solution]]

## Problem

Given the `root` of a binary tree, return a list of its node values in **inorder** order: for every node, first visit its entire left subtree, then the node itself, then its entire right subtree. An empty tree yields an empty list.

Follow-up: the recursive version is trivial — can you do it iteratively?

## Examples

**Example 1**
```text
Input: root = [1,null,2,3]
Output: [1,3,2]
```

**Example 2**
```text
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]
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
	def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.inorderTraversal(build_tree([1, None, 2, 3])) == [1, 3, 2]
	assert s.inorderTraversal(build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])) == [4, 2, 6, 5, 7, 1, 3, 9, 8]
	assert s.inorderTraversal(build_tree([])) == []
	assert s.inorderTraversal(build_tree([1])) == [1]
	assert s.inorderTraversal(build_tree([3, 2, None, 1])) == [1, 2, 3]  # left-skewed
	assert s.inorderTraversal(build_tree([1, None, 2, None, 3])) == [1, 2, 3]  # right-skewed
	assert s.inorderTraversal(build_tree([4, 2, 6, 1, 3, 5, 7])) == [1, 2, 3, 4, 5, 6, 7]  # BST -> sorted
	print("All tests passed!")
```
