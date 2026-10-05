# Minimum Interval to Include Each Query

You are given a 2D array `intervals` where `intervals[i] = [left_i, right_i]` describes the inclusive integer interval from `left_i` to `right_i`; its size is `right_i - left_i + 1`. You are also given an array `queries`. For each `queries[j]`, find the size of the **smallest** interval `i` with `left_i <= queries[j] <= right_i`, or `-1` if no interval contains it. Return an array of answers in the same order as `queries`.

## Example

```text
Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: 2 → [2,4] (size 3); 3 → [2,4] (size 3); 4 → [4,4] (size 1); 5 → [3,6] (size 4).
```

```python

```
