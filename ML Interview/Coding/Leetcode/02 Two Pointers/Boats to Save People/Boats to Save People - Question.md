---
topic: "Two Pointers"
difficulty: Medium
leetcode: https://leetcode.com/problems/boats-to-save-people/
neetcode: https://neetcode.io/problems/boats-to-save-people
---
# Boats to Save People

**Topic:** [[02 Two Pointers|Two Pointers]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/boats-to-save-people/) · [NeetCode](https://neetcode.io/problems/boats-to-save-people)

**Solve it in:** [[Boats to Save People]] · **Answer:** [[Boats to Save People - Solution]]

## Problem

You are given an array `people` where `people[i]` is the weight of person `i`, and an unlimited number of boats, each with weight capacity `limit`. A boat carries **at most two** people at once, provided their combined weight is at most `limit`. Every individual weight is at most `limit`. Return the minimum number of boats needed to carry everyone.

## Examples

**Example 1**
```text
Input: people = [1,2], limit = 3
Output: 1
```

**Example 2**
```text
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: (1,2), (2), (3)
```

**Example 3**
```text
Input: people = [3,5,3,4], limit = 5
Output: 4
```

## Constraints

- `1 <= people.length <= 5 * 10^4`
- `1 <= people[i] <= limit <= 3 * 10^4`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        pass  # your code here


if __name__ == "__main__":
    sol = Solution()
    assert sol.numRescueBoats([1, 2], 3) == 1
    assert sol.numRescueBoats([3, 2, 2, 1], 3) == 3
    assert sol.numRescueBoats([3, 5, 3, 4], 5) == 4
    assert sol.numRescueBoats([5], 5) == 1
    assert sol.numRescueBoats([1, 1, 1, 1], 2) == 2
    assert sol.numRescueBoats([2, 4, 1, 3, 5], 6) == 3
    assert sol.numRescueBoats([2, 49, 10, 30, 50, 21], 50) == 4
    print("All tests passed!")
```
