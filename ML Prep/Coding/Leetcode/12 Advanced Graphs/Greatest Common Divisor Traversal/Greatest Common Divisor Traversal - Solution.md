---
topic: "Advanced Graphs"
difficulty: Hard
leetcode: https://leetcode.com/problems/greatest-common-divisor-traversal/
neetcode: https://neetcode.io/problems/greatest-common-divisor-traversal
---
# Greatest Common Divisor Traversal - Solution

**Question:** [[Greatest Common Divisor Traversal - Question]] · **Difficulty:** Hard

## Intuition

Comparing all pairs is `O(n^2)`. Instead, connect each index to its **prime factors**: two indices sharing a prime end up in the same component. Union-Find over indices, where for each prime we remember the first index that had it, gives connectivity in near-linear time. A smallest-prime-factor sieve makes factorisation fast.

## Approach

1. If `n == 1`, return `True`. If any value is `1`, return `False` (1 shares no factor with anything).
2. Build a smallest-prime-factor sieve up to `max(nums)`.
3. For each index `i`, factor `nums[i]` into distinct primes; for each prime `p`, union `i` with `first_index[p]` (or record `i` as the first).
4. Return `True` iff all indices have the same root (component count is 1).

## Code

```python
from typing import List


class Solution:
	def canTraverseAllPairs(self, nums: List[int]) -> bool:
		n = len(nums)
		if n == 1:
			return True
		if 1 in nums:
			return False  # 1 can't connect to anything

		max_v = max(nums)
		spf = list(range(max_v + 1))  # smallest prime factor sieve
		i = 2
		while i * i <= max_v:
			if spf[i] == i:
				for j in range(i * i, max_v + 1, i):
					if spf[j] == j:
						spf[j] = i
			i += 1

		parent = list(range(n))

		def find(x):
			while parent[x] != x:
				parent[x] = parent[parent[x]]
				x = parent[x]
			return x

		components = n
		first_index = {}  # prime -> some index whose value has that prime
		for idx, v in enumerate(nums):
			while v > 1:
				p = spf[v]
				while v % p == 0:
					v //= p
				if p in first_index:
					ra, rb = find(idx), find(first_index[p])
					if ra != rb:
						parent[ra] = rb
						components -= 1
				else:
					first_index[p] = idx
		return components == 1
```

## Complexity

- **Time:** `O(M log log M + n log M)` — sieve up to `M = max(nums)`, and each number has `O(log M)` prime factors (union-find is near-constant).
- **Space:** `O(M + n)` — sieve array plus union-find parents.

## Other Approaches

- **Brute-force graph + BFS:** add an edge for every pair with `gcd > 1` and check connectivity — Time `O(n^2 log M)`, Space `O(n^2)`.
- **Trial-division factorisation:** factor each number up to `sqrt(v)` instead of a sieve — Time `O(n · sqrt(M))`, Space `O(n)`.

## Key Takeaway

When edges are defined by a shared property (common prime, same email, same group), union each item with a representative of that property instead of comparing all pairs — `O(n^2)` becomes near-linear.
