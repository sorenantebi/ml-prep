---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/group-anagrams/
neetcode: https://neetcode.io/problems/anagram-groups
---
# Group Anagrams - Solution

**Question:** [[Group Anagrams - Question]] · **Difficulty:** Medium

## Intuition

All anagrams share the same letter-frequency signature. If we compute a canonical key for each word (a 26-length count tuple, or the sorted word) and bucket words by that key in a hash map, each bucket is one anagram group.

## Approach

1. Create a `defaultdict(list)` called `groups`.
2. For each word, build a 26-entry count array of its letters and convert it to a tuple (hashable key).
3. Append the word to `groups[key]`.
4. Return the list of bucket values.

## Code

```python
from collections import defaultdict
from typing import List


class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		groups = defaultdict(list)
		for word in strs:
			count = [0] * 26
			for ch in word:
				count[ord(ch) - ord("a")] += 1
			groups[tuple(count)].append(word)  # tuple is hashable; identical for anagrams
		return list(groups.values())
```

## Complexity

- **Time:** `O(n · k)` — `n` words of max length `k`, each counted in `O(k)` (plus `O(26)` to build the key).
- **Space:** `O(n · k)` — the map stores every word plus one key per group.

## Other Approaches

- **Sorted-string key:** use `"".join(sorted(word))` as the key — Time `O(n · k log k)`, Space `O(n · k)`.

## Key Takeaway

Grouping by an equivalence relation = hash map from a canonical form to a list; for anagrams the canonical form is the sorted word or its letter-count tuple.
