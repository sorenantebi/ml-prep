---
topic: "Trees"
difficulty: Easy
leetcode: https://leetcode.com/problems/subtree-of-another-tree/
neetcode: https://neetcode.io/problems/subtree-of-a-binary-tree
---
# Subtree of Another Tree

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/subtree-of-another-tree/) · [NeetCode](https://neetcode.io/problems/subtree-of-a-binary-tree)

**Solve it in:** [[Subtree of Another Tree]] · **Answer:** [[Subtree of Another Tree - Solution]]

## Problem

Given the roots of two binary trees `root` and `subRoot`, return `true` if some node of `root` is the root of a subtree that is **identical** to `subRoot` (same structure and values), and `false` otherwise. A subtree of a node consists of that node and **all** of its descendants — so a partial match that leaves out some descendants does not count. The whole tree `root` is also considered a subtree of itself.

## Examples

**Example 1**
```text
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

**Example 2**
```text
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
Explanation: node 4 in root has an extra descendant 0.
```

## Constraints

- The number of nodes in `root` is in the range `[1, 2000]`
- The number of nodes in `subRoot` is in the range `[1, 1000]`
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
	def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.isSubtree(build_tree([3, 4, 5, 1, 2]), build_tree([4, 1, 2])) is True
	assert s.isSubtree(build_tree([3, 4, 5, 1, 2, None, None, None, None, 0]), build_tree([4, 1, 2])) is False
	assert s.isSubtree(build_tree([1, 1]), build_tree([1])) is True
	assert s.isSubtree(build_tree([12]), build_tree([2])) is False          # naive string matching pitfall
	assert s.isSubtree(build_tree([1, 2, 3]), build_tree([1, 2])) is False  # must include all descendants
	assert s.isSubtree(build_tree([1, 2, 3]), build_tree([1, 2, 3])) is True  # whole tree
	assert s.isSubtree(build_tree([3, 4, 5, 1, None, 2]), build_tree([3, 1, 2])) is False
	print("All tests passed!")
```
