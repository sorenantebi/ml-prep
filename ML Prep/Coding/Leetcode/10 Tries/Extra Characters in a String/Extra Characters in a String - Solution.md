---
topic: "Tries"
difficulty: Medium
leetcode: https://leetcode.com/problems/extra-characters-in-a-string/
neetcode: https://neetcode.io/problems/extra-characters-in-a-string
---
# Extra Characters in a String - Solution

**Question:** [[Extra Characters in a String - Question]] · **Difficulty:** Medium

## Intuition

Let `dp[i]` be the minimum extra characters for the suffix `s[i:]`. At position `i` we either skip `s[i]` (cost `1 + dp[i + 1]`) or use a dictionary word that starts at `i` and ends at `j` (cost `dp[j + 1]`). A trie of the dictionary lets us enumerate all words starting at `i` in a single forward walk, stopping as soon as no word can continue.

## Approach

1. Insert all dictionary words into a trie.
2. Set `dp[n] = 0` and fill `dp` from `i = n - 1` down to `0`.
3. Start with `dp[i] = 1 + dp[i + 1]` (treat `s[i]` as extra).
4. Walk the trie along `s[i], s[i+1], ...`; whenever the node at `s[j]` marks a word end, update `dp[i] = min(dp[i], dp[j + 1])`. Stop when the path breaks.
5. Return `dp[0]`.

## Code

```python
from typing import List

class Solution:
	def minExtraChar(self, s: str, dictionary: List[str]) -> int:
		# build trie: nested dicts, "$" marks the end of a word
		root = {}
		for w in dictionary:
			node = root
			for ch in w:
				node = node.setdefault(ch, {})
			node["$"] = True

		n = len(s)
		dp = [0] * (n + 1)              # dp[i] = min extra chars in s[i:]
		for i in range(n - 1, -1, -1):
			dp[i] = 1 + dp[i + 1]       # option 1: s[i] is extra
			node = root
			for j in range(i, n):       # option 2: a word s[i..j]
				node = node.get(s[j])
				if node is None:
					break
				if "$" in node:
					dp[i] = min(dp[i], dp[j + 1])
		return dp[0]
```

## Complexity

- **Time:** `O(n^2 + total dictionary length)` — for each start `i` the trie walk is at most `n` steps.
- **Space:** `O(n + total dictionary length)` — the DP array and the trie.

## Other Approaches

- **DP with a hash set:** for each `i`, try every end `j` and check `s[i:j+1] in words` — Time `O(n^3)` (substring slicing/hashing), Space `O(n + total dictionary length)`.
- **Top-down memoized recursion:** same recurrence written recursively — same complexity as the corresponding bottom-up version.

## Key Takeaway

"Segment a string into dictionary words" → suffix DP; pairing it with a trie lets you enumerate all matching words from a start index in one pass with early termination.
