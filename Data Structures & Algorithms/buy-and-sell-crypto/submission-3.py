class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftPointer = 0
        rightPointer = 1
        maxProfit = 0

        while(leftPointer < rightPointer and rightPointer < len(prices)):
            if(prices[rightPointer] - prices[leftPointer] > 0):
                profit = prices[rightPointer] - prices[leftPointer]
                if(profit > maxProfit):
                    maxProfit = profit
            else:
                leftPointer = rightPointer
            rightPointer = rightPointer + 1
        
        return maxProfit
