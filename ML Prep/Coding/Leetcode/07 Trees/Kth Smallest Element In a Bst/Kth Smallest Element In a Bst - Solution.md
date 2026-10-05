---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
neetcode: https://neetcode.io/problems/kth-smallest-integer-in-bst
---
# Kth Smallest Element In a Bst - Solution

**Question:** [[Kth Smallest Element In a Bst - Question]] · **Difficulty:** Medium

## Intuition

An inorder traversal of a BST visits values in ascending order, so the k-th node popped during inorder is the answer. Using the iterative version lets us stop immediately after `k` nodes instead of traversing the whole tree.

## Approach

1. Run iterative inorder: push nodes while going left.
2. Pop a node — it is the next smallest value; decrement `k`.
3. If `k` hits `0`, return that node's value.
4. Otherwise move to the popped node's right child and continue.

## Code

```python
from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
		stack, cur = [], root
		while cur or stack:
			while cur:
				stack.append(cur)
				cur = cur.left
			cur = stack.pop()       # next value in sorted order
			k -= 1
			if k == 0:
				return cur.val
			cur = cur.right
		return -1                   # unreachable for valid k
```

## Complexity

- **Time:** `O(h + k)` — descend to the minimum, then pop `k` nodes.
- **Space:** `O(h)` — the stack holds one root-to-leaf path.

## Other Approaches

- **Full inorder into a list:** collect all values, return `vals[k-1]` — Time `O(n)`, Space `O(n)`.
- **Subtree-size augmentation (follow-up):** store each node's subtree size so each query walks down in `O(h)`, updated on insert/delete — Time `O(h)` per query.

## Key Takeaway

"Sorted order in a BST" means inorder traversal; the iterative form lets you stop early after the k-th element.
