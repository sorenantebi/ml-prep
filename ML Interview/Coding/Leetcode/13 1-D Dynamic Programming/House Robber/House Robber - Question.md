---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/house-robber/
neetcode: https://neetcode.io/problems/house-robber
---
# House Robber

**Topic:** [[13 1-D Dynamic Programming|1-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/house-robber/) · [NeetCode](https://neetcode.io/problems/house-robber)

**Solve it in:** [[House Robber]] · **Answer:** [[House Robber - Solution]]

## Problem

Houses along a street each hold some amount of money, given by `nums[i]`. You want to take as much money as possible, but you cannot take from two **adjacent** houses (it would trigger an alarm). Return the maximum total you can collect.

## Examples

**Example 1**
```text
Input: nums = [1,2,3,1]
Output: 4
Explanation: Take houses 0 and 2: 1 + 3.
```

**Example 2**
```text
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Take houses 0, 2, 4: 2 + 9 + 1.
```

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.rob([1,2,3,1]) == 4
    assert s.rob([2,7,9,3,1]) == 12
    assert s.rob([5]) == 5
    assert s.rob([2,1,1,2]) == 4
    assert s.rob([0,0]) == 0
    assert s.rob([1,3,1]) == 3
    assert s.rob([400] * 100) == 20000
    print("All tests passed!")
```
