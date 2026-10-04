---
topic: "Arrays & Hashing"
difficulty: Easy
leetcode: https://leetcode.com/problems/longest-common-prefix/
neetcode: https://neetcode.io/problems/longest-common-prefix
---
# Longest Common Prefix - Solution

**Question:** [[Longest Common Prefix - Question]] · **Difficulty:** Easy

## Intuition

The common prefix can be no longer than the shortest string. Compare characters column by column (vertical scanning): the first column where any string ends or disagrees with the first string marks the end of the prefix.

## Approach

1. Use the first string as the reference.
2. For each index `i` in the reference, look at every other string.
3. If some string has length `<= i` or a different character at `i`, return `ref[:i]`.
4. If the loop completes, the whole reference is the common prefix.

## Code

```python
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = strs[0]
        for i, ch in enumerate(ref):
            for word in strs[1:]:
                # stop at the first column that runs off a word or mismatches
                if i == len(word) or word[i] != ch:
                    return ref[:i]
        return ref
```

## Complexity

- **Time:** `O(S)` — where `S` is the total number of characters; each character is compared at most once.
- **Space:** `O(1)` — besides the returned slice.

## Other Approaches

- **Sort then compare first and last:** after sorting, the common prefix of the lexicographically smallest and largest strings is the answer — Time `O(n · m log n)`, Space `O(1)` extra.
- **Trie:** insert all words and walk down while a node has a single child and is not a word end — Time `O(S)`, Space `O(S)`.

## Key Takeaway

Vertical scanning stops as early as possible and handles empty strings naturally; the "min vs max after sorting" trick is a neat shortcut to remember.
