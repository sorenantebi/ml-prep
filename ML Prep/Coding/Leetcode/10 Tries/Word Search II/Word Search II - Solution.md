---
topic: "Tries"
difficulty: Hard
leetcode: https://leetcode.com/problems/word-search-ii/
neetcode: https://neetcode.io/problems/search-for-word-ii
---
# Word Search II - Solution

**Question:** [[Word Search II - Question]] · **Difficulty:** Hard

## Intuition

Running a separate Word Search for each word repeats the same board exploration over and over. Instead, put all words in a trie and run one backtracking DFS from every cell, walking the trie in lockstep with the board path. A path is abandoned as soon as it is not a prefix of any word, and each trie node that ends a word stores that word so it can be reported directly.

## Approach

1. Build a trie; at the node where a word ends, store `node["$"] = word`.
2. For each cell, start `dfs(r, c, parent_node)` if the cell's letter is a child of the root.
3. In `dfs`: move to the child node for `board[r][c]`. If it contains `"$"`, add the word to the result and delete the marker (avoids duplicates).
4. Mark the cell as visited (temporarily set it to `"#"`), recurse into the 4 neighbours whose letters are children of the current node, then restore the cell.
5. Pruning: if the child node becomes empty after exploring, remove it from its parent so exhausted branches are never re-explored.

## Code

```python
from typing import List

class Solution:
	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
		root = {}
		for w in words:
			node = root
			for ch in w:
				node = node.setdefault(ch, {})
			node["$"] = w                         # store the full word at its end node

		rows, cols = len(board), len(board[0])
		res = []

		def dfs(r: int, c: int, parent: dict) -> None:
			ch = board[r][c]
			node = parent[ch]
			word = node.pop("$", None)
			if word:                              # found; pop prevents duplicates
				res.append(word)

			board[r][c] = "#"                     # mark visited
			for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
				nr, nc = r + dr, c + dc
				if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in node:
					dfs(nr, nc, node)
			board[r][c] = ch                      # restore

			if not node:                          # prune exhausted trie branches
				parent.pop(ch)

		for r in range(rows):
			for c in range(cols):
				if board[r][c] in root:
					dfs(r, c, root)
		return res
```

## Complexity

- **Time:** `O(m · n · 3^(L-1))` worst case, where `L` is the max word length (4 directions at the first step, then at most 3 since we can't go back) — plus `O(total word length)` to build the trie. Pruning makes it much faster in practice.
- **Space:** `O(total word length)` for the trie; `O(L)` recursion stack.

## Other Approaches

- **Word Search per word:** run a backtracking search for each word separately — Time `O(W · m · n · 3^L)`, Space `O(L)`; too slow for `3 * 10^4` words.

## Key Takeaway

When searching for many words at once, build a trie and walk it during the DFS; store the word at its terminal node and prune emptied branches to avoid redundant work.
