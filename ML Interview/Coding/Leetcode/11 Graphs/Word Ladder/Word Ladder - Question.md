---
topic: "Graphs"
difficulty: Hard
leetcode: https://leetcode.com/problems/word-ladder/
neetcode: https://neetcode.io/problems/word-ladder
---
# Word Ladder

**Topic:** [[11 Graphs|Graphs]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/word-ladder/) · [NeetCode](https://neetcode.io/problems/word-ladder)

**Solve it in:** [[Word Ladder]] · **Answer:** [[Word Ladder - Solution]]

## Problem

You are given two words `beginWord` and `endWord`, and a dictionary `wordList`. A **transformation sequence** is a list of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every pair of consecutive words differs in exactly one letter.
- Every `si` is in `wordList` (`beginWord` itself does not need to be in the list).
- `sk == endWord`.

Return the **number of words** in the shortest transformation sequence from `beginWord` to `endWord` (counting `beginWord`), or `0` if no such sequence exists.

## Examples

**Example 1**
```text
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog" has 5 words.
```

**Example 2**
```text
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: "cog" is not in the word list.
```

## Constraints

- `1 <= beginWord.length <= 10`
- `endWord.length == beginWord.length`, all words in `wordList` have this length
- `1 <= wordList.length <= 5000`
- All words consist of lowercase English letters
- `beginWord != endWord`; words in `wordList` are unique

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
    assert s.ladderLength("a", "c", ["a","b","c"]) == 2
    assert s.ladderLength("hot", "dog", ["hot","dog"]) == 0  # differ in 2 letters, no bridge
    assert s.ladderLength("hot", "dog", ["hot","dot","dog"]) == 3
    assert s.ladderLength("abc", "abd", ["abd"]) == 2
    assert s.ladderLength("aaa", "ccc", ["aab","abb","bbb","bbc","bcc","ccc","aac","acc"]) == 4
    print("All tests passed!")
```
