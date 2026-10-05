# Greatest Common Divisor Traversal

You are given a 0-indexed integer array `nums`. You may move directly between indices `i` and `j` (`i != j`) if and only if `gcd(nums[i], nums[j]) > 1`.

Return `true` if, for **every** pair of indices `i < j`, there is some sequence of moves that gets from `i` to `j`; otherwise return `false`.

## Example

```text
Input: nums = [2,3,6]
Output: true
Explanation: 0 <-> 2 (gcd 2) and 1 <-> 2 (gcd 3), so all indices are connected.
```

```python

```
