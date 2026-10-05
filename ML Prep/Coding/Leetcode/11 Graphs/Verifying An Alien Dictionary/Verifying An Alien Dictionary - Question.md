---
topic: "Graphs"
difficulty: Easy
leetcode: https://leetcode.com/problems/verifying-an-alien-dictionary/
neetcode: https://neetcode.io/problems/verifying-an-alien-dictionary
---
# Verifying An Alien Dictionary

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/verifying-an-alien-dictionary/) · [NeetCode](https://neetcode.io/problems/verifying-an-alien-dictionary)

**Solve it in:** [[Verifying An Alien Dictionary]] · **Answer:** [[Verifying An Alien Dictionary - Solution]]

## Problem

An alien language uses the same 26 lowercase English letters, but in a different alphabetical order. You are given `order`, a permutation of the 26 letters describing that alphabet, and a list `words` written in the alien language.

Return `true` if `words` is sorted lexicographically according to the alien alphabet, and `false` otherwise. Lexicographic order works as usual: compare at the first differing character; if one word is a prefix of the other, the shorter word must come first.

## Examples

**Example 1**
```text
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: 'h' comes before 'l' in this alphabet.
```

**Example 2**
```text
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: At index 3, 'd' comes after 'l', so "word" > "world".
```

**Example 3**
```text
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: "app" is a prefix of "apple", so it must come first.
```

## Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 20`
- `order.length == 26`
- All characters are lowercase English letters; `order` contains each letter exactly once

## Starter Code & Test Cases

```python
from typing import List


class Solution:
	def isAlienSorted(self, words: List[str], order: str) -> bool:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz") is True
	assert s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz") is False
	assert s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz") is False
	assert s.isAlienSorted(["app","apple"], "abcdefghijklmnopqrstuvwxyz") is True
	assert s.isAlienSorted(["single"], "zyxwvutsrqponmlkjihgfedcba") is True
	assert s.isAlienSorted(["cba","abc"], "zyxwvutsrqponmlkjihgfedcba") is True
	assert s.isAlienSorted(["abc","abc","abd"], "abcdefghijklmnopqrstuvwxyz") is True
	assert s.isAlienSorted(["kuvp","q"], "ngxlkthsjuoqcpavbfdermiywz") is True
	print("All tests passed!")
```
