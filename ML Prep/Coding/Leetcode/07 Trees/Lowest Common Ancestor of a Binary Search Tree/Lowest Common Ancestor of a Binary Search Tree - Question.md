---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
neetcode: https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree
---
# Lowest Common Ancestor of a Binary Search Tree

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) · [NeetCode](https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree)

**Solve it in:** [[Lowest Common Ancestor of a Binary Search Tree]] · **Answer:** [[Lowest Common Ancestor of a Binary Search Tree - Solution]]

## Problem

You are given the `root` of a **binary search tree** and two nodes `p` and `q` that are guaranteed to exist in it. Return their **lowest common ancestor (LCA)**: the deepest node that has both `p` and `q` as descendants, where a node counts as a descendant of itself (so if `p` is an ancestor of `q`, the answer is `p`). All values in the BST are unique and `p != q`.

## Examples

**Example 1**
```text
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
```

**Example 2**
```text
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: a node may be its own ancestor.
```

**Example 3**
```text
Input: root = [2,1], p = 2, q = 1
Output: 2
```

## Constraints

- The number of nodes is in the range `[2, 10^5]`
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are unique; `p != q`; both exist in the BST

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


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
	"""Return the node holding `val` in a BST (test helper)."""
	while root and root.val != val:
		root = root.left if val < root.val else root.right
	return root


class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	t = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
	lca = lambda a, b: s.lowestCommonAncestor(t, find_node(t, a), find_node(t, b)).val
	assert lca(2, 8) == 6
	assert lca(2, 4) == 2
	assert lca(3, 5) == 4
	assert lca(0, 5) == 2
	assert lca(7, 9) == 8
	assert lca(3, 9) == 6
	t2 = build_tree([2, 1])
	assert s.lowestCommonAncestor(t2, find_node(t2, 2), find_node(t2, 1)).val == 2
	print("All tests passed!")
```
