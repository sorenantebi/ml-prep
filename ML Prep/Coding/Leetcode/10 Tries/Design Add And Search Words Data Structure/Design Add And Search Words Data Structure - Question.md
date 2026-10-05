---
topic: "Tries"
difficulty: Medium
leetcode: https://leetcode.com/problems/design-add-and-search-words-data-structure/
neetcode: https://neetcode.io/problems/design-word-search-data-structure
---
# Design Add And Search Words Data Structure

**Topic:** [[10 Tries|Tries]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/design-add-and-search-words-data-structure/) · [NeetCode](https://neetcode.io/problems/design-word-search-data-structure)

**Solve it in:** [[Design Add And Search Words Data Structure]] · **Answer:** [[Design Add And Search Words Data Structure - Solution]]

## Problem

Design a data structure that stores words and supports searching with wildcards. Implement `WordDictionary`:

- `WordDictionary()` — create an empty structure.
- `addWord(word)` — store `word`.
- `search(word)` — return `True` if some stored word matches `word`, else `False`. The query may contain `'.'` characters, each of which matches **any single** letter. A match must have exactly the same length.

## Examples

**Example 1**
```text
Input:  ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
        [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output: [null,null,null,null,false,true,true,true]
```

**Example 2**
```text
Input:  ["WordDictionary","addWord","search","search"]
        [[],["a"],["."],[".."]]
Output: [null,null,true,false]
```

## Constraints

- `1 <= word.length <= 25`
- Words passed to `addWord` contain only lowercase English letters
- Queries passed to `search` contain lowercase letters or `'.'`
- Each query contains at most `2` dots
- At most `10^4` calls in total

## Starter Code & Test Cases

```python
class WordDictionary:
	def __init__(self):
		pass  # your code here

	def addWord(self, word: str) -> None:
		pass

	def search(self, word: str) -> bool:
		pass


if __name__ == "__main__":
	def run(ops, args):
		obj = None
		out = []
		for op, a in zip(ops, args):
			if op == "WordDictionary":
				obj = WordDictionary()
				out.append(None)
			else:
				out.append(getattr(obj, op)(*a))
		return out

	assert run(
		["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"],
		[[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
	) == [None, None, None, None, False, True, True, True]

	assert run(["WordDictionary", "addWord", "search", "search"], [[], ["a"], ["."], [".."]]) == [None, None, True, False]

	d = WordDictionary()
	assert d.search("a") is False and d.search(".") is False
	d.addWord("at")
	d.addWord("and")
	d.addWord("an")
	d.addWord("add")
	assert d.search("a") is False
	assert d.search(".at") is False
	d.addWord("bat")
	assert d.search(".at") is True
	assert d.search("an.") is True
	assert d.search("a.d.") is False
	assert d.search("b.") is False
	assert d.search("a.d") is True
	assert d.search("..") is True
	assert d.search("...") is True
	assert d.search("....") is False
	print("All tests passed!")
```
