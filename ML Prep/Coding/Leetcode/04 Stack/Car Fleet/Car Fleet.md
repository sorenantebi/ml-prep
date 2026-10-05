# Car Fleet

There are `n` cars on a one-lane road heading to a destination at mile `target`. Car `i` starts at mile `position[i]` and drives at constant speed `speed[i]` (miles per hour). All positions are distinct.

A car can never pass the car in front of it. If it catches up, it slows down and drives bumper-to-bumper at the slower car's speed; from then on they move together as one **car fleet**. A single car on its own is also a fleet. If a car catches up with a fleet exactly at the destination, it still counts as part of that fleet.

Return the number of distinct car fleets that arrive at the destination.

## Example

```text
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation: cars at 10 and 8 meet at 12; car at 0 alone; cars at 5 and 3 meet at 6
```

```python

```
