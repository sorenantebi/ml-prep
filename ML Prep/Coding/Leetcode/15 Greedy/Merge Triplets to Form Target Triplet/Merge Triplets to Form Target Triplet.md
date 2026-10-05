# Merge Triplets to Form Target Triplet

A triplet is an array of three integers. You are given a 2-D array `triplets` where `triplets[i] = [a_i, b_i, c_i]`, and a target triplet `target = [x, y, z]`.

You may apply the following operation any number of times (including zero): choose two indices `i != j` and replace `triplets[j]` with `[max(a_i, a_j), max(b_i, b_j), max(c_i, c_j)]`.

Return `true` if it is possible for `target` to appear as an element of `triplets` after some sequence of operations, otherwise `false`.

## Example

```text
Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true
Explanation: Merge [2,5,3] and [1,7,5] -> [2,7,5].
```

```python

```
