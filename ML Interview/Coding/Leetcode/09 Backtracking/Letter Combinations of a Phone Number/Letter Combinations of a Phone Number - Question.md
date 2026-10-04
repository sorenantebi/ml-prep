---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
neetcode: https://neetcode.io/problems/combinations-of-a-phone-number
---
# Letter Combinations of a Phone Number

**Topic:** [[09 Backtracking|Backtracking]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) · [NeetCode](https://neetcode.io/problems/combinations-of-a-phone-number)

**Solve it in:** [[Letter Combinations of a Phone Number]] · **Answer:** [[Letter Combinations of a Phone Number - Solution]]

## Problem

On a classic phone keypad each digit from `2` to `9` maps to a group of letters:

```text
2: abc   3: def   4: ghi   5: jkl
6: mno   7: pqrs  8: tuv   9: wxyz
```

Given a string `digits` containing only characters `'2'`–`'9'`, return every letter string the digits could represent (choose one letter per digit, in order). Return the answer in any order. If `digits` is empty, return an empty list.

## Examples

**Example 1**
```text
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**Example 2**
```text
Input: digits = ""
Output: []
```

**Example 3**
```text
Input: digits = "2"
Output: ["a","b","c"]
```

## Constraints

- `0 <= digits.length <= 4`
- `digits[i]` is in `'2'`–`'9'`

## Starter Code & Test Cases

```python
from typing import List
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.letterCombinations("23")) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert s.letterCombinations("") == []
    assert sorted(s.letterCombinations("2")) == ["a", "b", "c"]
    assert sorted(s.letterCombinations("7")) == ["p", "q", "r", "s"]
    assert sorted(s.letterCombinations("99")) == sorted(a + b for a in "wxyz" for b in "wxyz")
    res = s.letterCombinations("7979")
    assert len(res) == 256 and len(set(res)) == 256
    assert sorted(s.letterCombinations("234")) == sorted("".join(p) for p in product("abc", "def", "ghi"))
    print("All tests passed!")
```
