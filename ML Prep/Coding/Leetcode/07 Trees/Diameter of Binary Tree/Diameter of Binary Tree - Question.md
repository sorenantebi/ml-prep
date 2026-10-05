---
topic: "Trees"
difficulty: Easy
leetcode: https://leetcode.com/problems/diameter-of-binary-tree/
neetcode: https://neetcode.io/problems/binary-tree-diameter
---
# Diameter of Binary Tree

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/) · [NeetCode](https://neetcode.io/problems/binary-tree-diameter)

**Solve it in:** [[Diameter of Binary Tree]] · **Answer:** [[Diameter of Binary Tree - Solution]]

## Problem

Given the `root` of a binary tree, return the length of its **diameter**: the longest path (measured in **edges**) between any two nodes. The path does not have to pass through the root.

## Examples

**Example 1**
```text
Input: root = [1,2,3,4,5]
Output: 3
Explanation: path 4 -> 2 -> 1 -> 3 (or 5 -> 2 -> 1 -> 3) has 3 edges.
```

**Example 2**
```text
Input: root = [1,2]
Output: 1
```

## Constraints

- The number of nodes is in the range `[1, 10^4]`
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
	def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.diameterOfBinaryTree(build_tree([1, 2, 3, 4, 5])) == 3
	assert s.diameterOfBinaryTree(build_tree([1, 2])) == 1
	assert s.diameterOfBinaryTree(build_tree([1])) == 0
	# longest path 7-5-3-2-4-6-8 lies entirely in the left subtree
	assert s.diameterOfBinaryTree(build_tree([1, 2, None, 3, 4, 5, None, None, 6, 7, None, None, 8])) == 6
	assert s.diameterOfBinaryTree(build_tree([1, 2, 3, 4, 5, 6, 7])) == 4
	assert s.diameterOfBinaryTree(build_tree([1, None, 2, None, 3, None, 4])) == 3  # chain
	print("All tests passed!")
```
