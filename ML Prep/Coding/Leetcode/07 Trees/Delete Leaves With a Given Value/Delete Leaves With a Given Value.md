# Delete Leaves With a Given Value

Given the `root` of a binary tree and an integer `target`, delete every **leaf** whose value equals `target`. Deleting leaves can turn their parent into a new leaf; if that parent also has value `target`, it must be deleted too, and so on, until no leaf with value `target` remains. Return the resulting root (which may be `null`).

## Example

```text
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: the 2-leaves go first; then the left child 2 becomes a leaf and is removed too.
```

```python

```
