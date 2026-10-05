# Last Stone Weight II

You have an array `stones` where `stones[i]` is the weight of the `i`-th stone. Repeatedly pick **any two** stones with weights `x <= y` and smash them together:

- If `x == y`, both stones are destroyed.
- If `x != y`, the stone of weight `x` is destroyed and the other stone's weight becomes `y - x`.

The process ends when at most one stone remains. Return the **smallest possible** weight of the remaining stone, or `0` if no stones are left.

## Example

```text
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: Smash 2,4 -> 2; 7,8 -> 1; 2,1 -> 1; 1,1 -> 0; leaving [1].
```

```python

```
