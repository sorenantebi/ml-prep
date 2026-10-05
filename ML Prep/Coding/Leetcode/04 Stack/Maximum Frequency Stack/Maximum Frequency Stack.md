# Maximum Frequency Stack

Design a stack-like structure `FreqStack` whose `pop` removes the **most frequent** element rather than simply the most recent one.

- `FreqStack()` — creates an empty frequency stack.
- `push(val)` — pushes integer `val` onto the stack.
- `pop()` — removes and returns the element with the highest frequency currently in the stack. If several elements tie for the highest frequency, remove and return the one that was pushed most recently among them.

`pop` is only called when the stack is non-empty.

## Example

```text
Input:  ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]
        [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation: stack is [5,7,5,7,4,5]; 5 is most frequent -> 5;
then 5 and 7 tie (2 each), 7 is closer to the top -> 7; then 5; then 4
```

```python

```
