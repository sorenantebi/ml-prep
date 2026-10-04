---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/validate-binary-search-tree/
neetcode: https://neetcode.io/problems/valid-binary-search-tree
---
# Validate Binary Search Tree - Solution

**Question:** [[Validate Binary Search Tree - Question]] · **Difficulty:** Medium

## Intuition

Comparing a node only with its direct children is not enough — every node must respect **all** its ancestors. Track an open interval `(low, high)` of allowed values: going left tightens the upper bound to the parent's value, going right tightens the lower bound.

## Approach

1. Start with `(root, -inf, +inf)` on a stack.
2. Pop `(node, low, high)`; if `node` is null, continue.
3. If not `low < node.val < high`, return `false`.
4. Push `(node.left, low, node.val)` and `(node.right, node.val, high)`.
5. If the stack empties without a violation, return `true`.

## Code

```python
from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, low, high = stack.pop()
            if not node:
                continue
            if not (low < node.val < high):      # must respect every ancestor
                return False
            stack.append((node.left, low, node.val))
            stack.append((node.right, node.val, high))
        return True
```

## Complexity

- **Time:** `O(n)` — each node is checked once.
- **Space:** `O(h)` — the stack holds pending nodes along the current path plus siblings (`O(n)` worst case).

## Other Approaches

- **Inorder traversal:** a BST's inorder sequence is strictly increasing; compare each value with the previous one — Time `O(n)`, Space `O(h)`.
- **Recursive bounds DFS:** `valid(node, low, high)` — same logic, Time `O(n)`, Space `O(h)` recursion.

## Key Takeaway

BST validity is a global constraint — propagate `(min, max)` bounds down the tree (or check that inorder is strictly increasing) instead of only comparing parent and child.
