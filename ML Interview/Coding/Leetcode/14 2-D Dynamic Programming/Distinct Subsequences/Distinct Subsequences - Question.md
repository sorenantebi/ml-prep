---
topic: "2-D Dynamic Programming"
difficulty: Hard
leetcode: https://leetcode.com/problems/distinct-subsequences/
neetcode: https://neetcode.io/problems/count-subsequences
---
# Distinct Subsequences

**Topic:** [[14 2-D Dynamic Programming|2-D Dynamic Programming]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/distinct-subsequences/) · [NeetCode](https://neetcode.io/problems/count-subsequences)

**Solve it in:** [[Distinct Subsequences]] · **Answer:** [[Distinct Subsequences - Solution]]

## Problem

Given two strings `s` and `t`, return the number of distinct **subsequences** of `s` that are equal to `t`. Two subsequences are different if they use a different set of index positions in `s`, even if the resulting strings look the same.

The answer fits in a 32-bit signed integer.

## Examples

**Example 1**
```text
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation: Any one of the three 'b's can be the one left out.
```

**Example 2**
```text
Input: s = "babgbag", t = "bag"
Output: 5
```

## Constraints

- `1 <= s.length, t.length <= 1000`
- `s` and `t` consist of English letters.

## Starter Code & Test Cases

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        pass  # your code here


if __name__ == "__main__":
    sol = Solution()
    assert sol.numDistinct("rabbbit", "rabbit") == 3
    assert sol.numDistinct("babgbag", "bag") == 5
    assert sol.numDistinct("abc", "abc") == 1
    assert sol.numDistinct("abc", "abcd") == 0  # t longer than s
    assert sol.numDistinct("aaa", "a") == 3
    assert sol.numDistinct("aaaa", "aa") == 6
    assert sol.numDistinct("xyz", "a") == 0
    assert sol.numDistinct("b", "b") == 1
    print("All tests passed!")
```
