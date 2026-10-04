---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/permutations/
neetcode: https://neetcode.io/problems/permutations
---
# Permutations

**Topic:** [[09 Backtracking|Backtracking]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/permutations/) · [NeetCode](https://neetcode.io/problems/permutations)

**Solve it in:** [[Permutations]] · **Answer:** [[Permutations - Solution]]

## Problem

Given an array `nums` of **distinct** integers, return every possible ordering (permutation) of its elements. The permutations can be returned in any order.

## Examples

**Example 1**
```text
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Example 2**
```text
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

**Example 3**
```text
Input: nums = [1]
Output: [[1]]
```

## Constraints

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All values in `nums` are unique

## Starter Code & Test Cases

```python
from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pass  # your code here


def norm(res):
    return sorted(map(list, res))


if __name__ == "__main__":
    s = Solution()
    assert norm(s.permute([1, 2, 3])) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert norm(s.permute([0, 1])) == [[0, 1], [1, 0]]
    assert norm(s.permute([1])) == [[1]]
    assert norm(s.permute([-1, 5, 0])) == norm(permutations([-1, 5, 0]))
    res = s.permute([1, 2, 3, 4, 5, 6])
    assert len(res) == 720 and norm(res) == norm(permutations([1, 2, 3, 4, 5, 6]))
    print("All tests passed!")
```
