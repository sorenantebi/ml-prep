---
topic: "Sliding Window"
difficulty: Hard
leetcode: https://leetcode.com/problems/minimum-window-substring/
neetcode: https://neetcode.io/problems/minimum-window-with-characters
---
# Minimum Window Substring

**Topic:** [[03 Sliding Window|Sliding Window]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/minimum-window-substring/) · [NeetCode](https://neetcode.io/problems/minimum-window-with-characters)

**Solve it in:** [[Minimum Window Substring]] · **Answer:** [[Minimum Window Substring - Solution]]

## Problem

Given strings `s` and `t`, return the shortest contiguous substring of `s` that contains every character of `t` **including multiplicity** (if `t` has two `'a'`s, the window needs at least two `'a'`s). If no such window exists, return the empty string `""`. The test data guarantees the minimum window is unique.

## Examples

**Example 1**
```text
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

**Example 2**
```text
Input: s = "a", t = "a"
Output: "a"
```

**Example 3**
```text
Input: s = "a", t = "aa"
Output: ""
Explanation: s has only one 'a'
```

## Constraints

- `1 <= s.length, t.length <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters
- Aim for `O(m + n)` time

## Starter Code & Test Cases

```python
class Solution:
	def minWindow(self, s: str, t: str) -> str:
		pass  # your code here


if __name__ == "__main__":
	sol = Solution()
	assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
	assert sol.minWindow("a", "a") == "a"
	assert sol.minWindow("a", "aa") == ""
	assert sol.minWindow("ab", "b") == "b"
	assert sol.minWindow("abc", "d") == ""
	assert sol.minWindow("aaflslflsldkalskaaa", "aaa") == "aaa"
	assert sol.minWindow("bba", "ab") == "ba"
	assert sol.minWindow("aAbB", "AB") == "AbB"
	print("All tests passed!")
```
