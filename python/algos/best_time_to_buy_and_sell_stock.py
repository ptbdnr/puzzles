"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        bb, bs, p = 0, 0, 0
        for i in range(1, len(prices)):
            if prices[i] - prices[bb] > p:
                bs = i
                p = prices[bs] - prices[bb]
            if prices[i] < prices[bb]:
                bb = i
                bs = i
        return p
