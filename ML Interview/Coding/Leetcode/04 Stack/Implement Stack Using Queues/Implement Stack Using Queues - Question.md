---
topic: "Stack"
difficulty: Easy
leetcode: https://leetcode.com/problems/implement-stack-using-queues/
neetcode: https://neetcode.io/problems/implement-stack-using-queues
---
# Implement Stack Using Queues

**Topic:** [[04 Stack|Stack]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/implement-stack-using-queues/) · [NeetCode](https://neetcode.io/problems/implement-stack-using-queues)

**Solve it in:** [[Implement Stack Using Queues]] · **Answer:** [[Implement Stack Using Queues - Solution]]

## Problem

Build a last-in-first-out (LIFO) stack using only queues. Implement the class `MyStack` with:

- `MyStack()` — creates an empty stack.
- `push(x)` — puts element `x` on top of the stack.
- `pop()` — removes the top element and returns it.
- `top()` — returns the top element without removing it.
- `empty()` — returns `true` if the stack holds no elements, `false` otherwise.

You may only use standard queue operations: add to the back, look at/remove from the front, size, and is-empty (a `deque` used strictly as a queue is fine). All calls to `pop` and `top` are guaranteed to be on a non-empty stack.

**Follow-up:** can you do it with a single queue?

## Examples

**Example 1**
```text
Input:  ["MyStack","push","push","top","pop","empty"]
        [[],[1],[2],[],[],[]]
Output: [null,null,null,2,2,false]
```

**Example 2**
```text
Input:  ["MyStack","push","pop","empty"]
        [[],[5],[],[]]
Output: [null,null,5,true]
```

## Constraints

- `1 <= x <= 9`
- At most `100` calls are made to `push`, `pop`, `top` and `empty`
- `pop` and `top` are only called on a non-empty stack

## Starter Code & Test Cases

```python
from collections import deque


class MyStack:
    def __init__(self):
        pass  # your code here

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def top(self) -> int:
        pass

    def empty(self) -> bool:
        pass


if __name__ == "__main__":
    st = MyStack()
    assert st.empty() is True
    st.push(1)
    st.push(2)
    assert st.top() == 2
    assert st.pop() == 2
    assert st.empty() is False
    assert st.top() == 1
    st.push(3)
    st.push(4)
    assert st.pop() == 4
    assert st.pop() == 3
    assert st.pop() == 1
    assert st.empty() is True

    st2 = MyStack()
    for v in range(1, 10):
        st2.push(v)
    assert [st2.pop() for _ in range(9)] == list(range(9, 0, -1))
    assert st2.empty() is True
    print("All tests passed!")
```
