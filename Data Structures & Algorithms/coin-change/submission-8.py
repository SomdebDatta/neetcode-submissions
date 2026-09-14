class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        
        def recursion(total):
            if total == 0:
                return 0
            
            if total in cache:
                return cache[total]

            res = float('inf')

            for coin in coins:
                if total - coin >= 0:
                    res = min(res, 1 + recursion(total - coin))
                
            cache[total] = res
            return cache[total]
        
        res = recursion(amount)

        if res == float('inf'):
            return -1
        return res