# Baseball Game

You are keeping score for a baseball game with unusual rules. You receive a list of strings `operations`, processed left to right, starting from an empty record of scores. Each operation is one of:

- An integer `x` (as a string): record a new score of `x`.
- `"+"`: record a new score equal to the sum of the previous two scores.
- `"D"`: record a new score equal to double the previous score.
- `"C"`: invalidate (remove) the previous score from the record.

Return the sum of all scores remaining in the record after every operation has been applied. The input is guaranteed to be valid: `"+"` always has at least two prior scores, and `"D"`/`"C"` always have at least one.

## Example

```text
Input: operations = ["5","2","C","D","+"]
Output: 30
Explanation: record evolves [5] -> [5,2] -> [5] -> [5,10] -> [5,10,15]; sum = 30
```

```python

```
