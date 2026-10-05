# Evaluate Division

You are given `equations`, where `equations[i] = [A, B]` are variable names, and `values[i]` is a real number such that `A / B = values[i]`.

You are also given `queries`, where `queries[j] = [C, D]` asks for the value of `C / D`.

Return a list with the answer to each query, derived from the given equations. If an answer cannot be determined — for example, a variable never appears in any equation, or `C` and `D` are not connected through the equations — return `-1.0` for that query. Note that `X / X` is `1.0` only if `X` appears in some equation; otherwise it is `-1.0`.

The input is guaranteed to be consistent (no contradictions, no division by zero).

## Example

```text
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
       queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.0,0.5,-1.0,1.0,-1.0]
Explanation: a/b = 2, b/c = 3 => a/c = 6, b/a = 0.5; "e" and "x" are unknown.
```

```python

```
