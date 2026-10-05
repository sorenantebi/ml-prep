---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
neetcode: https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal
---
# Construct Binary Tree From Preorder And Inorder Traversal - Solution

**Question:** [[Construct Binary Tree From Preorder And Inorder Traversal - Question]] · **Difficulty:** Medium

## Intuition

The first preorder value is always the root. Its position in `inorder` splits the inorder array into the left subtree (everything before) and right subtree (everything after). Because preorder lists the whole left subtree before the right one, we can consume preorder left to right with a single pointer while recursing on inorder index ranges; a hashmap gives `O(1)` root lookups.

## Approach

1. Build `pos[value] = index in inorder`.
2. Keep a pointer `pre_i` into `preorder` (starts at 0).
3. `build(lo, hi)` constructs the subtree whose inorder range is `[lo, hi]`:
   - if `lo > hi`, return null;
   - root value = `preorder[pre_i]`, advance `pre_i`;
   - `mid = pos[root value]`; build left from `[lo, mid-1]`, then right from `[mid+1, hi]` (left first, matching preorder).
4. Return `build(0, n-1)`.

## Code

```python
import sys
from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
		sys.setrecursionlimit(max(1000, 2 * len(preorder) + 100))  # skewed trees recurse n deep
		pos = {v: i for i, v in enumerate(inorder)}
		pre_i = 0

		def build(lo, hi):
			nonlocal pre_i
			if lo > hi:
				return None
			root = TreeNode(preorder[pre_i])
			pre_i += 1
			mid = pos[root.val]            # splits inorder into left | root | right
			root.left = build(lo, mid - 1)  # must be built before the right subtree
			root.right = build(mid + 1, hi)
			return root

		return build(0, len(inorder) - 1)
```

## Complexity

- **Time:** `O(n)` — each node is created once with `O(1)` index lookup.
- **Space:** `O(n)` — the hashmap, plus `O(h)` recursion stack.

## Other Approaches

- **Slicing recursion:** `root = preorder[0]`, `mid = inorder.index(root)`, recurse on list slices — Time `O(n^2)`, Space `O(n^2)` from copies; simple but slow.
- **Iterative stack:** push preorder nodes, popping while the stack top matches the current inorder value to know when to attach a right child — Time `O(n)`, Space `O(n)`.

## Key Takeaway

Preorder (or postorder) identifies the root; inorder tells you how many nodes go left vs. right. A value-to-index hashmap plus a moving preorder pointer makes the reconstruction linear.
