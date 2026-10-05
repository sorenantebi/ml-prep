# Open The Lock

A lock has 4 circular wheels, each showing a digit `'0'`–`'9'`. A move turns exactly one wheel by one slot, either up or down; the wheels wrap around (`'9'` → `'0'` and `'0'` → `'9'`). The lock starts at `"0000"`.

You are given a list `deadends`: if the lock ever shows one of these combinations, it jams and can no longer be turned. You are also given a `target` combination.

Return the minimum number of moves needed to reach `target` from `"0000"` without ever passing through a dead end, or `-1` if it is impossible.

## Example

```text
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: e.g. "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
```

```python

```
