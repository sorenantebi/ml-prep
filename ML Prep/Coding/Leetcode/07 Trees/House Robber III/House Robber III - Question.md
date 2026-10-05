---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/house-robber-iii/
neetcode: https://neetcode.io/problems/house-robber-iii
---
# House Robber III

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/house-robber-iii/) · [NeetCode](https://neetcode.io/problems/house-robber-iii)

**Solve it in:** [[House Robber III]] · **Answer:** [[House Robber III - Solution]]

## Problem

The houses in a neighborhood form a binary tree whose single entrance is the `root`; each node's value is the amount of money in that house. A thief may rob any set of houses **except** that two houses directly connected by an edge (parent and child) cannot both be robbed on the same night. Given the `root`, return the maximum total amount the thief can steal.

## Examples

**Example 1**
```text
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: rob 3 + 3 + 1 (the root and the two grandchildren).
```

**Example 2**
```text
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: rob 4 + 5 (the two children of the root).
```

## Constraints

- The number of nodes is in the range `[1, 10^4]`
- `0 <= Node.val <= 10^4`

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
	def rob(self, root: Optional[TreeNode]) -> int:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.rob(build_tree([3, 2, 3, None, 3, None, 1])) == 7
	assert s.rob(build_tree([3, 4, 5, 1, 3, None, 1])) == 9
	assert s.rob(build_tree([1])) == 1
	assert s.rob(build_tree([4, 1, None, 2, None, 3])) == 7   # chain 4-1-2-3: rob 4 and 3
	assert s.rob(build_tree([2, 1, 3, None, 4])) == 7         # 3 and 4 are not adjacent
	assert s.rob(build_tree([0, 0, 0])) == 0
	assert s.rob(build_tree([10, 1, 1, 5, 5, 5, 5])) == 30    # skip the middle level
	print("All tests passed!")
```
