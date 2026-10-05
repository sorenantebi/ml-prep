---
topic: "Trees"
difficulty: Hard
leetcode: https://leetcode.com/problems/binary-tree-maximum-path-sum/
neetcode: https://neetcode.io/problems/binary-tree-maximum-path-sum
---
# Binary Tree Maximum Path Sum

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/binary-tree-maximum-path-sum/) · [NeetCode](https://neetcode.io/problems/binary-tree-maximum-path-sum)

**Solve it in:** [[Binary Tree Maximum Path Sum]] · **Answer:** [[Binary Tree Maximum Path Sum - Solution]]

## Problem

A **path** in a binary tree is a sequence of nodes in which every consecutive pair is joined by an edge; each node appears at most once, and the path need not pass through the root. A path must contain **at least one** node. The path sum is the sum of its node values. Given the `root`, return the maximum path sum over all non-empty paths. Node values can be negative.

## Examples

**Example 1**
```text
Input: root = [1,2,3]
Output: 6
Explanation: path 2 -> 1 -> 3.
```

**Example 2**
```text
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: path 15 -> 20 -> 7.
```

**Example 3**
```text
Input: root = [-3]
Output: -3
```

## Constraints

- The number of nodes is in the range `[1, 3 * 10^4]`
- `-1000 <= Node.val <= 1000`

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
	def maxPathSum(self, root: Optional[TreeNode]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.maxPathSum(build_tree([1, 2, 3])) == 6
	assert s.maxPathSum(build_tree([-10, 9, 20, None, None, 15, 7])) == 42
	assert s.maxPathSum(build_tree([-3])) == -3
	assert s.maxPathSum(build_tree([2, -1])) == 2
	assert s.maxPathSum(build_tree([-2, -1])) == -1                 # all negative
	assert s.maxPathSum(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 48
	assert s.maxPathSum(build_tree([1, -2, 3])) == 4
	print("All tests passed!")
```
