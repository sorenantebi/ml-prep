---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
neetcode: https://neetcode.io/problems/count-good-nodes-in-binary-tree
---
# Count Good Nodes In Binary Tree

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) · [NeetCode](https://neetcode.io/problems/count-good-nodes-in-binary-tree)

**Solve it in:** [[Count Good Nodes In Binary Tree]] · **Answer:** [[Count Good Nodes In Binary Tree - Solution]]

## Problem

Given the `root` of a binary tree, a node `X` is called **good** if, on the path from the root down to `X`, no node has a value strictly greater than `X`'s value. Return the number of good nodes in the tree. (The root is always good.)

## Examples

**Example 1**
```text
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: the root 3, the 4, the 5, and the lower-left 3 are good.
```

**Example 2**
```text
Input: root = [3,3,null,4,2]
Output: 3
Explanation: node 2 is not good because 3 lies above it.
```

**Example 3**
```text
Input: root = [1]
Output: 1
```

## Constraints

- The number of nodes is in the range `[1, 10^5]`
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
	def goodNodes(self, root: TreeNode) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.goodNodes(build_tree([3, 1, 4, 3, None, 1, 5])) == 4
	assert s.goodNodes(build_tree([3, 3, None, 4, 2])) == 3
	assert s.goodNodes(build_tree([1])) == 1
	assert s.goodNodes(build_tree([2, None, 4, 10, 8, None, None, 4])) == 4
	assert s.goodNodes(build_tree([-1, -2, -3])) == 1
	assert s.goodNodes(build_tree([5, 4, 6, 3, None, None, 7])) == 3
	assert s.goodNodes(build_tree([1, 2, 3, 4, 5, 6, 7])) == 7   # strictly increasing paths
	print("All tests passed!")
```
