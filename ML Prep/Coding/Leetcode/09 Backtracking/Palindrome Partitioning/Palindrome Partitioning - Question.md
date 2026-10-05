---
topic: "Backtracking"
difficulty: Medium
leetcode: https://leetcode.com/problems/palindrome-partitioning/
neetcode: https://neetcode.io/problems/palindrome-partitioning
---
# Palindrome Partitioning

**Topic:** [[09 Backtracking|Backtracking]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/palindrome-partitioning/) · [NeetCode](https://neetcode.io/problems/palindrome-partitioning)

**Solve it in:** [[Palindrome Partitioning]] · **Answer:** [[Palindrome Partitioning - Solution]]

## Problem

Given a string `s`, split it into one or more contiguous pieces such that **every piece is a palindrome** (reads the same forwards and backwards). Return all possible ways to do this; each way is a list of the pieces in order. The ways can be returned in any order.

## Examples

**Example 1**
```text
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

**Example 2**
```text
Input: s = "a"
Output: [["a"]]
```

## Constraints

- `1 <= s.length <= 16`
- `s` consists of lowercase English letters

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def partition(self, s: str) -> List[List[str]]:
		pass  # your code here


def brute(s):
	if not s:
		return [[]]
	out = []
	for i in range(1, len(s) + 1):
		if s[:i] == s[:i][::-1]:
			out += [[s[:i]] + rest for rest in brute(s[i:])]
	return out


if __name__ == "__main__":
	sol = Solution()
	assert sorted(sol.partition("aab")) == sorted([["a", "a", "b"], ["aa", "b"]])
	assert sol.partition("a") == [["a"]]
	assert sorted(sol.partition("ab")) == [["a", "b"]]
	assert sorted(sol.partition("aba")) == sorted([["a", "b", "a"], ["aba"]])
	assert sorted(sol.partition("efe")) == sorted([["e", "f", "e"], ["efe"]])
	for s in ["abbab", "racecar", "aaaa", "cdd"]:
		assert sorted(sol.partition(s)) == sorted(brute(s))
	assert len(sol.partition("a" * 16)) == 2 ** 15
	print("All tests passed!")
```
