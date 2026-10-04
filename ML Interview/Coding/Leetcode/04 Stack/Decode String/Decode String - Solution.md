---
topic: "Stack"
difficulty: Medium
leetcode: https://leetcode.com/problems/decode-string/
neetcode: https://neetcode.io/problems/decode-string
---
# Decode String - Solution

**Question:** [[Decode String - Question]] · **Difficulty:** Medium

## Intuition

Each `[` starts a new nested context whose result must later be repeated and appended to the context outside it. A stack saves the outer context (string built so far and the repeat count) when entering a bracket, and restores it when the bracket closes.

## Approach

1. Maintain `cur` (string of the current level) and `num` (count being parsed).
2. Digit: `num = num * 10 + digit` (counts can have several digits).
3. `[`: push `(cur, num)`, then reset `cur = ""`, `num = 0`.
4. `]`: pop `(prev, k)` and set `cur = prev + cur * k`.
5. Letter: append to `cur`.
6. Return `cur`.

## Code

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # (string before '[', repeat count)
        cur, num = "", 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append((cur, num))
                cur, num = "", 0
            elif ch == "]":
                prev, k = stack.pop()
                cur = prev + cur * k
            else:
                cur += ch
        return cur
```

## Complexity

- **Time:** `O(m)` where `m` is the decoded length (times nesting depth for repeated string copying) — the output must be built anyway.
- **Space:** `O(m)` — the partial strings plus a stack as deep as the nesting.

## Other Approaches

- **Recursive descent:** a function parses from index `i` until a `]`, recursing on each `k[` — Time `O(m)`, Space `O(m)` including recursion depth.

## Key Takeaway

For nested structures, push the outer context on `[`/`(` and combine on `]`/`)` — the same pattern as calculators and nested-list parsers.
