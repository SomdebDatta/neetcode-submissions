class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.ans = -float('inf')
        dp = [[-1, -1] for _ in range(len(prices))]


        def recursion(canBuy, idx):
            if idx >= len(prices):
                return 0
            
            if dp[idx][canBuy] != -1:
                return dp[idx][canBuy]
                
            if canBuy:
                dp[idx][canBuy] = max(-prices[idx] + recursion(0, idx + 1), recursion(1, idx + 1))
                return dp[idx][canBuy]
            else:
                dp[idx][canBuy] = max(prices[idx] + recursion(1, idx + 2), recursion(0, idx + 1))
                return dp[idx][canBuy]
        
        return recursion(1, 0)