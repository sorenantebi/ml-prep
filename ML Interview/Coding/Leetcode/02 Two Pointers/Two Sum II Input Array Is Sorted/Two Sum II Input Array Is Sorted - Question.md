---
topic: "Two Pointers"
difficulty: Medium
leetcode: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
neetcode: https://neetcode.io/problems/two-integer-sum-ii
---
# Two Sum II Input Array Is Sorted

**Topic:** [[02 Two Pointers|Two Pointers]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) · [NeetCode](https://neetcode.io/problems/two-integer-sum-ii)

**Solve it in:** [[Two Sum II Input Array Is Sorted]] · **Answer:** [[Two Sum II Input Array Is Sorted - Solution]]

## Problem

You are given a **1-indexed** integer array `numbers` sorted in non-decreasing order and an integer `target`. Find the two distinct positions `index1 < index2` whose values add up to `target`, and return them as `[index1, index2]` (both 1-based). Exactly one valid answer is guaranteed, and you may not use the same element twice. The solution must use only constant extra space.

## Examples

**Example 1**
```text
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: 2 + 7 == 9
```

**Example 2**
```text
Input: numbers = [2,3,4], target = 6
Output: [1,3]
```

**Example 3**
```text
Input: numbers = [-1,0], target = -1
Output: [1,2]
```

## Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`, sorted non-decreasing
- `-1000 <= target <= 1000`
- Exactly one solution exists

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pass  # your code here


if __name__ == "__main__":
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert sol.twoSum([2, 3, 4], 6) == [1, 3]
    assert sol.twoSum([-1, 0], -1) == [1, 2]
    assert sol.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5]
    assert sol.twoSum([-5, -3, 0, 2, 8], 5) == [2, 5]
    assert sol.twoSum([5, 25, 75], 100) == [2, 3]
    assert sol.twoSum(list(range(1, 1001)), 1999) == [999, 1000]
    print("All tests passed!")
```
