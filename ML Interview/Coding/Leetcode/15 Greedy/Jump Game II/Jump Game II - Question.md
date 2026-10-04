---
topic: "Greedy"
difficulty: Medium
leetcode: https://leetcode.com/problems/jump-game-ii/
neetcode: https://neetcode.io/problems/jump-game-ii
---
# Jump Game II

**Topic:** [[15 Greedy|Greedy]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/jump-game-ii/) · [NeetCode](https://neetcode.io/problems/jump-game-ii)

**Solve it in:** [[Jump Game II]] · **Answer:** [[Jump Game II - Solution]]

## Problem

You are given an integer array `nums` and start at index `0`. From index `i` you may jump forward to any index `i + j` with `0 <= j <= nums[i]` and `i + j < n`. Return the **minimum number of jumps** needed to reach index `n - 1`. The input is guaranteed to allow reaching the last index.

## Examples

**Example 1**
```text
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: 0 -> 1 -> 4
```

**Example 2**
```text
Input: nums = [2,3,0,1,4]
Output: 2
```

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- The last index is always reachable.

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.jump([2, 3, 1, 1, 4]) == 2
    assert s.jump([2, 3, 0, 1, 4]) == 2
    assert s.jump([0]) == 0
    assert s.jump([1, 1, 1, 1]) == 3
    assert s.jump([5, 1, 1, 1, 1]) == 1
    assert s.jump([1, 2, 3]) == 2
    assert s.jump([2, 1]) == 1
    assert s.jump([1, 2, 1, 1, 1]) == 3
    print("All tests passed!")
```
