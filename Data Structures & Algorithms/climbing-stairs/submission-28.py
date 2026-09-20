class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n + 1)
        
        def recursion(idx):
            if idx > n:
                return 0
            
            if idx == n:
                return 1

            if cache[idx] != -1:
                return cache[idx]
            
            cache[idx] = recursion(idx + 1) + recursion(idx + 2)
            return cache[idx]

        return recursion(0)