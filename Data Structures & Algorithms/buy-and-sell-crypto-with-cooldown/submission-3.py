class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.ans = -float('inf')
        dp = {}

        def recursion(canBuy, idx):
            if idx >= len(prices):
                return 0
            
            if (canBuy, idx) in dp:
                return dp[(canBuy, idx)]
                
            if canBuy:
                dp[(canBuy, idx)] = max(-prices[idx] + recursion(0, idx + 1), recursion(1, idx + 1))
                return dp[(canBuy, idx)]
            else:
                dp[(canBuy, idx)] = max(prices[idx] + recursion(1, idx + 2), recursion(0, idx + 1))
                return dp[(canBuy, idx)]
        
        return recursion(True, 0)