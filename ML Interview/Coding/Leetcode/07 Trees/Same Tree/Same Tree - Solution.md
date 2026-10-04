---
topic: "Trees"
difficulty: Easy
leetcode: https://leetcode.com/problems/same-tree/
neetcode: https://neetcode.io/problems/same-binary-tree
---
# Same Tree - Solution

**Question:** [[Same Tree - Question]] · **Difficulty:** Easy

## Intuition

Two trees are equal iff their roots match and their left subtrees are equal and their right subtrees are equal. A simultaneous DFS over both trees checks that, bailing out at the first mismatch in shape or value.

## Approach

1. If both nodes are null, return `true`.
2. If exactly one is null, or their values differ, return `false`.
3. Return `isSameTree(p.left, q.left) and isSameTree(p.right, q.right)`.

## Code

```python
from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:   # shape or value mismatch
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

## Complexity

- **Time:** `O(min(n, m))` — stops at the first mismatch; at most visits every node of the smaller tree.
- **Space:** `O(min(h1, h2))` — recursion stack.

## Other Approaches

- **Iterative BFS on pairs:** push `(p, q)` pairs into a queue and compare each pair — Time `O(n)`, Space `O(w)`.
- **Serialize and compare:** serialize both with explicit null markers and compare strings — Time `O(n + m)`, Space `O(n + m)`.

## Key Takeaway

The "walk two trees in lockstep" recursion is a building block for Subtree of Another Tree, Symmetric Tree, and Merge Two Binary Trees.
