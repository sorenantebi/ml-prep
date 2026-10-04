---
topic: "Bit Manipulation"
difficulty: Easy
leetcode: https://leetcode.com/problems/missing-number/
neetcode: https://neetcode.io/problems/missing-number
---
# Missing Number

**Topic:** [[18 Bit Manipulation|Bit Manipulation]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/missing-number/) · [NeetCode](https://neetcode.io/problems/missing-number)

**Solve it in:** [[Missing Number]] · **Answer:** [[Missing Number - Solution]]

## Problem

You are given an array `nums` of `n` **distinct** integers taken from the range `[0, n]`. Exactly one number in that range is absent from the array. Return the missing number.

Follow-up: solve it with `O(1)` extra space and `O(n)` time.

## Examples

**Example 1**
```text
Input: nums = [3,0,1]
Output: 2
```

**Example 2**
```text
Input: nums = [0,1]
Output: 2
Explanation: n = 2, so the range is [0, 2]; 2 is missing.
```

**Example 3**
```text
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
```

## Constraints

- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- All values in `nums` are unique.

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.missingNumber([3, 0, 1]) == 2
    assert s.missingNumber([0, 1]) == 2
    assert s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert s.missingNumber([0]) == 1
    assert s.missingNumber([1]) == 0
    assert s.missingNumber([1, 2, 3]) == 0
    big = list(range(10001))
    big.remove(4242)
    assert s.missingNumber(big[::-1]) == 4242
    print("All tests passed!")
```
