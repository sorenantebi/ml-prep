---
topic: "Backtracking"
difficulty: Hard
leetcode: https://leetcode.com/problems/word-break-ii/
neetcode: https://neetcode.io/problems/word-break-ii
---
# Word Break II

**Topic:** [[09 Backtracking|Backtracking]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/word-break-ii/) · [NeetCode](https://neetcode.io/problems/word-break-ii)

**Solve it in:** [[Word Break II]] · **Answer:** [[Word Break II - Solution]]

## Problem

Given a string `s` and a list of words `wordDict`, insert spaces into `s` so that every resulting piece is a word from the dictionary. Return **all** sentences that can be formed this way, in any order.

Dictionary words may be used multiple times. If no segmentation exists, return an empty list.

## Examples

**Example 1**
```text
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
```

**Example 2**
```text
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
```

**Example 3**
```text
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
```

## Constraints

- `1 <= s.length <= 20`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 10`
- `s` and `wordDict[i]` are lowercase English letters; dictionary words are unique
- The number of answers is at most `10^5`

## Starter Code & Test Cases

```python
from typing import List
from functools import lru_cache


class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
		pass  # your code here


if __name__ == "__main__":
	sol = Solution()
	assert sorted(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])) == sorted(["cats and dog", "cat sand dog"])
	assert sorted(sol.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])) == sorted(
		["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
	)
	assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == []
	assert sol.wordBreak("a", ["a"]) == ["a"]
	assert sol.wordBreak("a", ["b"]) == []
	assert sorted(sol.wordBreak("aaa", ["a", "aa"])) == sorted(["a a a", "a aa", "aa a"])
	res = sol.wordBreak("a" * 20, ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"])
	assert len(res) == len(set(res)) == 521472
	assert sol.wordBreak("aaaaaaaaaaaaaaaaaab", ["a", "aa", "aaa", "aaaa"]) == []
	print("All tests passed!")
```
