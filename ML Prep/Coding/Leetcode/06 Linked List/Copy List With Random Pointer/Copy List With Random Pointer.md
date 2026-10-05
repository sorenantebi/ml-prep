# Copy List With Random Pointer

A linked list of length `n` is given where every node has a `val`, a `next` pointer, and an extra `random` pointer that may point to any node in the list or be `null`. Build a **deep copy** of the list: `n` brand-new nodes such that for every original node, its copy has the same value, and the copy's `next` and `random` pointers point to the copies of the corresponding original targets. No pointer in the copy may reference an original node. Return the head of the copy.

(LeetCode serializes each node as `[val, random_index]`, where `random_index` is the index of the node `random` points to, or `null`.)

## Example

```text
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

```python

```
