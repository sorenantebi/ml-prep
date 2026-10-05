---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/insert-into-a-binary-search-tree/
neetcode: https://neetcode.io/problems/insert-into-a-binary-search-tree
---
# Insert into a Binary Search Tree

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/insert-into-a-binary-search-tree/) · [NeetCode](https://neetcode.io/problems/insert-into-a-binary-search-tree)

**Solve it in:** [[Insert into a Binary Search Tree]] · **Answer:** [[Insert into a Binary Search Tree - Solution]]

## Problem

You are given the `root` of a binary search tree and a `val` that does **not** already exist in the tree. Insert `val` so the tree remains a valid BST and return the (possibly new) root. Several valid resulting trees may exist — any of them is accepted.

## Examples

**Example 1**
```text
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
```

**Example 2**
```text
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
```

**Example 3**
```text
Input: root = [], val = 5
Output: [5]
```

## Constraints

- The number of nodes is in the range `[0, 10^4]`
- `-10^8 <= Node.val, val <= 10^8`
- All values are unique and `val` is not in the tree

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


def inorder(root: Optional[TreeNode]) -> List[int]:
	"""Inorder values (test helper). Strictly increasing <=> valid BST."""
	return inorder(root.left) + [root.val] + inorder(root.right) if root else []


class Solution:
	def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()

	def check(values, val):
		res = s.insertIntoBST(build_tree(values), val)
		# any valid BST containing the old values + val is accepted
		assert inorder(res) == sorted([v for v in values if v is not None] + [val])
		return res

	assert tree_to_list(check([4, 2, 7, 1, 3], 5)) == [4, 2, 7, 1, 3, 5]  # leaf-insertion answer
	check([40, 20, 60, 10, 30, 50, 70], 25)
	assert tree_to_list(check([], 5)) == [5]
	check([1], 0)
	check([1], 2)
	check([5, 3, 8, 1, 4, 7, 9], 6)
	check([10, 5, None, 2], 3)
	print("All tests passed!")
```
