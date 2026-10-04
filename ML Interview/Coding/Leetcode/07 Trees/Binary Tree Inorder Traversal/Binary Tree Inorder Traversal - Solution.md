---
topic: "Trees"
difficulty: Easy
leetcode: https://leetcode.com/problems/binary-tree-inorder-traversal/
neetcode: https://neetcode.io/problems/binary-tree-inorder-traversal
---
# Binary Tree Inorder Traversal - Solution

**Question:** [[Binary Tree Inorder Traversal - Question]] · **Difficulty:** Easy

## Intuition

Inorder is "left, node, right". Recursion does this naturally, but an explicit stack simulates the call stack: keep walking left and pushing nodes; when you can't go left any more, the top of the stack is the next node to emit, after which you move into its right subtree.

## Approach

1. Start with `cur = root` and an empty stack.
2. While `cur` is not null, push it and go to `cur.left`.
3. Pop a node, append its value to the result.
4. Set `cur = node.right` and repeat until both `cur` is null and the stack is empty.

## Code

```python
from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        cur = root
        while cur or stack:
            while cur:              # dive as far left as possible
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()       # leftmost unvisited node
            res.append(cur.val)
            cur = cur.right         # then handle its right subtree
        return res
```

## Complexity

- **Time:** `O(n)` — each node is pushed and popped exactly once.
- **Space:** `O(h)` — the stack holds at most one root-to-leaf path (`O(n)` worst case for a skewed tree); output list not counted.

## Other Approaches

- **Recursive DFS:** `dfs(left); append(val); dfs(right)` — Time `O(n)`, Space `O(h)` recursion stack.
- **Morris traversal:** temporarily thread each inorder predecessor's right pointer back to the current node to avoid a stack — Time `O(n)`, Space `O(1)`.

## Key Takeaway

The iterative inorder template ("push all lefts, pop, go right") is reused in many BST problems (kth smallest, BST iterator, validate BST) — memorize it.
