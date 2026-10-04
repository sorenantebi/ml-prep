---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/group-anagrams/
neetcode: https://neetcode.io/problems/anagram-groups
---
# Group Anagrams

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/group-anagrams/) · [NeetCode](https://neetcode.io/problems/anagram-groups)

**Solve it in:** [[Group Anagrams]] · **Answer:** [[Group Anagrams - Solution]]

## Problem

Given an array of strings `strs`, partition the strings into groups such that two strings land in the same group exactly when they are anagrams of each other (same letters with the same multiplicities). Return the list of groups. Both the order of the groups and the order of strings inside each group may be arbitrary.

## Examples

**Example 1**
```text
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2**
```text
Input: strs = [""]
Output: [[""]]
```

**Example 3**
```text
Input: strs = ["abc","bca","xyz"]
Output: [["abc","bca"],["xyz"]]
```

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pass  # your code here


def normalize(groups):
    return sorted(sorted(g) for g in groups)


if __name__ == "__main__":
    s = Solution()
    assert normalize(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == \
        normalize([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert normalize(s.groupAnagrams([""])) == [[""]]
    assert normalize(s.groupAnagrams(["a"])) == [["a"]]
    assert normalize(s.groupAnagrams(["abc", "bca", "xyz"])) == [["abc", "bca"], ["xyz"]]
    assert normalize(s.groupAnagrams(["", "", "b"])) == [["", ""], ["b"]]
    assert normalize(s.groupAnagrams(["ab", "ba", "ab"])) == [["ab", "ab", "ba"]]
    assert normalize(s.groupAnagrams(["aab", "abb"])) == [["aab"], ["abb"]]
    print("All tests passed!")
```
