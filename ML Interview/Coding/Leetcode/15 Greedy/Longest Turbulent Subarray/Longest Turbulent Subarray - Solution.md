---
topic: "Greedy"
difficulty: Medium
leetcode: https://leetcode.com/problems/longest-turbulent-subarray/
neetcode: https://neetcode.io/problems/longest-turbulent-subarray
---
# Longest Turbulent Subarray - Solution

**Question:** [[Longest Turbulent Subarray - Question]] · **Difficulty:** Medium

## Intuition

Track two running lengths for the turbulent subarray ending at index `i`: `inc` (last step went up) and `dec` (last step went down). An up-step extends a sequence whose previous step was down, and vice versa; an equal pair resets both to 1. This is a sliding-window / Kadane-style scan.

## Approach

1. `inc = dec = 1`, `best = 1`.
2. For `i` from 1 to `n - 1`:
   - If `arr[i] > arr[i-1]`: `inc = dec + 1`, `dec = 1`.
   - If `arr[i] < arr[i-1]`: `dec = inc + 1`, `inc = 1`.
   - Else: `inc = dec = 1`.
   - `best = max(best, inc, dec)`.
3. Return `best`.

## Code

```python
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        inc = dec = best = 1  # lengths of turbulent runs ending here with an up / down step
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                inc, dec = dec + 1, 1  # up-step must follow a down-step
            elif arr[i] < arr[i - 1]:
                inc, dec = 1, inc + 1  # down-step must follow an up-step
            else:
                inc = dec = 1
            best = max(best, inc, dec)
        return best
```

## Complexity

- **Time:** `O(n)` — single pass.
- **Space:** `O(1)` — constant state.

## Other Approaches

- **Two-pointer sliding window:** extend `r` while comparison signs alternate, otherwise move `l` to `r - 1` (or `r` on equality) — Time `O(n)`, Space `O(1)`.
- **Brute force:** check every start and extend while turbulent — Time `O(n^2)`, Space `O(1)`.

## Key Takeaway

For "longest alternating run" problems, keep one running length per possible last-step state and let each step feed the opposite state.
