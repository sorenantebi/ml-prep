# Path with Minimum Effort

You are a hiker on a 2D grid `heights` of size `rows x columns`, where `heights[r][c]` is the altitude of cell `(r, c)`. You start in the top-left cell `(0, 0)` and want to reach the bottom-right cell `(rows - 1, columns - 1)`. From any cell you may step up, down, left, or right (staying inside the grid).

The **effort** of a route is the largest absolute height difference between any two consecutive cells along that route. Return the minimum effort over all possible routes from the top-left to the bottom-right cell.

## Example

```text
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: Route 1 -> 3 -> 5 -> 3 -> 5 never has a jump bigger than 2.
```

```python

```
