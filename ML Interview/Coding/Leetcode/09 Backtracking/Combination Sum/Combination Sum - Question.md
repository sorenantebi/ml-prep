---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/combination-sum/
neetcode: https://neetcode.io/problems/combination-target-sum
---
# Combination Sum

**Topic:** [[09 Backtracking|Backtracking]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/combination-sum/) · [NeetCode](https://neetcode.io/problems/combination-target-sum)

**Solve it in:** [[Combination Sum]] · **Answer:** [[Combination Sum - Solution]]

## Problem

Given an array of **distinct** positive integers `candidates` and a positive integer `target`, return all unique combinations of candidates whose sum equals `target`. The same candidate may be used **any number of times**.

Two combinations are considered the same if they use each number the same number of times (order does not matter). Return the combinations in any order. The test data guarantees fewer than 150 valid combinations.

## Examples

**Example 1**
```text
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
```

**Example 2**
```text
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

**Example 3**
```text
Input: candidates = [2], target = 1
Output: []
```

## Constraints

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`, all distinct
- `1 <= target <= 40`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        pass  # your code here


def norm(res):
    return sorted(sorted(x) for x in res)


if __name__ == "__main__":
    s = Solution()
    assert norm(s.combinationSum([2, 3, 6, 7], 7)) == norm([[2, 2, 3], [7]])
    assert norm(s.combinationSum([2, 3, 5], 8)) == norm([[2, 2, 2, 2], [2, 3, 3], [3, 5]])
    assert s.combinationSum([2], 1) == []
    assert norm(s.combinationSum([2], 6)) == [[2, 2, 2]]
    assert norm(s.combinationSum([7, 3, 2], 18)) == norm([
        [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 3, 3], [2, 2, 2, 2, 3, 7],
        [2, 2, 2, 3, 3, 3, 3], [2, 2, 7, 7], [2, 3, 3, 3, 7], [3, 3, 3, 3, 3, 3],
    ])
    assert norm(s.combinationSum([5, 10], 3)) == []
    assert norm(s.combinationSum([8, 4], 8)) == norm([[8], [4, 4]])
    print("All tests passed!")
```
