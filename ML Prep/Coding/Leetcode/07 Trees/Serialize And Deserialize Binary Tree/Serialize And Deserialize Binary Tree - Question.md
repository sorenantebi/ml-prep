---
topic: "Trees"
difficulty: Hard
leetcode: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
neetcode: https://neetcode.io/problems/serialize-and-deserialize-binary-tree
---
# Serialize And Deserialize Binary Tree

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) · [NeetCode](https://neetcode.io/problems/serialize-and-deserialize-binary-tree)

**Solve it in:** [[Serialize And Deserialize Binary Tree]] · **Answer:** [[Serialize And Deserialize Binary Tree - Solution]]

## Problem

Design an algorithm to **serialize** a binary tree into a string and **deserialize** that string back into the original tree structure. Implement the `Codec` class:

- `serialize(root)` — encodes the tree as a single string.
- `deserialize(data)` — decodes a string produced by `serialize` and returns the root of an identical tree.

There are no restrictions on the string format; the only requirement is that `deserialize(serialize(root))` reproduces the same tree (structure and values). Values may be negative and the tree may be empty.

## Examples

**Example 1**
```text
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```

**Example 2**
```text
Input: root = []
Output: []
```

## Constraints

- The number of nodes is in the range `[0, 10^4]`
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


class Codec:
	def serialize(self, root: Optional[TreeNode]) -> str:
		"""Encodes a tree to a single string."""
		pass  # your code here

	def deserialize(self, data: str) -> Optional[TreeNode]:
		"""Decodes your encoded data to tree."""
		pass  # your code here


if __name__ == "__main__":
	def roundtrip(values):
		ser, deser = Codec(), Codec()
		data = ser.serialize(build_tree(values))
		assert isinstance(data, str)
		return tree_to_list(deser.deserialize(data))

	for vals in ([1, 2, 3, None, None, 4, 5],
				 [],
				 [1],
				 [-1, -2, -3],
				 [1, 2, None, 3, None, 4],          # left chain
				 [12, 1000, -1000, None, 7, 0],     # multi-digit & negative values
				 [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]):
		assert roundtrip(vals) == vals, vals

	deep = [0] + [x for k in range(1, 5000) for x in (None, k)]  # 5000-deep right chain
	assert roundtrip(deep) == deep
	print("All tests passed!")
```
