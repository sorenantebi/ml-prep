---
topic: "Binary Search"
difficulty: Easy
leetcode: https://leetcode.com/problems/guess-number-higher-or-lower/
neetcode: https://neetcode.io/problems/guess-number-higher-or-lower
---
# Guess Number Higher Or Lower - Solution

**Question:** [[Guess Number Higher Or Lower - Question]] · **Difficulty:** Easy

## Intuition

`guess` tells us which side of our guess the hidden number lies on, which is exactly the comparison a binary search needs. Halving the candidate range each call finds the number in about `log2(n)` guesses.

## Approach

1. Set `lo = 1`, `hi = n`.
2. While `lo <= hi`: guess `mid`.
3. If the result is `0`, return `mid`; if `-1` (too high) set `hi = mid - 1`; if `1` (too low) set `lo = mid + 1`.

## Code

```python
# The guess API is already defined for you.
# def guess(num: int) -> int:

class Solution:
	def guessNumber(self, n: int) -> int:
		lo, hi = 1, n
		while lo <= hi:
			mid = (lo + hi) // 2
			res = guess(mid)
			if res == 0:
				return mid
			if res == -1:      # mid is too high
				hi = mid - 1
			else:              # mid is too low
				lo = mid + 1
		return -1  # unreachable for valid input
```

## Complexity

- **Time:** `O(log n)` — one API call per halving step.
- **Space:** `O(1)`.

## Other Approaches

- **Linear guessing:** try `1, 2, 3, …` until `guess` returns `0` — Time `O(n)`, Space `O(1)` (too slow for `n` near `2^31`).
- **Ternary search:** split into thirds with two guesses per step — Time `O(log n)` but more calls on average than binary search.

## Key Takeaway

Any oracle that answers "too high / too low / correct" turns the problem into standard binary search; be careful to map the API's sign convention to the right half.
