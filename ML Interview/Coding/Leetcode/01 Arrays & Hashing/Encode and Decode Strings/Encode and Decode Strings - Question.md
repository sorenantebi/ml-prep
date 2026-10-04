---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/encode-and-decode-strings/
neetcode: https://neetcode.io/problems/string-encode-and-decode
---
# Encode and Decode Strings

**Topic:** [[01 Arrays & Hashing|Arrays & Hashing]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/encode-and-decode-strings/) · [NeetCode](https://neetcode.io/problems/string-encode-and-decode)

**Solve it in:** [[Encode and Decode Strings]] · **Answer:** [[Encode and Decode Strings - Solution]]

## Problem

Design a pair of functions that convert a list of strings into a single string and back again, so the list can be transmitted as one string and reconstructed exactly on the other side. Implement the class `Codec` with:

- `encode(strs)`: takes a list of strings and returns one encoded string.
- `decode(s)`: takes a string produced by `encode` and returns the original list of strings.

The strings may contain any of the 256 ASCII characters (including delimiters you might be tempted to use, such as `#`, `,`, or spaces), may be empty, and the list itself may be empty. Do not rely on language serialization helpers such as `eval` or `pickle`. (This is a LeetCode Premium problem; on NeetCode it is called "String Encode and Decode".)

## Examples

**Example 1**
```text
Input: ["neet","code","love","you"]
Output: ["neet","code","love","you"]
Explanation: decode(encode(strs)) returns the original list.
```

**Example 2**
```text
Input: ["we","say",":","yes","#4#"]
Output: ["we","say",":","yes","#4#"]
```

**Example 3**
```text
Input: ["", ""]
Output: ["", ""]
```

## Constraints

- `0 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` may contain any of the 256 valid ASCII characters.

## Starter Code & Test Cases

```python
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        pass  # your code here

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        pass  # your code here


def roundtrip(strs):
    c = Codec()
    encoded = c.encode(strs)
    assert isinstance(encoded, str)
    return c.decode(encoded)


if __name__ == "__main__":
    cases = [
        ["neet", "code", "love", "you"],
        ["we", "say", ":", "yes", "#4#"],
        ["", ""],
        [],
        [""],
        ["12#ab", "#", "3#", "##"],
        ["line\nbreak", "tab\there", "".join(chr(i) for i in range(256))],
        ["x" * 200] * 200,
    ]
    for strs in cases:
        assert roundtrip(strs) == strs, strs
    print("All tests passed!")
```
