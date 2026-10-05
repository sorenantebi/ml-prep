# Stone Game II

Piles of stones are arranged in a row, with `piles[i]` stones in pile `i`. Alice and Bob alternate turns, Alice first. A value `M` starts at `1`.

On each turn, the current player takes **all** stones from the first `X` remaining piles, where `1 <= X <= 2M`. Afterwards `M` becomes `max(M, X)`. The game ends when all piles are taken.

Both players play optimally to maximize their own stones. Return the maximum number of stones Alice can collect.

## Example

```text
Input: piles = [2,7,9,4,4]
Output: 10
Explanation: Alice takes 1 pile (2), Bob takes 2 (7+9), Alice takes the last 2 (4+4) -> 2+4+4 = 10.
```

```python

```
