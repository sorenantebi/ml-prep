---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/delete-node-in-a-bst/
neetcode: https://neetcode.io/problems/delete-node-in-a-bst
---
# Delete Node in a BST - Solution

**Question:** [[Delete Node in a BST - Question]] · **Difficulty:** Medium

## Intuition

First locate the node using BST search. Deleting it has three cases: a leaf simply disappears; a node with one child is replaced by that child; a node with two children takes the value of its **inorder successor** (the minimum of its right subtree), and then that successor — which has no left child — is deleted from the right subtree.

## Approach

1. If `root` is null, return null.
2. If `key < root.val`, set `root.left = deleteNode(root.left, key)`; if `key > root.val`, recurse right the same way.
3. Otherwise `root` is the target:
   - If it has no left child, return `root.right`; if no right child, return `root.left`.
   - Else find the minimum node in `root.right`, copy its value into `root`, and delete that value from `root.right`.
4. Return `root`.

## Code

```python
from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
		if not root:
			return None
		if key < root.val:
			root.left = self.deleteNode(root.left, key)
		elif key > root.val:
			root.right = self.deleteNode(root.right, key)
		else:
			if not root.left:           # 0 or 1 child: splice it out
				return root.right
			if not root.right:
				return root.left
			succ = root.right           # 2 children: inorder successor
			while succ.left:
				succ = succ.left
			root.val = succ.val
			root.right = self.deleteNode(root.right, succ.val)
		return root
```

## Complexity

- **Time:** `O(h)` — one descent to find the key plus one descent to find/delete the successor.
- **Space:** `O(h)` — recursion stack.

## Other Approaches

- **Attach left subtree under successor:** when the node has two children, hang its left subtree off the leftmost node of its right subtree and return the right child — Time `O(h)`, Space `O(h)`, but can increase tree height.
- **Rebuild from inorder:** collect values, drop `key`, rebuild a balanced BST — Time `O(n)`, Space `O(n)`.

## Key Takeaway

BST deletion = search + three cases; the two-child case reduces to deleting the inorder successor (or predecessor), which always has at most one child.
