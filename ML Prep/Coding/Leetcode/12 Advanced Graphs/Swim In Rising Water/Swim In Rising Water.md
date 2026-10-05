# Swim In Rising Water

You are given an `n x n` grid where `grid[r][c]` is the elevation of cell `(r, c)`; the values are a permutation of `0 .. n^2 - 1`. Rain starts falling, and at time `t` the water level everywhere is `t`.

You may swim from a cell to a 4-directionally adjacent cell only if both cells have elevation at most `t`. Swimming any distance takes zero time. Starting at `(0, 0)`, return the smallest time `t` at which you can reach `(n - 1, n - 1)`.

## Example

```text
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation: The target cell itself has elevation 3, so you must wait until t = 3.
```

```python

```
