class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def recursion(target):
            if target == 0:
                return 0
            
            if target < 0:
                return float('inf')
            
            mini = float('inf')
            for coin in coins:
                ans = recursion(target - coin)

                if ans != float('inf'):
                    mini = min(mini, 1 + ans)
            
            return mini
        
        
        def mem(target):
            if target == 0:
                return 0
            
            if target < 0:
                return float('inf')
            
            if dp[target] != -1:
                return dp[target]
            
            mini = float('inf')

            for coin in coins:
                ans = mem(target - coin)

                if ans != float('inf'):
                    mini = min(mini, 1 + ans)
                
            dp[target] = mini
            return dp[target]        
        
        # res = recursion(amount)
        # return res if res != float('inf') else -1

        dp = [-1] * (amount + 1)
        res = mem(amount)
        return res if res != float('inf') else -1