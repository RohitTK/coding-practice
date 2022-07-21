from typing import List

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


class Solution:
    # Logic: Imagine a graph where y-axis is the price and x is the day
    # Finding the maximum possible difference between two points is the base of this logic
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                max_profit = max(prices[r] - prices[l], max_profit)
            else:
                l = r
            r += 1
        return max_profit


testcases = [[7, 1, 5, 3, 6, 4],
             [7, 6, 4, 3, 1]]

sol = Solution()

for testcase in testcases:
    print('Price List:', testcase,
          '\nMax Profit: ', sol.maxProfit(testcase), '\n')
