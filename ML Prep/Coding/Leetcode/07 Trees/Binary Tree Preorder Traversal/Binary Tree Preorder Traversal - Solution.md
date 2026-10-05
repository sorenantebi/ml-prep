---
topic: "Trees"
difficulty: Easy
leetcode: https://leetcode.com/problems/binary-tree-preorder-traversal/
neetcode: https://neetcode.io/problems/binary-tree-preorder-traversal
---
# Binary Tree Preorder Traversal - Solution

**Question:** [[Binary Tree Preorder Traversal - Question]] · **Difficulty:** Easy

## Intuition

Preorder emits a node as soon as it is reached, so an explicit stack works directly: pop a node, record it, then push its children. Because a stack is LIFO, push the **right** child before the left so the left subtree is processed first.

## Approach

1. If the tree is empty, return `[]`; otherwise push `root` onto a stack.
2. Pop a node and append its value.
3. Push `node.right` (if any), then `node.left` (if any).
4. Repeat until the stack is empty.

## Code

```python
from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		if not root:
			return []
		res, stack = [], [root]
		while stack:
			node = stack.pop()
			res.append(node.val)
			if node.right:          # right first so left is popped first
				stack.append(node.right)
			if node.left:
				stack.append(node.left)
		return res
```

## Complexity

- **Time:** `O(n)` — every node is pushed and popped once.
- **Space:** `O(h)` — the stack holds roughly one pending right child per level (`O(n)` worst case); output not counted.

## Other Approaches

- **Recursive DFS:** `append(val); dfs(left); dfs(right)` — Time `O(n)`, Space `O(h)`.
- **Morris preorder:** thread predecessors to avoid the stack — Time `O(n)`, Space `O(1)`.

## Key Takeaway

For iterative preorder, push children in reverse of the order you want to visit them (right, then left) — the same trick generalizes to N-ary trees.
