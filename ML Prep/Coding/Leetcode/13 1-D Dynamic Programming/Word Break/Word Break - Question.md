---
topic: "1-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/word-break/
neetcode: https://neetcode.io/problems/word-break
---
# Word Break

**Topic:** [[13 1-D Dynamic Programming|1-D Dynamic Programming]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/word-break/) · [NeetCode](https://neetcode.io/problems/word-break)

**Solve it in:** [[Word Break]] · **Answer:** [[Word Break - Solution]]

## Problem

Given a string `s` and a list of strings `wordDict`, return `true` if `s` can be split into a sequence of one or more dictionary words (concatenated with no gaps), and `false` otherwise. A dictionary word may be used any number of times.

## Examples

**Example 1**
```text
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
```

**Example 2**
```text
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: "apple" is reused.
```

**Example 3**
```text
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

## Constraints

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and the words contain only lowercase English letters; all words are unique.

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		pass  # your code here


if __name__ == "__main__":
	sol = Solution()
	assert sol.wordBreak("leetcode", ["leet","code"]) is True
	assert sol.wordBreak("applepenapple", ["apple","pen"]) is True
	assert sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]) is False
	assert sol.wordBreak("a", ["b"]) is False
	assert sol.wordBreak("aaaaaaa", ["aaaa","aaa"]) is True
	assert sol.wordBreak("cars", ["car","ca","rs"]) is True
	assert sol.wordBreak("a" * 150 + "b", ["a","aa","aaa"]) is False
	print("All tests passed!")
```
