---
topic: "Trees"
difficulty: Hard
leetcode: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
neetcode: https://neetcode.io/problems/serialize-and-deserialize-binary-tree
---
# Serialize And Deserialize Binary Tree - Solution

**Question:** [[Serialize And Deserialize Binary Tree - Question]] · **Difficulty:** Hard

## Intuition

A traversal alone is ambiguous, but a traversal that also records **null children** pins down the structure exactly. Level-order (BFS) with `"N"` markers is easy to encode and decode iteratively — each non-null node consumes the next two tokens as its left and right children — and it avoids recursion-depth problems on very deep trees.

## Approach

1. **Serialize:** BFS from the root; append each node's value (or `"N"` for null) and enqueue both children of every non-null node. Join tokens with commas.
2. **Deserialize:** split on commas; if the first token is `"N"`, return null.
3. Create the root from token 0 and put it in a queue; keep an index `i = 1`.
4. For each dequeued node, read token `i` as its left child and `i+1` as its right child (skipping `"N"`), enqueue any created children, and advance `i` by 2.
5. Return the root.

## Code

```python
from collections import deque
from typing import Optional

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        out, q = [], deque([root])
        while q:
            node = q.popleft()
            if node:
                out.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                out.append("N")             # explicit null marker keeps structure
        return ",".join(out)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        tokens = data.split(",")
        if tokens[0] == "N":
            return None
        root = TreeNode(int(tokens[0]))
        q, i = deque([root]), 1
        while q:
            node = q.popleft()
            if tokens[i] != "N":            # next two tokens are this node's children
                node.left = TreeNode(int(tokens[i]))
                q.append(node.left)
            if tokens[i + 1] != "N":
                node.right = TreeNode(int(tokens[i + 1]))
                q.append(node.right)
            i += 2
        return root
```

## Complexity

- **Time:** `O(n)` — each node (and each null child) is emitted and parsed once.
- **Space:** `O(n)` — the output string/token list and the BFS queue.

## Other Approaches

- **Preorder DFS with null markers:** serialize `val, left, right` recursively; deserialize by consuming tokens with an iterator in the same order — Time `O(n)`, Space `O(n)` (recursion depth `O(h)`, so deep trees need a higher recursion limit).
- **Preorder + inorder arrays:** only works with unique values and needs two traversals — Time `O(n)`, Space `O(n)`.

## Key Takeaway

Include null markers and any traversal becomes a lossless encoding; decode by replaying the same traversal order. BFS-based codecs stay iterative and are safe for deep trees.
