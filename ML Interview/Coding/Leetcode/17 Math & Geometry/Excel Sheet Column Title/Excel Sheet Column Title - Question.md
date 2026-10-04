---
topic: "Math & Geometry"
difficulty: Easy
leetcode: https://leetcode.com/problems/excel-sheet-column-title/
neetcode: https://neetcode.io/problems/excel-sheet-column-title
---
# Excel Sheet Column Title

**Topic:** [[17 Math & Geometry|Math & Geometry]] · **Difficulty:** Easy · [LeetCode](https://leetcode.com/problems/excel-sheet-column-title/) · [NeetCode](https://neetcode.io/problems/excel-sheet-column-title)

**Solve it in:** [[Excel Sheet Column Title]] · **Answer:** [[Excel Sheet Column Title - Solution]]

## Problem

You are given a positive integer `columnNumber`. Return the label that a spreadsheet program such as Excel would show for that column.

Columns are labeled `A` through `Z` for 1 through 26, then continue with two letters (`AA` = 27, `AB` = 28, ..., `AZ` = 52, `BA` = 53, ..., `ZZ` = 702), then three letters (`AAA` = 703), and so on. Note that this is a base-26 system **without a zero digit**: the letters represent the values 1 through 26.

## Examples

**Example 1**
```text
Input: columnNumber = 1
Output: "A"
```

**Example 2**
```text
Input: columnNumber = 28
Output: "AB"
Explanation: 1 * 26 + 2 = 28
```

**Example 3**
```text
Input: columnNumber = 701
Output: "ZY"
Explanation: 26 * 26 + 25 = 701
```

## Constraints

- `1 <= columnNumber <= 2^31 - 1`

## Starter Code & Test Cases

```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        pass  # your code here


if __name__ == "__main__":
    s = Solution()
    assert s.convertToTitle(1) == "A"
    assert s.convertToTitle(28) == "AB"
    assert s.convertToTitle(701) == "ZY"
    assert s.convertToTitle(26) == "Z"
    assert s.convertToTitle(27) == "AA"
    assert s.convertToTitle(52) == "AZ"
    assert s.convertToTitle(702) == "ZZ"
    assert s.convertToTitle(703) == "AAA"
    assert s.convertToTitle(2147483647) == "FXSHRXW"
    print("All tests passed!")
```
