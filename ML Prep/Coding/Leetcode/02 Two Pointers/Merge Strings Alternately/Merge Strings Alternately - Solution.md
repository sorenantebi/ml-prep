---
topic: "Two Pointers"
difficulty: Easy
leetcode: https://leetcode.com/problems/merge-strings-alternately/
neetcode: https://neetcode.io/problems/merge-strings-alternately
---
# Merge Strings Alternately - Solution

**Question:** [[Merge Strings Alternately - Question]] · **Difficulty:** Easy

## Intuition

Walk one index through both strings at the same time, appending from each while it still has characters. Whatever is left in the longer string is appended at the end automatically because the shorter one stops contributing.

## Approach

1. Create an empty list `res`.
2. For `i` from `0` to `max(len(word1), len(word2)) - 1`:
   - If `i < len(word1)`, append `word1[i]`.
   - If `i < len(word2)`, append `word2[i]`.
3. Return `"".join(res)`.

## Code

```python
class Solution:
	def mergeAlternately(self, word1: str, word2: str) -> str:
		res = []
		for i in range(max(len(word1), len(word2))):
			if i < len(word1):
				res.append(word1[i])
			if i < len(word2):
				res.append(word2[i])
		return "".join(res)
```

## Complexity

- **Time:** `O(n + m)` — each character is appended once.
- **Space:** `O(n + m)` — for the output string.

## Other Approaches

- **Two explicit pointers:** advance `i` and `j` while both are in range, then append `word1[i:]` and `word2[j:]` — Time `O(n + m)`, Space `O(n + m)`.

## Key Takeaway

Build strings with a list and `"".join` to avoid quadratic concatenation; handle unequal lengths by checking bounds or appending the tail.
