"""
Stock Market Profit Calculator

This module provides functionality to calculate the maximum profit
that can be made from buying and selling a stock given an array of prices.
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Calculate the maximum profit that can be made from buying and selling a stock.
    
    This function finds the maximum profit by determining the optimal buy and sell points
    in the given array of stock prices. It assumes you can only buy once and sell once,
    and you must buy before you sell.
    
    Args:
        prices (List[int]): A list of stock prices where prices[i] is the price on day i.
        
    Returns:
        int: The maximum profit that can be achieved. If no profit can be made, returns 0.
        
    Time Complexity:
        O(n) where n is the number of prices
        
    Space Complexity:
        O(1) - constant extra space
        
    Example:
        >>> max_profit([7, 1, 5, 3, 6, 4])
        5  # Buy at 1, sell at 6
        
        >>> max_profit([7, 6, 4, 3, 1])
        0  # No profit can be made
    """
    if not prices or len(prices) < 2:
        return 0
        
    max_profit = 0
    min_price = prices[0]
    
    for price in prices[1:]:
        # Calculate potential profit if we sell at current price
        potential_profit = price - min_price
        
        # Update max profit if this is better
        max_profit = max(max_profit, potential_profit)
        
        # Update min price if current price is lower
        min_price = min(min_price, price)
        
    return max_profit
