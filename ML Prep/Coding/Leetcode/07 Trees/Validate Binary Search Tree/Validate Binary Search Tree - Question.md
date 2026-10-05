---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/validate-binary-search-tree/
neetcode: https://neetcode.io/problems/valid-binary-search-tree
---
# Validate Binary Search Tree

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/validate-binary-search-tree/) · [NeetCode](https://neetcode.io/problems/valid-binary-search-tree)

**Solve it in:** [[Validate Binary Search Tree]] · **Answer:** [[Validate Binary Search Tree - Solution]]

## Problem

Given the `root` of a binary tree, decide whether it is a valid **binary search tree**:

- every value in a node's left subtree is **strictly less** than the node's value,
- every value in a node's right subtree is **strictly greater** than the node's value,
- and both subtrees are themselves valid BSTs.

Return `true` or `false`. Duplicates make the tree invalid.

## Examples

**Example 1**
```text
Input: root = [2,1,3]
Output: true
```

**Example 2**
```text
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: the right child 4 is smaller than the root 5.
```

**Example 3**
```text
Input: root = [5,4,6,null,null,3,7]
Output: false
Explanation: 3 sits in 5's right subtree, even though it is a valid left child of 6.
```

## Constraints

- The number of nodes is in the range `[1, 10^4]`
- `-2^31 <= Node.val <= 2^31 - 1`

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
	def isValidBST(self, root: Optional[TreeNode]) -> bool:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.isValidBST(build_tree([2, 1, 3])) is True
	assert s.isValidBST(build_tree([5, 1, 4, None, None, 3, 6])) is False
	assert s.isValidBST(build_tree([5, 4, 6, None, None, 3, 7])) is False
	assert s.isValidBST(build_tree([2, 2, 2])) is False                  # duplicates
	assert s.isValidBST(build_tree([1])) is True
	assert s.isValidBST(build_tree([-2147483648, None, 2147483647])) is True  # extreme values
	assert s.isValidBST(build_tree([1, None, 1])) is False
	assert s.isValidBST(build_tree([8, 4, 12, 2, 6, 10, 14])) is True
	print("All tests passed!")
```
