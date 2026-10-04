---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/binary-tree-right-side-view/
neetcode: https://neetcode.io/problems/binary-tree-right-side-view
---
# Binary Tree Right Side View

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/) · [NeetCode](https://neetcode.io/problems/binary-tree-right-side-view)

**Solve it in:** [[Binary Tree Right Side View]] · **Answer:** [[Binary Tree Right Side View - Solution]]

## Problem

Imagine standing to the right of a binary tree. Given its `root`, return the values of the nodes you can see, ordered from top to bottom — i.e. the **rightmost** node of every level. An empty tree yields `[]`.

## Examples

**Example 1**
```text
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

**Example 2**
```text
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
Explanation: the deepest node 5 sits under the left subtree but is still visible.
```

**Example 3**
```text
Input: root = [1,null,3]
Output: [1,3]
```

## Constraints

- The number of nodes is in the range `[0, 100]`
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.rightSideView(build_tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    assert s.rightSideView(build_tree([1, 2, 3, 4, None, None, None, 5])) == [1, 3, 4, 5]
    assert s.rightSideView(build_tree([1, None, 3])) == [1, 3]
    assert s.rightSideView(build_tree([])) == []
    assert s.rightSideView(build_tree([1, 2])) == [1, 2]  # left child visible when no right
    assert s.rightSideView(build_tree([1, 2, 3, 4, 5, 6, 7])) == [1, 3, 7]
    print("All tests passed!")
```
