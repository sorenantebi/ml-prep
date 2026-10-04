---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/combinations/
neetcode: https://neetcode.io/problems/combinations
---
# Combinations

**Topic:** [[09 Backtracking|Backtracking]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/combinations/) · [NeetCode](https://neetcode.io/problems/combinations)

**Solve it in:** [[Combinations]] · **Answer:** [[Combinations - Solution]]

## Problem

Given two integers `n` and `k`, return every possible combination of `k` distinct numbers chosen from the range `[1, n]`.

A combination is unordered (`[1,2]` and `[2,1]` are the same), so each set should appear once. The answer may be returned in any order.

## Examples

**Example 1**
```text
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
```

**Example 2**
```text
Input: n = 1, k = 1
Output: [[1]]
```

## Constraints

- `1 <= n <= 20`
- `1 <= k <= n`

## Starter Code & Test Cases

```python
from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        pass  # your code here


def norm(res):
    return sorted(sorted(x) for x in res)


if __name__ == "__main__":
    s = Solution()
    assert norm(s.combine(4, 2)) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert norm(s.combine(1, 1)) == [[1]]
    assert norm(s.combine(3, 3)) == [[1, 2, 3]]
    assert norm(s.combine(5, 1)) == [[1], [2], [3], [4], [5]]
    assert norm(s.combine(5, 3)) == norm(combinations(range(1, 6), 3))
    res = s.combine(20, 10)
    assert len(res) == 184756
    assert len(set(map(tuple, map(sorted, res)))) == 184756
    print("All tests passed!")
```
