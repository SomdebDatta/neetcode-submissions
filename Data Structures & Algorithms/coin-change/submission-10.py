class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [-1] * (amount+1)

        def recursion(pending):
            if pending < 0:
                return float('inf')
            
            if pending == 0:
                return 0
            
            if cache[pending] != -1:
                return cache[pending]
            
            mini = float('inf')
            for coin in coins:
                res = recursion(pending - coin)

                if res != float('inf'):
                    mini = min(mini, 1 + res)
            cache[pending] = mini
            return cache[pending]
        
        res = recursion(amount)
        return res if res != float('inf') else -1