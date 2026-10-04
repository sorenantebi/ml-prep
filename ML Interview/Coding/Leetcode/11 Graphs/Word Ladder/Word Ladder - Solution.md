---
topic: "Graphs"
difficulty: Hard
leetcode: https://leetcode.com/problems/word-ladder/
neetcode: https://neetcode.io/problems/word-ladder
---
# Word Ladder - Solution

**Question:** [[Word Ladder - Question]] · **Difficulty:** Hard

## Intuition

Words are nodes; two words are connected if they differ by exactly one letter. The shortest transformation sequence is a shortest path in an unweighted graph, so use **BFS**. Rather than comparing every pair of words, generate neighbors by trying all 26 letters at each position and keeping only candidates that are in the (unvisited) dictionary.

## Approach

1. Put `wordList` in a set; if `endWord` is missing, return `0`.
2. BFS from `beginWord` with level counter starting at 1.
3. For each word in the current level, for each position and each letter `a`–`z`, form a candidate; if it is `endWord`, return `level + 1`; if it is in the remaining word set, remove it (mark visited) and enqueue it.
4. If BFS ends, return `0`.

## Code

```python
from collections import deque
from string import ascii_lowercase
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        q = deque([beginWord])
        words.discard(beginWord)
        length = 1
        while q:
            for _ in range(len(q)):  # process one BFS level
                word = q.popleft()
                for i in range(len(word)):
                    for ch in ascii_lowercase:
                        cand = word[:i] + ch + word[i + 1:]
                        if cand == endWord:
                            return length + 1
                        if cand in words:
                            words.remove(cand)  # removing from the set == marking visited
                            q.append(cand)
            length += 1
        return 0
```

## Complexity

- **Time:** `O(N * L^2 * 26)` — `N` words, each visited once; `L * 26` candidates per word, each costing `O(L)` to build and hash.
- **Space:** `O(N * L)` — the word set and BFS queue.

## Other Approaches

- **Wildcard pattern buckets:** map patterns like `h*t` to the words matching them and BFS through buckets — Time `O(N * L^2)`, Space `O(N * L^2)`.
- **Bidirectional BFS:** expand from both ends, always growing the smaller frontier — same worst case, much faster in practice.

## Key Takeaway

Shortest number of single-step edits = BFS over an implicit graph; generate neighbors on the fly and delete visited words from the dictionary set.
