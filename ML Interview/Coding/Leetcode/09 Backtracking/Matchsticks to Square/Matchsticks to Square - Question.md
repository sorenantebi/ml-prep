---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/matchsticks-to-square/
neetcode: https://neetcode.io/problems/matchsticks-to-square
---
# Matchsticks to Square

**Topic:** [[09 Backtracking|Backtracking]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/matchsticks-to-square/) · [NeetCode](https://neetcode.io/problems/matchsticks-to-square)

**Solve it in:** [[Matchsticks to Square]] · **Answer:** [[Matchsticks to Square - Solution]]

## Problem

You are given an array `matchsticks` where `matchsticks[i]` is the length of the `i`-th stick. Determine whether **all** of the sticks can be arranged to form a square. Sticks cannot be broken, but they may be joined end to end, and each stick must be used exactly once.

Return `true` if a square can be formed, otherwise `false`.

## Examples

**Example 1**
```text
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: sides 2, 2, 2 and 1+1 give a square of side 2
```

**Example 2**
```text
Input: matchsticks = [3,3,3,3,4]
Output: false
```

## Constraints

- `1 <= matchsticks.length <= 15`
- `1 <= matchsticks[i] <= 10^8`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.makesquare([1, 1, 2, 2, 2]) is True
    assert s.makesquare([3, 3, 3, 3, 4]) is False
    assert s.makesquare([5]) is False
    assert s.makesquare([1, 1, 1, 1]) is True
    assert s.makesquare([2, 2, 2, 2, 2, 6]) is False  # sum 16 but a side of 4 can't hold the 6
    assert s.makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]) is True
    assert s.makesquare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 3, 2, 1]) is False
    assert s.makesquare([10, 6, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2]) is True
    assert s.makesquare([100000000] * 4) is True
    print("All tests passed!")
```
