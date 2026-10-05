# IPO

A company wants to raise its capital before going public. It may complete **at most `k` distinct projects**. Project `i` yields a pure profit of `profits[i]` and can only be started if the current capital is at least `capital[i]`. Completing a project adds its profit to the capital (the required capital is not spent).

Starting with capital `w`, choose up to `k` projects (each at most once, one after another) to maximize the final capital, and return that maximum.

## Example

```text
Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: do project 0 (capital 0 -> 1), then project 2 (capital 1 -> 4)
```

```python

```
