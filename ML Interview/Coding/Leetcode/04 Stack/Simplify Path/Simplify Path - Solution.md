---
topic: "Stack"
difficulty: Medium
leetcode: https://leetcode.com/problems/simplify-path/
neetcode: https://neetcode.io/problems/simplify-path
---
# Simplify Path - Solution

**Question:** [[Simplify Path - Question]] · **Difficulty:** Medium

## Intuition

Navigating directories is stack-like: entering a directory pushes it and `".."` pops back to the parent. Splitting on `'/'` gives the components; empty strings (from repeated slashes) and `"."` are no-ops.

## Approach

1. Split `path` by `'/'`.
2. For each component:
   - skip `""` and `"."`;
   - on `".."`, pop the stack if non-empty;
   - otherwise push the name.
3. Return `"/" + "/".join(stack)`.

## Code

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split("/"):
            if part == "" or part == ".":
                continue           # repeated slash or current dir
            if part == "..":
                if stack:
                    stack.pop()    # go to parent (no-op at root)
            else:
                stack.append(part) # names like "..." are regular names
        return "/" + "/".join(stack)
```

## Complexity

- **Time:** `O(n)` — splitting and joining are linear in the path length.
- **Space:** `O(n)` — the components and the stack.

## Other Approaches

- **Manual character scan:** walk the string with an index, extracting each name between slashes without `split` — Time `O(n)`, Space `O(n)`; same logic, more code.

## Key Takeaway

Path normalization is a stack problem: push names, pop on `".."`, ignore `"."` and empty segments.
