# Jump Game VII

You are given a binary string `s` (0-indexed) and integers `minJump` and `maxJump`. You start at index `0`, which is guaranteed to be `'0'`. From index `i` you may jump to index `j` if:

- `i + minJump <= j <= min(i + maxJump, s.length - 1)`, and
- `s[j] == '0'`.

Return `true` if you can reach index `s.length - 1`, otherwise `false`.

## Example

```text
Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation: 0 -> 3 -> 5
```

```python

```
