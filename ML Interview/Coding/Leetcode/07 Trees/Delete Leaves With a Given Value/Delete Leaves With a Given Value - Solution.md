---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/delete-leaves-with-a-given-value/
neetcode: https://neetcode.io/problems/delete-leaves-with-a-given-value
---
# Delete Leaves With a Given Value - Solution

**Question:** [[Delete Leaves With a Given Value - Question]] · **Difficulty:** Medium

## Intuition

Whether a node becomes a leaf depends on what happens to its children first — so process the tree **post-order**. After both subtrees have been cleaned, the node is a leaf exactly when both pruned children are null; if it is also equal to `target`, delete it by returning null to its parent.

## Approach

1. If `node` is null, return null.
2. `node.left = removeLeafNodes(node.left, target)`; same for `node.right`.
3. If `node` now has no children and `node.val == target`, return null.
4. Otherwise return `node`.

## Code

```python
from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        # clean children first so newly-exposed leaves are handled
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root
```

## Complexity

- **Time:** `O(n)` — every node is visited once.
- **Space:** `O(h)` — recursion stack.

## Other Approaches

- **Repeated passes:** delete matching leaves, repeat until nothing changes — Time `O(n^2)` worst case (a chain of targets), Space `O(h)`.
- **Iterative post-order with parent pointers:** same logic using an explicit stack — Time `O(n)`, Space `O(n)`.

## Key Takeaway

For "prune and cascade upward" tree edits, use post-order recursion that returns the (possibly null) new subtree root and reassigns `node.left/right = recurse(...)`.
