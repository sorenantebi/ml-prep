---
topic: "Math & Geometry"
difficulty: Medium
leetcode: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
neetcode: https://neetcode.io/problems/insert-greatest-common-divisors-in-linked-list
---
# Insert Greatest Common Divisors in Linked List - Solution

**Question:** [[Insert Greatest Common Divisors in Linked List - Question]] · **Difficulty:** Medium

## Intuition

Walk the list once. At each node that has a successor, splice in a new node holding `gcd(cur.val, cur.next.val)`, then jump over the new node to the original successor. The GCD itself comes from the Euclidean algorithm.

## Approach

1. Set `cur = head`.
2. While `cur` and `cur.next` both exist:
   - compute `g = gcd(cur.val, cur.next.val)`;
   - set `cur.next = ListNode(g, cur.next)` to insert the new node;
   - advance `cur = cur.next.next`, skipping the inserted node.
3. Return `head`.

## Code

```python
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
	def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
		def gcd(a: int, b: int) -> int:
			while b:
				a, b = b, a % b
			return a

		cur = head
		while cur and cur.next:
			cur.next = ListNode(gcd(cur.val, cur.next.val), cur.next)
			cur = cur.next.next  # skip the node we just inserted
		return head
```

## Complexity

- **Time:** `O(n * log M)`: one GCD per adjacent pair, and each Euclid run takes `O(log M)` steps for values up to `M`.
- **Space:** `O(1)` extra, not counting the `n - 1` new nodes that form part of the output.

## Other Approaches

- **Collect values, then rebuild:** copy the values into an array, build a new interleaved list, and return it. Time `O(n log M)`, Space `O(n)` extra.

## Key Takeaway

To insert while traversing a linked list, link in the new node first and then step past it (`cur = cur.next.next`), so you never revisit nodes you just created. Know Euclid's `a, b = b, a % b` by heart.
