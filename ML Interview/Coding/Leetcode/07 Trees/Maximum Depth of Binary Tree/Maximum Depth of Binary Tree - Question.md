---
topic: "Trees"
difficulty: Easy
leetcode: https://leetcode.com/problems/maximum-depth-of-binary-tree/
neetcode: https://neetcode.io/problems/depth-of-binary-tree
---
# Maximum Depth of Binary Tree

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/) · [NeetCode](https://neetcode.io/problems/depth-of-binary-tree)

**Solve it in:** [[Maximum Depth of Binary Tree]] · **Answer:** [[Maximum Depth of Binary Tree - Solution]]

## Problem

Given the `root` of a binary tree, return its **maximum depth**: the number of nodes on the longest path from the root down to any leaf. An empty tree has depth `0`.

## Examples

**Example 1**
```text
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2**
```text
Input: root = [1,null,2]
Output: 2
```

**Example 3**
```text
Input: root = []
Output: 0
```

## Constraints

- The number of nodes is in the range `[0, 10^4]`
- `-100 <= Node.val <= 100`

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.maxDepth(build_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert s.maxDepth(build_tree([1, None, 2])) == 2
    assert s.maxDepth(build_tree([])) == 0
    assert s.maxDepth(build_tree([1])) == 1
    assert s.maxDepth(build_tree([1, 2, None, 3, None, 4])) == 4  # left-skewed chain
    assert s.maxDepth(build_tree([1, 2, 3, 4, 5, 6, 7])) == 3     # perfect tree
    deep = build_tree([0] + [i for k in range(1, 3000) for i in (k, None)])  # 3000-node chain
    assert s.maxDepth(deep) == 3000
    print("All tests passed!")
```
