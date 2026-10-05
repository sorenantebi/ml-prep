# Simplify Path

You are given an absolute Unix-style file path `path` (it starts with `'/'`). Convert it to its simplified canonical form and return it.

Rules of the Unix-style path:

- `"."` refers to the current directory, and `".."` refers to the parent directory (going above the root stays at the root).
- Multiple consecutive slashes such as `"//"` act as a single slash.
- Any other sequence of characters, including names like `"..."`, is a normal directory/file name.

The canonical path must:

- start with a single `'/'`,
- separate directory names by exactly one `'/'`,
- not end with `'/'` (unless it is the root `"/"` itself), and
- contain no `"."` or `".."` components.

## Example

```text
Input: path = "/home//foo/"
Output: "/home/foo"
```

```python

```
