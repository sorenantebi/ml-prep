---
topic: "Stack"
difficulty: Medium
leetcode: https://leetcode.com/problems/evaluate-reverse-polish-notation/
neetcode: https://neetcode.io/problems/evaluate-reverse-polish-notation
---
# Evaluate Reverse Polish Notation

**Topic:** [[04 Stack|Stack]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/) · [NeetCode](https://neetcode.io/problems/evaluate-reverse-polish-notation)

**Solve it in:** [[Evaluate Reverse Polish Notation]] · **Answer:** [[Evaluate Reverse Polish Notation - Solution]]

## Problem

You are given an arithmetic expression written in Reverse Polish Notation (postfix) as an array of strings `tokens`. Each token is either an integer or one of the operators `"+"`, `"-"`, `"*"`, `"/"`. Evaluate the expression and return its integer value.

Rules:

- Each operator applies to the two most recent operands (the first popped is the right operand).
- Integer division truncates toward zero (e.g. `-7 / 2 = -3`).
- There is never division by zero, the expression is always valid, and every intermediate result fits in a 32-bit signed integer.

## Examples

**Example 1**
```text
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: (2 + 1) * 3 = 9
```

**Example 2**
```text
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: 4 + (13 / 5) = 4 + 2 = 6
```

**Example 3**
```text
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
```

## Constraints

- `1 <= tokens.length <= 10^4`
- `tokens[i]` is an operator or an integer in `[-200, 200]`

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    assert s.evalRPN(["42"]) == 42
    assert s.evalRPN(["-7", "2", "/"]) == -3   # truncate toward zero
    assert s.evalRPN(["7", "-2", "/"]) == -3
    assert s.evalRPN(["3", "5", "-"]) == -2      # operand order matters
    assert s.evalRPN(["-4", "-3", "*"]) == 12
    print("All tests passed!")
```
