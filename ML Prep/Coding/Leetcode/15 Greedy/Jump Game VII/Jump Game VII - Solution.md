---
topic: "Greedy"
difficulty: Medium
leetcode: https://leetcode.com/problems/jump-game-vii/
neetcode: https://neetcode.io/problems/jump-game-vii
---
# Jump Game VII - Solution

**Question:** [[Jump Game VII - Question]] · **Difficulty:** Medium

## Intuition

Index `j` is reachable iff `s[j] == '0'` and **some** reachable index lies in the window `[j - maxJump, j - minJump]`. Rather than checking the whole window each time, keep a sliding count of reachable indices inside it: add `reach[j - minJump]` as it enters and subtract `reach[j - maxJump - 1]` as it leaves.

## Approach

1. `reach = [False] * n`, `reach[0] = True`, `count = 0` (reachable indices currently in the window).
2. For `j` from 1 to `n - 1`:
   - If `j - minJump >= 0` and `reach[j - minJump]`: `count += 1` (enters window).
   - If `j - maxJump - 1 >= 0` and `reach[j - maxJump - 1]`: `count -= 1` (leaves window).
   - `reach[j] = count > 0 and s[j] == '0'`.
3. Return `reach[n - 1]`.

## Code

```python
class Solution:
	def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
		n = len(s)
		reach = [False] * n
		reach[0] = True
		count = 0  # number of reachable indices in [j - maxJump, j - minJump]
		for j in range(1, n):
			if j - minJump >= 0 and reach[j - minJump]:
				count += 1  # index j - minJump slides into the window
			if j - maxJump - 1 >= 0 and reach[j - maxJump - 1]:
				count -= 1  # index j - maxJump - 1 slides out
			reach[j] = count > 0 and s[j] == "0"
		return reach[-1]
```

## Complexity

- **Time:** `O(n)` — each index enters and leaves the window once.
- **Space:** `O(n)` — the `reach` array.

## Other Approaches

- **BFS with a "farthest scanned" pointer:** from each popped index only scan positions beyond the previous maximum so each index is enqueued once — Time `O(n)`, Space `O(n)`.
- **Naive DP:** check every index in the window for each `j` — Time `O(n * (maxJump - minJump))`, Space `O(n)`.

## Key Takeaway

When reachability depends on "any reachable index in a sliding range", maintain a running count (or prefix sum) over the window instead of rescanning it.
