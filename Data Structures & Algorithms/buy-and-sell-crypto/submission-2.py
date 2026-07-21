class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)
        start = 0
        end = 1
        max_profit = 0

        while(end < len_prices):
            profit = prices[end] - prices[start]
            if(profit < 0):
                start = end
            elif(profit >= 0):
                max_profit = max(max_profit, profit)
            end = end + 1
        
        return max_profit
            