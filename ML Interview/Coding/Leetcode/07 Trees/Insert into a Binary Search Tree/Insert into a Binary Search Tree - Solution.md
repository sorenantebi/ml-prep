---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/insert-into-a-binary-search-tree/
neetcode: https://neetcode.io/problems/insert-into-a-binary-search-tree
---
# Insert into a Binary Search Tree - Solution

**Question:** [[Insert into a Binary Search Tree - Question]] · **Difficulty:** Medium

## Intuition

In a BST there is always a valid spot for a new value as a **leaf**: walk down from the root, going left when `val` is smaller and right when larger, until you fall off the tree. Attach the new node there — no restructuring needed.

## Approach

1. If `root` is null, return a new node with `val`.
2. Walk from `cur = root`: if `val < cur.val`, go left, else go right.
3. When the chosen child is null, create the new node there and stop.
4. Return the original `root`.

## Code

```python
from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur = root
        while True:
            if val < cur.val:
                if not cur.left:
                    cur.left = TreeNode(val)    # empty slot found
                    return root
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
```

## Complexity

- **Time:** `O(h)` — one comparison per level (`O(log n)` balanced, `O(n)` skewed).
- **Space:** `O(1)` — iterative.

## Other Approaches

- **Recursive:** `if val < root.val: root.left = insertIntoBST(root.left, val)` (similarly right), returning `root` — Time `O(h)`, Space `O(h)` recursion stack.

## Key Takeaway

BST insertion = BST search that ends at a null child; the "return the subtree root and reassign" recursive style is the same template used for BST deletion.
