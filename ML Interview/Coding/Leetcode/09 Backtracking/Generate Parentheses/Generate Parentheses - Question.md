---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/generate-parentheses/
neetcode: https://neetcode.io/problems/generate-parentheses
---
# Generate Parentheses

**Topic:** [[09 Backtracking|Backtracking]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/generate-parentheses/) · [NeetCode](https://neetcode.io/problems/generate-parentheses)

**Solve it in:** [[Generate Parentheses]] · **Answer:** [[Generate Parentheses - Solution]]

## Problem

Given an integer `n`, return every string made of exactly `n` opening and `n` closing parentheses that is **well-formed** (every `'('` is matched by a later `')'`, and no prefix has more `')'` than `'('`). The strings may be returned in any order.

## Examples

**Example 1**
```text
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2**
```text
Input: n = 1
Output: ["()"]
```

## Constraints

- `1 <= n <= 8`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pass  # your code here


def valid(p: str) -> bool:
    bal = 0
    for ch in p:
        bal += 1 if ch == "(" else -1
        if bal < 0:
            return False
    return bal == 0


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.generateParenthesis(3)) == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
    assert s.generateParenthesis(1) == ["()"]
    assert sorted(s.generateParenthesis(2)) == ["(())", "()()"]
    catalan = [1, 1, 2, 5, 14, 42, 132, 429, 1430]
    for n in range(1, 9):
        res = s.generateParenthesis(n)
        assert len(res) == catalan[n] == len(set(res))
        assert all(len(p) == 2 * n and valid(p) for p in res)
    print("All tests passed!")
```
