# Car Pooling

A car with `capacity` empty seats drives only in one direction (east), so it can never go back to an earlier location. You are given `trips`, where `trips[i] = [numPassengers_i, from_i, to_i]` means `numPassengers_i` people must be picked up at kilometer `from_i` and dropped off at kilometer `to_i`.

Return `true` if every trip can be completed without the number of passengers in the car ever exceeding `capacity`, otherwise `false`. Passengers dropped off at a location free their seats before new passengers are picked up at that same location.

## Example

```text
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Explanation: between km 3 and 5 there are 5 passengers
```

```python

```
