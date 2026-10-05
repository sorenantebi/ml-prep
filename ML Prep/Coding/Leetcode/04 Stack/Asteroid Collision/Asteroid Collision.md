# Asteroid Collision

You are given an integer array `asteroids` describing asteroids in a row. The absolute value is the asteroid's size; the sign is its direction (positive = moving right, negative = moving left). All asteroids move at the same speed.

When a right-moving asteroid meets a left-moving one, they collide: the smaller one explodes; if they are the same size, both explode. Asteroids moving in the same direction never meet (and a left-mover on the left with a right-mover on the right move apart).

Return the state of the asteroids after all collisions, in their original left-to-right order.

## Example

```text
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: 10 and -5 collide, 10 survives
```

```python

```
