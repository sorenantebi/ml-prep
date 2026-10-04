---
topic: "Stack"
difficulty: Hard
leetcode: https://leetcode.com/problems/maximum-frequency-stack/
neetcode: https://neetcode.io/problems/maximum-frequency-stack
---
# Maximum Frequency Stack

**Topic:** [[04 Stack|Stack]] · **Difficulty:** Hard · [LeetCode](https://leetcode.com/problems/maximum-frequency-stack/) · [NeetCode](https://neetcode.io/problems/maximum-frequency-stack)

**Solve it in:** [[Maximum Frequency Stack]] · **Answer:** [[Maximum Frequency Stack - Solution]]

## Problem

Design a stack-like structure `FreqStack` whose `pop` removes the **most frequent** element rather than simply the most recent one.

- `FreqStack()` — creates an empty frequency stack.
- `push(val)` — pushes integer `val` onto the stack.
- `pop()` — removes and returns the element with the highest frequency currently in the stack. If several elements tie for the highest frequency, remove and return the one that was pushed most recently among them.

`pop` is only called when the stack is non-empty.

## Examples

**Example 1**
```text
Input:  ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]
        [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation: stack is [5,7,5,7,4,5]; 5 is most frequent -> 5;
then 5 and 7 tie (2 each), 7 is closer to the top -> 7; then 5; then 4
```

**Example 2**
```text
Input:  ["FreqStack","push","push","pop","pop"]
        [[],[1],[2],[],[]]
Output: [null,null,null,2,1]
Explanation: all frequencies tie, so it behaves like a normal stack
```

## Constraints

- `0 <= val <= 10^9`
- At most `2 * 10^4` calls to `push` and `pop`
- `pop` is only called on a non-empty stack

## Starter Code & Test Cases

```python
class FreqStack:
    def __init__(self):
        pass  # your code here

    def push(self, val: int) -> None:
        pass

    def pop(self) -> int:
        pass


if __name__ == "__main__":
    fs = FreqStack()
    for v in [5, 7, 5, 7, 4, 5]:
        fs.push(v)
    assert [fs.pop() for _ in range(4)] == [5, 7, 5, 4]

    fs = FreqStack()
    fs.push(1)
    fs.push(2)
    assert fs.pop() == 2
    assert fs.pop() == 1

    fs = FreqStack()
    for v in [3, 3, 3]:
        fs.push(v)
    assert [fs.pop() for _ in range(3)] == [3, 3, 3]

    fs = FreqStack()
    for v in [1, 2, 1, 2, 3]:
        fs.push(v)
    assert fs.pop() == 2   # 1 and 2 tie at freq 2, 2 pushed later
    fs.push(2)             # 2 back to freq 2, now most recent
    assert fs.pop() == 2
    assert [fs.pop() for _ in range(4)] == [1, 3, 2, 1]

    fs = FreqStack()
    fs.push(10**9)
    fs.push(0)
    fs.push(10**9)
    assert fs.pop() == 10**9
    assert fs.pop() == 0
    assert fs.pop() == 10**9
    print("All tests passed!")
```
