class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        buyVal = float('inf')

        #profit = price - minimum buy value

        for p in prices:
            if p < buyVal:
                buyVal = min(p, buyVal)

            profit = max(p - buyVal, profit)
            print(profit)
            
        return profit
             

        