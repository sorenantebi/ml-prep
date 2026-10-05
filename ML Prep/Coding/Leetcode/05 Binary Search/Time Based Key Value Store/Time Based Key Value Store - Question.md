---
topic: "Binary Search"
difficulty: Medium
leetcode: https://leetcode.com/problems/time-based-key-value-store/
neetcode: https://neetcode.io/problems/time-based-key-value-store
---
# Time Based Key Value Store

**Topic:** [[05 Binary Search|Binary Search]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/time-based-key-value-store/) · [NeetCode](https://neetcode.io/problems/time-based-key-value-store)

**Solve it in:** [[Time Based Key Value Store]] · **Answer:** [[Time Based Key Value Store - Solution]]

## Problem

Design a time-based key-value store that can keep several values for the same key at different timestamps and retrieve the value that was current at a given time. Implement the class `TimeMap`:

- `TimeMap()` — initializes the store.
- `set(key, value, timestamp)` — stores `value` for `key` at time `timestamp`.
- `get(key, timestamp)` — returns the value from the call `set(key, value, t)` with the largest `t <= timestamp`. If there is no such entry, return the empty string `""`.

All timestamps passed to `set` are strictly increasing across calls.

## Examples

**Example 1**
```text
Input:  ["TimeMap","set","get","get","set","get","get"]
        [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation: get("foo",3) has no entry at 3, so it returns the value at time 1
```

**Example 2**
```text
Input:  ["TimeMap","set","get"]
        [[],["k","v",10],["k",5]]
Output: [null,null,""]
Explanation: nothing was stored for "k" at or before time 5
```

## Constraints

- `1 <= key.length, value.length <= 100`
- `key` and `value` consist of lowercase English letters and digits
- `1 <= timestamp <= 10^7`
- Timestamps of `set` calls are strictly increasing
- At most `2 * 10^5` calls to `set` and `get`

## Starter Code & Test Cases

```python
class TimeMap:
	def __init__(self):
		pass  # your code here

	def set(self, key: str, value: str, timestamp: int) -> None:
		pass

	def get(self, key: str, timestamp: int) -> str:
		pass


if __name__ == "__main__":
	tm = TimeMap()
	tm.set("foo", "bar", 1)
	assert tm.get("foo", 1) == "bar"
	assert tm.get("foo", 3) == "bar"
	tm.set("foo", "bar2", 4)
	assert tm.get("foo", 4) == "bar2"
	assert tm.get("foo", 5) == "bar2"
	assert tm.get("foo", 3) == "bar"

	tm2 = TimeMap()
	tm2.set("k", "v", 10)
	assert tm2.get("k", 5) == ""
	assert tm2.get("missing", 100) == ""

	tm3 = TimeMap()
	tm3.set("a", "x1", 1)
	tm3.set("b", "y2", 2)
	tm3.set("a", "x3", 3)
	tm3.set("a", "x7", 7)
	assert [tm3.get("a", t) for t in range(0, 9)] == ["", "x1", "x1", "x3", "x3", "x3", "x3", "x7", "x7"]
	assert tm3.get("b", 1) == ""
	assert tm3.get("b", 10**7) == "y2"
	print("All tests passed!")
```
