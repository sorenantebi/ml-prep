---
topic: "Advanced Graphs"
difficulty: Hard
leetcode: https://leetcode.com/problems/build-a-matrix-with-conditions/
neetcode: https://neetcode.io/problems/build-a-matrix-with-conditions
---
# Build a Matrix With Conditions

**Topic:** [[12 Advanced Graphs|Advanced Graphs]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/build-a-matrix-with-conditions/) · [NeetCode](https://neetcode.io/problems/build-a-matrix-with-conditions)

**Solve it in:** [[Build a Matrix With Conditions]] · **Answer:** [[Build a Matrix With Conditions - Solution]]

## Problem

You are given a positive integer `k` and two lists of conditions:

- `rowConditions[i] = [above_i, below_i]`: number `above_i` must appear in a row strictly above number `below_i`.
- `colConditions[i] = [left_i, right_i]`: number `left_i` must appear in a column strictly left of number `right_i`.

Build a `k x k` matrix that contains each number from `1` to `k` **exactly once**, with every other cell equal to `0`, and that satisfies all conditions. Return any such matrix, or an empty matrix `[]` if none exists.

## Examples

**Example 1**
```text
Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
Output: [[3,0,0],[0,0,1],[0,2,0]]   (one valid answer)
```

**Example 2**
```text
Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
Output: []
Explanation: Rows require 1 above 2 above 3 above 1, a cycle.
```

## Constraints

- `2 <= k <= 400`
- `1 <= rowConditions.length, colConditions.length <= 10^4`
- Each condition is a pair of distinct numbers in `[1, k]`.

## Starter Code & Test Cases

```python
from typing import List
from collections import deque


def is_valid(k, rowConditions, colConditions, mat) -> bool:
    if len(mat) != k or any(len(row) != k for row in mat):
        return False
    pos = {}
    for r in range(k):
        for c in range(k):
            v = mat[r][c]
            if v != 0:
                if v in pos or not 1 <= v <= k:
                    return False
                pos[v] = (r, c)
    if len(pos) != k:
        return False
    return (all(pos[a][0] < pos[b][0] for a, b in rowConditions)
            and all(pos[a][1] < pos[b][1] for a, b in colConditions))


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    args = (3, [[1,2],[3,2]], [[2,1],[3,2]])
    assert is_valid(*args, s.buildMatrix(*args))
    assert s.buildMatrix(3, [[1,2],[2,3],[3,1],[2,3]], [[2,1]]) == []
    args = (2, [[1,2]], [[2,1]])
    assert is_valid(*args, s.buildMatrix(*args))
    assert s.buildMatrix(2, [[1,2],[2,1]], [[1,2]]) == []
    assert s.buildMatrix(4, [[1,2]], [[1,2],[2,3],[3,4],[4,1]]) == []
    args = (4, [[4,3],[3,2],[2,1]], [[1,2],[1,3],[1,4]])
    assert is_valid(*args, s.buildMatrix(*args))
    args = (5, [[1,2],[1,2],[3,4]], [[5,1]])
    assert is_valid(*args, s.buildMatrix(*args))
    print("All tests passed!")
```
