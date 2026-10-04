---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/subsets-ii/
neetcode: https://neetcode.io/problems/subsets-ii
---
# Subsets II

**Topic:** [[09 Backtracking|Backtracking]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/subsets-ii/) · [NeetCode](https://neetcode.io/problems/subsets-ii)

**Solve it in:** [[Subsets II]] · **Answer:** [[Subsets II - Solution]]

## Problem

Given an integer array `nums` that **may contain duplicate values**, return all distinct subsets (the power set). Two subsets with the same multiset of values count as the same subset and must appear only once.

The subsets may be returned in any order.

## Examples

**Example 1**
```text
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

**Example 2**
```text
Input: nums = [0]
Output: [[],[0]]
```

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

## Starter Code & Test Cases

```python
from typing import List
from itertools import combinations


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        pass  # your code here


def norm(res):
    return sorted(sorted(x) for x in res)


def brute(nums):
    return [list(t) for t in {tuple(sorted(c)) for r in range(len(nums) + 1) for c in combinations(nums, r)}]


if __name__ == "__main__":
    s = Solution()
    assert norm(s.subsetsWithDup([1, 2, 2])) == norm([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
    assert norm(s.subsetsWithDup([0])) == norm([[], [0]])
    assert norm(s.subsetsWithDup([3, 3, 3])) == norm([[], [3], [3, 3], [3, 3, 3]])
    assert norm(s.subsetsWithDup([4, 4, 4, 1, 4])) == norm(brute([4, 4, 4, 1, 4]))
    for case in ([1, 2, 3], [-1, 1, -1, 1], [5, 5, 2, 2, 0, 0, 7, 7, 7, 7]):
        res = s.subsetsWithDup(case)
        assert len(res) == len(set(tuple(sorted(x)) for x in res))  # no duplicates
        assert norm(res) == norm(brute(case))
    print("All tests passed!")
```
