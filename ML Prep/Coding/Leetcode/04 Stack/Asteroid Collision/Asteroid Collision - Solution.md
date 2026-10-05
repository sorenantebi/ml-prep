---
topic: "Stack"
difficulty: Medium
leetcode: https://leetcode.com/problems/asteroid-collision/
neetcode: https://neetcode.io/problems/asteroid-collision
---
# Asteroid Collision - Solution

**Question:** [[Asteroid Collision - Question]] · **Difficulty:** Medium

## Intuition

Collisions only happen between a new left-moving asteroid and the right-moving asteroids immediately to its left — the most recent survivors. Keeping survivors on a stack lets each incoming left-mover fight the top of the stack until it is destroyed or no right-mover remains in its way.

## Approach

1. Iterate through asteroids, maintaining a stack of survivors.
2. For each asteroid `a`, while `a < 0` and the stack top is positive (they collide):
   - If `top < -a`, pop the top and keep going (`a` survives this collision).
   - If `top == -a`, pop the top and destroy `a`; stop.
   - If `top > -a`, destroy `a`; stop.
3. If `a` survived, push it.
4. Return the stack.

## Code

```python
from typing import List


class Solution:
	def asteroidCollision(self, asteroids: List[int]) -> List[int]:
		stack = []
		for a in asteroids:
			alive = True
			# collision only when a moves left and the top moves right
			while alive and a < 0 and stack and stack[-1] > 0:
				if stack[-1] < -a:
					stack.pop()          # top explodes, a keeps going
				elif stack[-1] == -a:
					stack.pop()          # both explode
					alive = False
				else:
					alive = False        # a explodes
			if alive:
				stack.append(a)
		return stack
```

## Complexity

- **Time:** `O(n)` — each asteroid is pushed and popped at most once.
- **Space:** `O(n)` — the stack (also the output) can hold all asteroids.

## Other Approaches

- **Repeated simulation:** scan for adjacent `(+, -)` pairs and resolve them until none remain — Time `O(n^2)`, Space `O(n)`.

## Key Takeaway

When a new element can "cancel" a run of previous elements, use a stack and a while-loop that pops while the cancel condition holds — amortized O(n).
