---
topic: "Trees"
difficulty: Easy
leetcode: https://leetcode.com/problems/balanced-binary-tree/
neetcode: https://neetcode.io/problems/balanced-binary-tree
---
# Balanced Binary Tree - Solution

**Question:** [[Balanced Binary Tree - Question]] · **Difficulty:** Easy

## Intuition

Checking balance top-down recomputes heights repeatedly. Instead, compute heights bottom-up and use a sentinel (`-1`) to signal "some subtree below is already unbalanced", so the whole check finishes in one pass.

## Approach

1. Define `height(node)`: return `0` for null.
2. Recursively get the left and right heights; if either is `-1`, propagate `-1`.
3. If `|left - right| > 1`, return `-1`.
4. Otherwise return `1 + max(left, right)`.
5. The tree is balanced iff `height(root) != -1`.

## Code

```python
from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            l = height(node.left)
            if l == -1:
                return -1           # short-circuit: already unbalanced
            r = height(node.right)
            if r == -1 or abs(l - r) > 1:
                return -1
            return 1 + max(l, r)

        return height(root) != -1
```

## Complexity

- **Time:** `O(n)` — each node is visited once.
- **Space:** `O(h)` — recursion stack.

## Other Approaches

- **Top-down:** at each node compare `height(left)` and `height(right)` then recurse into both children — Time `O(n log n)` balanced / `O(n^2)` skewed, Space `O(h)`.

## Key Takeaway

When a check depends on subtree heights, compute them post-order and fold the validity flag into the return value (sentinel or `(ok, height)` tuple) to stay linear.
