# Online Stock Span

Design a class `StockSpanner` that receives a stock's price one day at a time and, for each new price, returns that day's **span**: the number of consecutive days, ending with today and going backwards, on which the price was less than or equal to today's price.

- `StockSpanner()` — initializes the object.
- `next(price)` — records today's `price` and returns its span.

For example, if the last prices were `[7, 2, 1, 2]` and today's price is `2`, the span is `4` (today plus the previous three days at or below `2`); if today's price were `8`, the span would be `5`.

## Example

```text
Input:  ["StockSpanner","next","next","next","next","next","next","next"]
        [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
```

```python

```
