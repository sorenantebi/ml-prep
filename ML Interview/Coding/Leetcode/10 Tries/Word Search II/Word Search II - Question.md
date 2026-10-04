---
topic: "Tries"
difficulty: Hard
leetcode: https://leetcode.com/problems/word-search-ii/
neetcode: https://neetcode.io/problems/search-for-word-ii
---
# Word Search II

**Topic:** [[10 Tries|Tries]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/word-search-ii/) · [NeetCode](https://neetcode.io/problems/search-for-word-ii)

**Solve it in:** [[Word Search II]] · **Answer:** [[Word Search II - Solution]]

## Problem

You are given an `m x n` grid `board` of lowercase letters and a list of distinct strings `words`. Return every word from `words` that can be spelled on the board by a path of sequentially adjacent cells (adjacent = sharing an edge horizontally or vertically), where no cell is used more than once within the same word. The result may be returned in any order.

## Examples

**Example 1**
```text
Input: board = [["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","v"]],
       words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

**Example 2**
```text
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

## Constraints

- `1 <= m, n <= 12`
- `board[i][j]` is a lowercase English letter
- `1 <= words.length <= 3 * 10^4`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase letters; all words are distinct

## Starter Code & Test Cases

```python
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()

    def run(board, words):
        return sorted(s.findWords([row[:] for row in board], words))

    board1 = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    assert run(board1, ["oath", "pea", "eat", "rain"]) == ["eat", "oath"]
    assert run([["a", "b"], ["c", "d"]], ["abcb"]) == []
    assert run([["a"]], ["a", "b", "aa"]) == ["a"]
    assert run([["a", "b"], ["c", "d"]], ["ab", "abdc", "acdb", "ad", "ba", "dcab"]) == ["ab", "abdc", "acdb", "ba", "dcab"]
    assert run([["a", "a"]], ["aaa", "aa"]) == ["aa"]   # a cell may not be reused
    assert run(board1, ["oa", "oaa", "oat", "oath", "oathk"]) == ["oa", "oaa", "oat", "oath", "oathk"]
    assert run([["x"] * 4 for _ in range(4)], ["x" * 16, "x" * 17]) == ["x" * 16]
    print("All tests passed!")
```
