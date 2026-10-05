---
topic: "Stack"
difficulty: Medium
leetcode: https://leetcode.com/problems/simplify-path/
neetcode: https://neetcode.io/problems/simplify-path
---
# Simplify Path

**Topic:** [[04 Stack|Stack]] · **Difficulty:** Medium · [LeetCode](https://leetcode.com/problems/simplify-path/) · [NeetCode](https://neetcode.io/problems/simplify-path)

**Solve it in:** [[Simplify Path]] · **Answer:** [[Simplify Path - Solution]]

## Problem

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

## Examples

**Example 1**
```text
Input: path = "/home//foo/"
Output: "/home/foo"
```

**Example 2**
```text
Input: path = "/a/./b/../../c/"
Output: "/c"
```

**Example 3**
```text
Input: path = "/../"
Output: "/"
```

## Constraints

- `1 <= path.length <= 3000`
- `path` consists of English letters, digits, `'.'`, `'/'`, or `'_'`
- `path` is a valid absolute Unix path

## Starter Code & Test Cases

```python
class Solution:
	def simplifyPath(self, path: str) -> str:
		pass  # your code here


if __name__ == "__main__":
	s = Solution()
	assert s.simplifyPath("/home/") == "/home"
	assert s.simplifyPath("/home//foo/") == "/home/foo"
	assert s.simplifyPath("/a/./b/../../c/") == "/c"
	assert s.simplifyPath("/../") == "/"
	assert s.simplifyPath("/") == "/"
	assert s.simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d"
	assert s.simplifyPath("/a//b////c/d//././/..") == "/a/b/c"
	assert s.simplifyPath("/x_1/..hidden/.") == "/x_1/..hidden"
	print("All tests passed!")
```
