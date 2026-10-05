# Alien Dictionary

An alien language uses a subset of lowercase English letters, but in an unknown order. You are given a list of `words` that is claimed to be sorted lexicographically according to the alien alphabet.

Return a string containing every unique letter that appears in `words`, arranged in an order consistent with the sorting. If the given ordering is impossible (contradictory), return `""`. If multiple orders are valid, return any of them.

Notes on lexicographic order: the first position where two words differ decides their order; if one word is a prefix of the other, the shorter word must come first (so `["abc", "ab"]` is invalid).

(LeetCode 269 is a premium problem; NeetCode hosts it as "Foreign Dictionary".)

## Example

```text
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
```

```python

```
