---
topic: "Graphs"
difficulty: Easy
leetcode: https://leetcode.com/problems/verifying-an-alien-dictionary/
neetcode: https://neetcode.io/problems/verifying-an-alien-dictionary
---
# Verifying An Alien Dictionary - Solution

**Question:** [[Verifying An Alien Dictionary - Question]] · **Difficulty:** Easy

## Intuition

Map each letter to its rank in the alien alphabet. Then the list is sorted if and only if every pair of *adjacent* words is in order, and comparing two words only depends on their first differing character (or on length when one is a prefix of the other).

## Approach

1. Build `rank[ch] = index` from `order`.
2. For each adjacent pair `(w1, w2)`:
   - Scan both words in parallel up to the shorter length.
   - At the first differing character, if `rank[w1[j]] > rank[w2[j]]` return `false`; otherwise this pair is fine — stop scanning.
   - If no difference is found, the pair is invalid only when `w1` is longer than `w2` (prefix rule).
3. If all pairs pass, return `true`.

## Code

```python
from typing import List


class Solution:
	def isAlienSorted(self, words: List[str], order: str) -> bool:
		rank = {ch: i for i, ch in enumerate(order)}
		for w1, w2 in zip(words, words[1:]):
			for a, b in zip(w1, w2):
				if a != b:
					if rank[a] > rank[b]:
						return False
					break  # first difference decides this pair
			else:
				# no difference found: longer word must not come first
				if len(w1) > len(w2):
					return False
		return True
```

## Complexity

- **Time:** `O(C)` — `C` is the total number of characters across all words; each character is compared at most once.
- **Space:** `O(1)` — the rank map has at most 26 entries.

## Other Approaches

- **Key transform + compare:** convert each word to a list of ranks and check `keys == sorted(keys)` (or compare adjacent keys with Python's list comparison) — Time `O(C log n)` for sorting or `O(C)` for adjacent comparison, Space `O(C)`.

## Key Takeaway

To check sortedness under a custom order, translate characters to ranks and only compare adjacent elements; remember the prefix edge case.
