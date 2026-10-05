---
topic: "Math & Geometry"
difficulty: Easy
leetcode: https://leetcode.com/problems/excel-sheet-column-title/
neetcode: https://neetcode.io/problems/excel-sheet-column-title
---
# Excel Sheet Column Title - Solution

**Question:** [[Excel Sheet Column Title - Question]] · **Difficulty:** Easy

## Intuition

This is base-26 conversion, except the digits run from 1 to 26 instead of 0 to 25. Subtracting 1 before each `% 26` and `// 26` shifts the digit into the familiar 0-based range, so `Z` (26) is handled correctly instead of becoming a "zero".

## Approach

1. While `columnNumber > 0`, decrement it by 1 to make the current digit 0-based.
2. Append the letter `chr(ord('A') + columnNumber % 26)`.
3. Integer-divide `columnNumber` by 26 to move on to the next digit.
4. The letters were produced least-significant first, so reverse them and join.

## Code

```python
class Solution:
	def convertToTitle(self, columnNumber: int) -> str:
		res = []
		while columnNumber > 0:
			columnNumber -= 1  # shift 1..26 to 0..25 so 'Z' doesn't become 0
			res.append(chr(ord('A') + columnNumber % 26))
			columnNumber //= 26
		return "".join(reversed(res))
```

## Complexity

- **Time:** `O(log_26 n)`: there is one iteration per output letter.
- **Space:** `O(log_26 n)`: the list of letters, which is also the output.

## Other Approaches

- **Recursive:** `convertToTitle((n - 1) // 26) + chr(ord('A') + (n - 1) % 26)`, with base case `n == 0` returning `""`. Time `O(log n)`, Space `O(log n)` for the recursion stack.

## Key Takeaway

In a "bijective" base with no zero digit, subtract 1 before taking the modulus and dividing. The same trick applies whenever labels start at 1, not 0.
