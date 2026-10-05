---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
neetcode: https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal
---
# Construct Binary Tree From Preorder And Inorder Traversal

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) · [NeetCode](https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal)

**Solve it in:** [[Construct Binary Tree From Preorder And Inorder Traversal]] · **Answer:** [[Construct Binary Tree From Preorder And Inorder Traversal - Solution]]

## Problem

You are given two integer arrays, `preorder` and `inorder`, which are the preorder and inorder traversals of the same binary tree. All values are **unique**. Reconstruct the tree and return its root.

## Examples

**Example 1**
```text
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

**Example 2**
```text
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

## Constraints

- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- All values are unique, and both arrays describe the same tree

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
	def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert tree_to_list(s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])) == [3, 9, 20, None, None, 15, 7]
	assert tree_to_list(s.buildTree([-1], [-1])) == [-1]
	assert tree_to_list(s.buildTree([1, 2], [2, 1])) == [1, 2]
	assert tree_to_list(s.buildTree([1, 2], [1, 2])) == [1, None, 2]
	assert tree_to_list(s.buildTree([1, 2, 4, 5, 3, 6], [4, 2, 5, 1, 6, 3])) == [1, 2, 3, 4, 5, 6]
	assert tree_to_list(s.buildTree([1, 2, 3, 4], [4, 3, 2, 1])) == [1, 2, None, 3, None, 4]  # left chain
	n = 3000
	chain = s.buildTree(list(range(n)), list(range(n)))   # right-skewed, 3000 deep
	assert tree_to_list(chain)[:5] == [0, None, 1, None, 2]
	print("All tests passed!")
```
