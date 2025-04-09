"""
Unit tests for the stock_profit module.

This module contains tests for the max_profit function to ensure
it correctly calculates the maximum profit from stock prices.
"""

import unittest
from stock_profit import max_profit


class TestMaxProfit(unittest.TestCase):
    """Test cases for the max_profit function."""

    def test_normal_case(self):
        """Test with a normal case where profit can be made."""
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(prices), 5)  # Buy at 1, sell at 6

    def test_decreasing_prices(self):
        """Test with decreasing prices where no profit can be made."""
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(prices), 0)

    def test_increasing_prices(self):
        """Test with strictly increasing prices."""
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(max_profit(prices), 4)  # Buy at 1, sell at 5

    def test_empty_list(self):
        """Test with an empty list."""
        prices = []
        self.assertEqual(max_profit(prices), 0)

    def test_single_price(self):
        """Test with a single price where no transaction is possible."""
        prices = [5]
        self.assertEqual(max_profit(prices), 0)

    def test_two_prices_profit(self):
        """Test with two prices where profit is possible."""
        prices = [1, 2]
        self.assertEqual(max_profit(prices), 1)

    def test_two_prices_no_profit(self):
        """Test with two prices where no profit is possible."""
        prices = [2, 1]
        self.assertEqual(max_profit(prices), 0)

    def test_large_price_list(self):
        """Test with a large list of prices."""
        prices = [7, 1, 5, 3, 6, 4, 8, 2, 9, 0, 3]
        self.assertEqual(max_profit(prices), 8)  # Buy at 1, sell at 9

    def test_same_prices(self):
        """Test with all the same prices."""
        prices = [5, 5, 5, 5, 5]
        self.assertEqual(max_profit(prices), 0)

    def test_negative_prices(self):
        """Test with negative prices (representing debt or liability)."""
        prices = [-7, -1, -5, -3, -6, -4]
        self.assertEqual(max_profit(prices), 6)  # Buy at -7, sell at -1


if __name__ == "__main__":
    unittest.main()


