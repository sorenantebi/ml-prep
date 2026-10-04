---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/last-stone-weight-ii/
neetcode: https://neetcode.io/problems/last-stone-weight-ii
---
# Last Stone Weight II

**Topic:** [[14 2-D Dynamic Programming|2-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/last-stone-weight-ii/) · [NeetCode](https://neetcode.io/problems/last-stone-weight-ii)

**Solve it in:** [[Last Stone Weight II]] · **Answer:** [[Last Stone Weight II - Solution]]

## Problem

You have an array `stones` where `stones[i]` is the weight of the `i`-th stone. Repeatedly pick **any two** stones with weights `x <= y` and smash them together:

- If `x == y`, both stones are destroyed.
- If `x != y`, the stone of weight `x` is destroyed and the other stone's weight becomes `y - x`.

The process ends when at most one stone remains. Return the **smallest possible** weight of the remaining stone, or `0` if no stones are left.

## Examples

**Example 1**
```text
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: Smash 2,4 -> 2; 7,8 -> 1; 2,1 -> 1; 1,1 -> 0; leaving [1].
```

**Example 2**
```text
Input: stones = [31,26,33,21,40]
Output: 5
```

**Example 3**
```text
Input: stones = [1,1]
Output: 0
```

## Constraints

- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 100`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.lastStoneWeightII([2, 7, 4, 1, 8, 1]) == 1
    assert s.lastStoneWeightII([31, 26, 33, 21, 40]) == 5
    assert s.lastStoneWeightII([1, 1]) == 0
    assert s.lastStoneWeightII([7]) == 7
    assert s.lastStoneWeightII([1, 2]) == 1
    assert s.lastStoneWeightII([3, 3, 3]) == 3
    assert s.lastStoneWeightII([1, 2, 3]) == 0
    assert s.lastStoneWeightII([100] * 30) == 0
    print("All tests passed!")
```
