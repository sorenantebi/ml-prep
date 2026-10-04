---
topic: "Tries"
difficulty: Medium
leetcode: https://leetcode.com/problems/extra-characters-in-a-string/
neetcode: https://neetcode.io/problems/extra-characters-in-a-string
---
# Extra Characters in a String

**Topic:** [[10 Tries|Tries]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/extra-characters-in-a-string/) · [NeetCode](https://neetcode.io/problems/extra-characters-in-a-string)

**Solve it in:** [[Extra Characters in a String]] · **Answer:** [[Extra Characters in a String - Solution]]

## Problem

You are given a 0-indexed string `s` and a list of distinct words `dictionary`. Split `s` into one or more **non-overlapping** substrings so that each chosen substring is a word in `dictionary`; characters of `s` that are not covered by any chosen substring are called *extra*. Return the minimum possible number of extra characters.

## Examples

**Example 1**
```text
Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: use "leet" (0..3) and "code" (5..8); only 's' at index 4 is extra.
```

**Example 2**
```text
Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: "hello" and "world" cover indices 3..12; "say" is left over.
```

## Constraints

- `1 <= s.length <= 50`
- `1 <= dictionary.length <= 50`
- `1 <= dictionary[i].length <= 50`
- `s` and `dictionary[i]` contain only lowercase English letters
- `dictionary` contains distinct words

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        pass  # your code here


if __name__ == "__main__":
    sol = Solution()
    assert sol.minExtraChar("leetscode", ["leet", "code", "leetcode"]) == 1
    assert sol.minExtraChar("sayhelloworld", ["hello", "world"]) == 3
    assert sol.minExtraChar("abc", ["abc"]) == 0
    assert sol.minExtraChar("abc", ["d"]) == 3
    assert sol.minExtraChar("a", ["a"]) == 0
    assert sol.minExtraChar("aaaa", ["aa", "aaa"]) == 0
    assert sol.minExtraChar("dwmodizxvvbosxxw", ["ox", "lb", "diz", "gu", "v", "ksv", "o", "nuq", "r", "txhe", "e", "wmo", "cehy", "tskz", "ds", "kzbu"]) == 7
    assert sol.minExtraChar("x" * 50, ["x" * 50, "y"]) == 0
    print("All tests passed!")
```
