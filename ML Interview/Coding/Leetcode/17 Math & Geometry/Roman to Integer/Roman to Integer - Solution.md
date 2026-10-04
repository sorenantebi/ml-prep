---
topic: "Math & Geometry"
difficulty: Easy
leetcode: https://leetcode.com/problems/roman-to-integer/
neetcode: https://neetcode.io/problems/roman-to-integer
---
# Roman to Integer - Solution

**Question:** [[Roman to Integer - Question]] · **Difficulty:** Easy

## Intuition

A symbol is subtracted exactly when the symbol right after it has a larger value; otherwise it is added. A single left-to-right scan that compares each symbol with its right neighbour therefore handles all six subtractive pairs, with no special cases.

## Approach

1. Map each symbol to its value.
2. For each index `i`, if `i + 1 < len(s)` and `val[s[i]] < val[s[i+1]]`, subtract `val[s[i]]`; otherwise add it.
3. Return the total.

## Code

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for i, ch in enumerate(s):
            # Smaller symbol before a larger one is subtractive (IV, IX, XL, ...)
            if i + 1 < len(s) and val[ch] < val[s[i + 1]]:
                total -= val[ch]
            else:
                total += val[ch]
        return total
```

## Complexity

- **Time:** `O(n)`: one pass over the string.
- **Space:** `O(1)`: the lookup table has a fixed size of 7 entries.

## Other Approaches

- **Right-to-left with previous value:** scan backwards and subtract a value when it is smaller than the largest value seen so far, otherwise add it. Time `O(n)`, Space `O(1)`.
- **Two-character lookup table:** check the six subtractive pairs first, then single symbols. Time `O(n)`, Space `O(1)`.

## Key Takeaway

When a symbol's sign depends on its neighbour, compare adjacent elements in one pass instead of listing special cases.
