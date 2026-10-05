# Evaluate Reverse Polish Notation

You are given an arithmetic expression written in Reverse Polish Notation (postfix) as an array of strings `tokens`. Each token is either an integer or one of the operators `"+"`, `"-"`, `"*"`, `"/"`. Evaluate the expression and return its integer value.

Rules:

- Each operator applies to the two most recent operands (the first popped is the right operand).
- Integer division truncates toward zero (e.g. `-7 / 2 = -3`).
- There is never division by zero, the expression is always valid, and every intermediate result fits in a 32-bit signed integer.

## Example

```text
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: (2 + 1) * 3 = 9
```

```python

```
