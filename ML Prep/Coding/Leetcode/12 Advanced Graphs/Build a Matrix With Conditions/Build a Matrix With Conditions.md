# Build a Matrix With Conditions

You are given a positive integer `k` and two lists of conditions:

- `rowConditions[i] = [above_i, below_i]`: number `above_i` must appear in a row strictly above number `below_i`.
- `colConditions[i] = [left_i, right_i]`: number `left_i` must appear in a column strictly left of number `right_i`.

Build a `k x k` matrix that contains each number from `1` to `k` **exactly once**, with every other cell equal to `0`, and that satisfies all conditions. Return any such matrix, or an empty matrix `[]` if none exists.

## Example

```text
Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
Output: [[3,0,0],[0,0,1],[0,2,0]]   (one valid answer)
```

```python

```
