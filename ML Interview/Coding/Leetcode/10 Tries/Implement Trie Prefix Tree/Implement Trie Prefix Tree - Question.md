---
topic: "Tries"
difficulty: Medium
leetcode: https://leetcode.com/problems/implement-trie-prefix-tree/
neetcode: https://neetcode.io/problems/implement-prefix-tree
---
# Implement Trie Prefix Tree

**Topic:** [[10 Tries|Tries]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/) · [NeetCode](https://neetcode.io/problems/implement-prefix-tree)

**Solve it in:** [[Implement Trie Prefix Tree]] · **Answer:** [[Implement Trie Prefix Tree - Solution]]

## Problem

A trie (prefix tree) stores a set of strings so that words and prefixes can be looked up efficiently. Implement the class `Trie`:

- `Trie()` — create an empty trie.
- `insert(word)` — add `word` to the trie.
- `search(word)` — return `True` if `word` was previously inserted (as a complete word), else `False`.
- `startsWith(prefix)` — return `True` if any previously inserted word begins with `prefix`, else `False`.

## Examples

**Example 1**
```text
Input:  ["Trie","insert","search","search","startsWith","insert","search"]
        [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
Output: [null,null,true,false,true,null,true]
```

**Example 2**
```text
Input:  ["Trie","insert","startsWith","search"]
        [[],["a"],["b"],["a"]]
Output: [null,null,false,true]
```

## Constraints

- `1 <= word.length, prefix.length <= 2000`
- `word` and `prefix` consist only of lowercase English letters
- At most `3 * 10^4` calls in total

## Starter Code & Test Cases

```python
class Trie:
    def __init__(self):
        pass  # your code here

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass


if __name__ == "__main__":
    def run(ops, args):
        obj = None
        out = []
        for op, a in zip(ops, args):
            if op == "Trie":
                obj = Trie()
                out.append(None)
            else:
                out.append(getattr(obj, op)(*a))
        return out

    assert run(
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
    ) == [None, None, True, False, True, None, True]

    assert run(["Trie", "insert", "startsWith", "search"], [[], ["a"], ["b"], ["a"]]) == [None, None, False, True]

    t = Trie()
    assert t.search("x") is False and t.startsWith("x") is False
    t.insert("car")
    t.insert("card")
    t.insert("care")
    assert t.search("car") and t.search("card") and t.search("care")
    assert not t.search("ca") and not t.search("cards")
    assert t.startsWith("ca") and t.startsWith("card") and not t.startsWith("cb")
    t.insert("car")  # duplicate insert is harmless
    assert t.search("car")
    long_word = "z" * 2000
    t.insert(long_word)
    assert t.search(long_word) and t.startsWith("z" * 1999) and not t.search("z" * 1999)
    print("All tests passed!")
```
