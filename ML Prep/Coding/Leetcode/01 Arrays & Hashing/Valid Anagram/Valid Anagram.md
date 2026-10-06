# Valid Anagram

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, otherwise return `false`. Two strings are anagrams when one can be produced by rearranging the characters of the other, using every character exactly as many times as it appears (so both strings must have identical character counts).

## Example

```text
Input: s = "listen", t = "silent"
Output: true
```

```python
from collections import Counter
return Counter(s) == Counter(t)

# or use bins where you do count[ord(char) - ord('a')] += 1
# char = some number 'a' = 65, so if 'a' --> 65 - 65 = 0
# 'b' - 'a' = 1 etc
```
