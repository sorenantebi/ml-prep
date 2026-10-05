# Word Ladder

You are given two words `beginWord` and `endWord`, and a dictionary `wordList`. A **transformation sequence** is a list of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every pair of consecutive words differs in exactly one letter.
- Every `si` is in `wordList` (`beginWord` itself does not need to be in the list).
- `sk == endWord`.

Return the **number of words** in the shortest transformation sequence from `beginWord` to `endWord` (counting `beginWord`), or `0` if no such sequence exists.

## Example

```text
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog" has 5 words.
```

```python

```
