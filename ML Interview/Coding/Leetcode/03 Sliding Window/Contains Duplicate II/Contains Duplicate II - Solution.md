---
topic: "Sliding Window"
difficulty: Easy
leetcode: https://leetcode.com/problems/contains-duplicate-ii/
neetcode: https://neetcode.io/problems/contains-duplicate-ii
---
# Contains Duplicate II - Solution

**Question:** [[Contains Duplicate II - Question]] · **Difficulty:** Easy

## Intuition

We only care about duplicates within distance `k`, so maintain a sliding window (as a hash set) containing the last `k` values. When a new value is already in the window, a close duplicate exists. Evict the value that falls out of range as the window slides.

## Approach

1. Create an empty set `window`.
2. For each index `i`:
   - If `nums[i]` is in `window`, return `True`.
   - Add `nums[i]` to `window`.
   - If `len(window) > k`, remove `nums[i - k]`.
3. Return `False`.

## Code

```python
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()  # values at indices (i - k, i)
        for i, x in enumerate(nums):
            if x in window:
                return True
            window.add(x)
            if len(window) > k:
                window.remove(nums[i - k])
        return False
```

## Complexity

- **Time:** `O(n)` — each element is added and removed at most once with `O(1)` set operations.
- **Space:** `O(min(n, k))` — the window holds at most `k` values.

## Other Approaches

- **Last-seen index map:** store the latest index of each value and check `i - last[x] <= k` — Time `O(n)`, Space `O(n)`.
- **Brute force:** compare each `i` with the next `k` elements — Time `O(n * k)`, Space `O(1)`.

## Key Takeaway

A fixed-size sliding window backed by a hash set answers "is there a duplicate within distance k" in linear time.
