---
topic: "2-D Dynamic Programming"
difficulty: Medium
leetcode: https://leetcode.com/problems/edit-distance/
neetcode: https://neetcode.io/problems/edit-distance
---
# Edit Distance - Solution

**Question:** [[Edit Distance - Question]] · **Difficulty:** Medium

## Intuition

Let `dp[i][j]` be the edit distance between `word1[:i]` and `word2[:j]`. If the last characters match, no operation is needed: `dp[i-1][j-1]`. Otherwise take `1 +` the best of delete (`dp[i-1][j]`), insert (`dp[i][j-1]`), or replace (`dp[i-1][j-1]`). Base cases: converting to/from an empty string costs its length.

## Approach

1. `prev = list(range(n + 1))` is row `i = 0` (insert `j` characters).
2. For each `i` from 1 to `m`, build `cur` with `cur[0] = i` (delete `i` characters), then fill `cur[j]` with the recurrence using `prev[j-1]`, `prev[j]`, `cur[j-1]`.
3. After all rows, return `prev[n]`.

## Code

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev = list(range(n + 1))  # "" -> word2[:j] needs j inserts
        for i in range(1, m + 1):
            cur = [i] + [0] * n     # word1[:i] -> "" needs i deletes
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = 1 + min(prev[j],      # delete word1[i-1]
                                     cur[j - 1],   # insert word2[j-1]
                                     prev[j - 1])  # replace
            prev = cur
        return prev[n]
```

## Complexity

- **Time:** `O(m * n)` — each prefix pair evaluated once.
- **Space:** `O(n)` — two rows.

## Other Approaches

- **Full 2-D table:** same recurrence; allows backtracking the actual edit script — Time `O(mn)`, Space `O(mn)`.
- **Memoized recursion on `(i, j)`:** top-down version — Time `O(mn)`, Space `O(mn)` plus recursion stack.

## Key Takeaway

Edit distance is the template for two-string alignment DPs: match -> diagonal, mismatch -> 1 + min(up, left, diagonal).
