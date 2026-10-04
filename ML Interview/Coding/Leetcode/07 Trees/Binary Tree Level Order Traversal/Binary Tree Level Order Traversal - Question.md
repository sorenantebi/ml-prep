---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/binary-tree-level-order-traversal/
neetcode: https://neetcode.io/problems/level-order-traversal-of-binary-tree
---
# Binary Tree Level Order Traversal

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/) · [NeetCode](https://neetcode.io/problems/level-order-traversal-of-binary-tree)

**Solve it in:** [[Binary Tree Level Order Traversal]] · **Answer:** [[Binary Tree Level Order Traversal - Solution]]

## Problem

Given the `root` of a binary tree, return its node values grouped **level by level**, from top to bottom, with each level listed from left to right. Return a list of lists (one inner list per level); an empty tree gives `[]`.

## Examples

**Example 1**
```text
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

**Example 2**
```text
Input: root = [1]
Output: [[1]]
```

**Example 3**
```text
Input: root = []
Output: []
```

## Constraints

- The number of nodes is in the range `[0, 2000]`
- `-1000 <= Node.val <= 1000`

## Starter Code & Test Cases

```python
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from a LeetCode-style level-order list (None = missing child)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Serialize a tree to a LeetCode-style level-order list (trailing Nones trimmed)."""
    if not root:
        return []
    out, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.levelOrder(build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
    assert s.levelOrder(build_tree([1])) == [[1]]
    assert s.levelOrder(build_tree([])) == []
    assert s.levelOrder(build_tree([1, 2, 3, 4, None, None, 5])) == [[1], [2, 3], [4, 5]]
    assert s.levelOrder(build_tree([1, 2, None, 3, None, 4])) == [[1], [2], [3], [4]]
    assert s.levelOrder(build_tree([1, 2, 3, 4, 5, 6, 7])) == [[1], [2, 3], [4, 5, 6, 7]]
    print("All tests passed!")
```
