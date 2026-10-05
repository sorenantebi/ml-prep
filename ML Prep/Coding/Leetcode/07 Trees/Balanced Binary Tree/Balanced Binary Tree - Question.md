---
topic: "Trees"
difficulty: Easy
leetcode: https://leetcode.com/problems/balanced-binary-tree/
neetcode: https://neetcode.io/problems/balanced-binary-tree
---
# Balanced Binary Tree

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/balanced-binary-tree/) · [NeetCode](https://neetcode.io/problems/balanced-binary-tree)

**Solve it in:** [[Balanced Binary Tree]] · **Answer:** [[Balanced Binary Tree - Solution]]

## Problem

Given a binary tree, decide whether it is **height-balanced**: for **every** node, the heights of its left and right subtrees differ by at most `1`. Return `true` if so, otherwise `false`. An empty tree is balanced.

## Examples

**Example 1**
```text
Input: root = [3,9,20,null,null,15,7]
Output: true
```

**Example 2**
```text
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

**Example 3**
```text
Input: root = []
Output: true
```

## Constraints

- The number of nodes is in the range `[0, 5000]`
- `-10^4 <= Node.val <= 10^4`

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
	def isBalanced(self, root: Optional[TreeNode]) -> bool:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.isBalanced(build_tree([3, 9, 20, None, None, 15, 7])) is True
	assert s.isBalanced(build_tree([1, 2, 2, 3, 3, None, None, 4, 4])) is False
	assert s.isBalanced(build_tree([])) is True
	assert s.isBalanced(build_tree([1])) is True
	assert s.isBalanced(build_tree([1, None, 2])) is True
	assert s.isBalanced(build_tree([1, None, 2, None, 3])) is False
	# root looks balanced (both sides height 3) but its children are not
	assert s.isBalanced(build_tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4])) is False
	print("All tests passed!")
```
