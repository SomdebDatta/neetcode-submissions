class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
                continue
            
            profit = max(profit, prices[r] - prices[l])
            r += 1
        
        return profit
