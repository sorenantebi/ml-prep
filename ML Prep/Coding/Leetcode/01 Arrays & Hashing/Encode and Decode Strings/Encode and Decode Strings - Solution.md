---
topic: "Arrays & Hashing"
difficulty: Medium
leetcode: https://leetcode.com/problems/encode-and-decode-strings/
neetcode: https://neetcode.io/problems/string-encode-and-decode
---
# Encode and Decode Strings - Solution

**Question:** [[Encode and Decode Strings - Question]] · **Difficulty:** Medium

## Intuition

Any delimiter character could also appear inside a string, so we cannot just join on a separator. Instead, prefix each string with its length and a marker, e.g. `"5#hello"`. When decoding we read the digits up to the first `#`, then take exactly that many characters, so the content is never interpreted, no matter what it contains.

## Approach

1. **Encode:** for each string `w`, append `f"{len(w)}#{w}"`; join everything together.
2. **Decode:** start at `i = 0`. Scan forward from `i` to the next `#` at `j`; `length = int(s[i:j])`.
3. The string is `s[j + 1 : j + 1 + length]`; append it and set `i = j + 1 + length`.
4. Repeat until `i` reaches the end of `s`.

## Code

```python
from typing import List


class Codec:
	def encode(self, strs: List[str]) -> str:
		return "".join(f"{len(w)}#{w}" for w in strs)

	def decode(self, s: str) -> List[str]:
		result, i = [], 0
		while i < len(s):
			j = i
			while s[j] != "#":  # length digits never contain '#'
				j += 1
			length = int(s[i:j])
			start = j + 1
			result.append(s[start:start + length])  # read exactly `length` chars, content is opaque
			i = start + length
		return result
```

## Complexity

- **Time:** `O(N)` — `N` is the total number of characters across all strings; each is written and read a constant number of times.
- **Space:** `O(N)` — for the encoded string and decoded output (no extra beyond the outputs).

## Other Approaches

- **Escaping a delimiter:** double every `#` inside strings and separate items with `" # "`-style tokens — Time `O(N)`, Space `O(N)`, but fiddlier to get right.
- **Fixed-width length header:** write each length as a 4-byte / fixed-width field instead of `len#` — Time `O(N)`, Space `O(N)`.

## Key Takeaway

Length-prefix framing (`len#payload`) is the robust way to serialize arbitrary strings; it is exactly how many network protocols (and chunked encodings) frame messages.
