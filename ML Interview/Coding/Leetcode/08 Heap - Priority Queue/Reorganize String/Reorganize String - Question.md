---
topic: "Heap / Priority Queue"
difficulty: Medium
leetcode: https://leetcode.com/problems/reorganize-string/
neetcode: https://neetcode.io/problems/reorganize-string
---
# Reorganize String

**Topic:** [[08 Heap - Priority Queue|Heap / Priority Queue]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/reorganize-string/) · [NeetCode](https://neetcode.io/problems/reorganize-string)

**Solve it in:** [[Reorganize String]] · **Answer:** [[Reorganize String - Solution]]

## Problem

Given a string `s`, rearrange its characters so that no two neighboring characters are the same. Return any such rearrangement, or the empty string `""` if no valid arrangement exists.

## Examples

**Example 1**
```text
Input: s = "aab"
Output: "aba"
```

**Example 2**
```text
Input: s = "aaab"
Output: ""
Explanation: three 'a's cannot be separated by a single 'b'
```

**Example 3**
```text
Input: s = "aabbcc"
Output: "abcabc"
Explanation: any valid answer such as "abacbc" is accepted
```

## Constraints

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters

## Starter Code & Test Cases

```python
from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        pass  # your code here


def is_valid(src: str, out: str) -> bool:
    return Counter(src) == Counter(out) and all(out[i] != out[i + 1] for i in range(len(out) - 1))


if __name__ == "__main__":
    sol = Solution()
    for s in ["aab", "aabbcc", "a", "ab", "vvvlo", "aaabbbccc", "abbabbaaab", "zzzzyyyxx" * 10]:
        res = sol.reorganizeString(s)
        assert is_valid(s, res), (s, res)
    assert sol.reorganizeString("aaab") == ""
    assert sol.reorganizeString("aa") == ""
    assert sol.reorganizeString("aaaaabbbb" + "a") == ""
    print("All tests passed!")
```
