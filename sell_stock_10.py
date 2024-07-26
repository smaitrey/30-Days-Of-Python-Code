"""
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5

"""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if(prices[i] < buy_price):
                buy_price = prices[i]

            elif(prices[i] - buy_price > profit):
                profit = prices[i] - buy_price

        return profit



## Test-case

prices = [7,1,5,3,6,4]
expected = 5
t1 = Solution()
result = t1.maxProfit(prices)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")

