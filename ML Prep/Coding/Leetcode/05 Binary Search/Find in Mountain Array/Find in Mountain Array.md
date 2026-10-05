# Find in Mountain Array

An array `arr` is a **mountain array** if `arr.length >= 3` and there is an index `p` (`0 < p < arr.length - 1`) such that values strictly increase up to `arr[p]` and then strictly decrease after it.

This is an interactive problem: you cannot access the array directly, only through a `MountainArray` object with two methods:

- `MountainArray.get(k)` — returns the element at index `k` (0-indexed),
- `MountainArray.length()` — returns the array's length.

Given a mountain array `mountainArr` and an integer `target`, return the **minimum** index `i` such that `mountainArr.get(i) == target`, or `-1` if `target` does not occur. Solutions that call `get` more than `100` times are rejected.

## Example

```text
Input: mountainArr = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 occurs at indices 2 and 5; return the smaller one
```

```python

```
