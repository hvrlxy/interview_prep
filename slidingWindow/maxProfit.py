'''
You are given an array prices where prices[i] 
is the price of a given stock on the ith day.

You want to maximize your profit by choosing 
a single day to buy one stock and choosing a 
different day in the future to sell that 
stock.

Return the maximum profit you can achieve 
from this transaction. If you cannot achieve 
any profit, return 0.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # initialize two pointers
        buy, sell = 0, 1
        # save the maximum profit possible
        max_profit = 0
        
        while sell <= len(prices) - 1 and prices[buy] > prices[buy + 1]:
            buy += 1
            sell += 1
            
        while sell <= len(prices) - 1:
            #calculate current profit and update the max_profit variable accordingly
            profit = prices[sell] - prices[buy]
            max_profit = max(profit, max_profit)
            
            # if the price at index sell is smaller than price at index buy,
            # move the sell pointer to the buy pointer
            if prices[sell] < prices[buy]:
                buy = sell
            # increment the sell pointer
            sell += 1
        
        return max_profit