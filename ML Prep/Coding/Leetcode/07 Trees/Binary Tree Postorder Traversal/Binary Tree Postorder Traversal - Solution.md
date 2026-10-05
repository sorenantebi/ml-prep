---
topic: "Trees"
difficulty: Easy
leetcode: https://leetcode.com/problems/binary-tree-postorder-traversal/
neetcode: https://neetcode.io/problems/binary-tree-postorder-traversal
---
# Binary Tree Postorder Traversal - Solution

**Question:** [[Binary Tree Postorder Traversal - Question]] · **Difficulty:** Easy

## Intuition

Postorder is "left, right, node". Its reverse is "node, right, left" — which is just a preorder traversal with the children swapped. So run that easy stack-based traversal and reverse the result at the end.

## Approach

1. If the tree is empty, return `[]`; push `root` onto a stack.
2. Pop a node, append its value.
3. Push `node.left` then `node.right` (so right is processed first).
4. When the stack is empty, reverse the collected list.

## Code

```python
from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		if not root:
			return []
		res, stack = [], [root]
		while stack:
			node = stack.pop()
			res.append(node.val)        # builds node -> right -> left
			if node.left:
				stack.append(node.left)
			if node.right:
				stack.append(node.right)
		return res[::-1]                # reverse gives left -> right -> node
```

## Complexity

- **Time:** `O(n)` — each node is pushed/popped once, plus an `O(n)` reversal.
- **Space:** `O(n)` — the result buffer is reversed at the end; the stack itself is `O(h)`-ish.

## Other Approaches

- **Recursive DFS:** `dfs(left); dfs(right); append(val)` — Time `O(n)`, Space `O(h)`.
- **Single stack with a `visited` flag / last-visited pointer:** emit a node only once its right child has been processed — Time `O(n)`, Space `O(h)`, no reversal.

## Key Takeaway

Iterative postorder = reversed "root, right, left" preorder; alternatively push `(node, visited)` pairs to handle any traversal order uniformly.
