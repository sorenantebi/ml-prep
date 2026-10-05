---
topic: "Binary Search"
difficulty: Medium
leetcode: https://leetcode.com/problems/time-based-key-value-store/
neetcode: https://neetcode.io/problems/time-based-key-value-store
---
# Time Based Key Value Store - Solution

**Question:** [[Time Based Key Value Store - Question]] · **Difficulty:** Medium

## Intuition

Because `set` timestamps arrive in increasing order, each key's list of `(timestamp, value)` pairs is already sorted. A `get` asks for the last entry with timestamp `<= t`, which is a classic upper-bound binary search on that list.

## Approach

1. Keep a dict `key -> list of (timestamp, value)`; `set` simply appends.
2. `get(key, t)`: binary search the key's list for the rightmost timestamp `<= t`.
3. Track the best candidate while searching: when `times[mid] <= t`, record it and move right; otherwise move left.
4. Return the recorded value, or `""` if none was found.

## Code

```python
from collections import defaultdict


class TimeMap:
	def __init__(self):
		self.store = defaultdict(list)  # key -> [(timestamp, value)], sorted by time

	def set(self, key: str, value: str, timestamp: int) -> None:
		self.store[key].append((timestamp, value))

	def get(self, key: str, timestamp: int) -> str:
		entries = self.store.get(key, [])
		lo, hi, res = 0, len(entries) - 1, ""
		while lo <= hi:
			mid = (lo + hi) // 2
			if entries[mid][0] <= timestamp:
				res = entries[mid][1]   # valid candidate, look for a later one
				lo = mid + 1
			else:
				hi = mid - 1
		return res
```

## Complexity

- **Time:** `O(1)` for `set`, `O(log k)` for `get` where `k` is the number of entries for that key.
- **Space:** `O(n)` — all stored entries.

## Other Approaches

- **Linear scan backwards on `get`:** walk the key's list from the end until a timestamp `<= t` — `get` is `O(k)`, Space `O(n)`.
- **`bisect.bisect_right`:** keep a parallel list of timestamps and use `bisect_right(times, t) - 1` — same `O(log k)`, less code.

## Key Takeaway

Append-only, time-ordered data is naturally sorted — answer "latest value at or before t" with an upper-bound binary search.
