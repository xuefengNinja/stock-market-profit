# Stock Market Profit Calculator

This project provides a function to calculate the maximum profit that can be made from buying and selling a stock given an array of stock prices.

## Problem Description

Given an array of stock prices where `prices[i]` is the price of a stock on day `i`, find the maximum profit that can be achieved by buying and selling once. You must buy before you sell.

## Implementation

The solution uses a simple one-pass algorithm with O(n) time complexity and O(1) space complexity:

1. Keep track of the minimum price seen so far
2. For each price, calculate the potential profit if we sell at that price
3. Update the maximum profit if the potential profit is greater

## Usage

```python
from stock_profit import max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print(f"Maximum profit: {profit}")  # Output: Maximum profit: 5
```

## Testing

The project includes comprehensive unit tests to verify the functionality:

```bash
python -m unittest test_stock_profit.py
```

## Time and Space Complexity

- Time Complexity: O(n) where n is the number of prices
- Space Complexity: O(1) - constant extra space

## Edge Cases Handled

- Empty price list
- Single price (no transaction possible)
- Strictly decreasing prices (no profit possible)
- Negative prices (representing debt or liability)
