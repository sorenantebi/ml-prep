---
topic: "Trees"
difficulty: Medium
leetcode: https://leetcode.com/problems/delete-leaves-with-a-given-value/
neetcode: https://neetcode.io/problems/delete-leaves-with-a-given-value
---
# Delete Leaves With a Given Value

**Topic:** [[07 Trees|Trees]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/delete-leaves-with-a-given-value/) · [NeetCode](https://neetcode.io/problems/delete-leaves-with-a-given-value)

**Solve it in:** [[Delete Leaves With a Given Value]] · **Answer:** [[Delete Leaves With a Given Value - Solution]]

## Problem

Given the `root` of a binary tree and an integer `target`, delete every **leaf** whose value equals `target`. Deleting leaves can turn their parent into a new leaf; if that parent also has value `target`, it must be deleted too, and so on, until no leaf with value `target` remains. Return the resulting root (which may be `null`).

## Examples

**Example 1**
```text
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: the 2-leaves go first; then the left child 2 becomes a leaf and is removed too.
```

**Example 2**
```text
Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]
```

**Example 3**
```text
Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
```

## Constraints

- The number of nodes is in the range `[1, 3000]`
- `1 <= Node.val, target <= 1000`

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
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert tree_to_list(s.removeLeafNodes(build_tree([1, 2, 3, 2, None, 2, 4]), 2)) == [1, None, 3, None, 4]
    assert tree_to_list(s.removeLeafNodes(build_tree([1, 3, 3, 3, 2]), 3)) == [1, 3, None, None, 2]
    assert tree_to_list(s.removeLeafNodes(build_tree([1, 2, None, 2, None, 2]), 2)) == [1]
    assert tree_to_list(s.removeLeafNodes(build_tree([1, 1, 1]), 1)) == []   # whole tree removed
    assert tree_to_list(s.removeLeafNodes(build_tree([1, 2, 3]), 1)) == [1, 2, 3]  # root is not a leaf
    assert tree_to_list(s.removeLeafNodes(build_tree([5]), 5)) == []
    assert tree_to_list(s.removeLeafNodes(build_tree([2, 2, 2, 3]), 2)) == [2, 2, None, 3]
    print("All tests passed!")
```
