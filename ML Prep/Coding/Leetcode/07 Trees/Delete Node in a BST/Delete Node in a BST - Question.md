---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/delete-node-in-a-bst/
neetcode: https://neetcode.io/problems/delete-node-in-a-bst
---
# Delete Node in a BST

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/delete-node-in-a-bst/) · [NeetCode](https://neetcode.io/problems/delete-node-in-a-bst)

**Solve it in:** [[Delete Node in a BST]] · **Answer:** [[Delete Node in a BST - Solution]]

## Problem

Given the `root` of a binary search tree and a `key`, remove the node whose value equals `key` (if such a node exists) while keeping the tree a valid BST, and return the possibly updated root. If `key` is not present, return the tree unchanged. Any valid resulting BST is accepted.

## Examples

**Example 1**
```text
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: [5,2,6,null,4,null,7] is also accepted.
```

**Example 2**
```text
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
```

**Example 3**
```text
Input: root = [], key = 0
Output: []
```

## Constraints

- The number of nodes is in the range `[0, 10^4]`
- `-10^5 <= Node.val, key <= 10^5`
- All node values are unique; `root` is a valid BST

Follow-up: can you do it in `O(height)` time?

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
	def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()

	def check(values, key):
		res = s.deleteNode(build_tree(values), key)
		# any valid BST holding exactly the remaining values is accepted
		assert inorder(res) == sorted(v for v in values if v is not None and v != key)
		return res

	check([5, 3, 6, 2, 4, None, 7], 3)   # node with two children
	assert tree_to_list(check([5, 3, 6, 2, 4, None, 7], 0)) == [5, 3, 6, 2, 4, None, 7]  # key absent
	assert check([], 0) is None
	check([5, 3, 6, 2, 4, None, 7], 5)   # delete the root
	check([5, 3, 6, 2, 4, None, 7], 7)   # delete a leaf
	check([5, 3, 6, 2, 4, None, 7], 6)   # node with one child
	assert check([1], 1) is None
	assert tree_to_list(check([2, 1], 2)) == [1]
	print("All tests passed!")
```
