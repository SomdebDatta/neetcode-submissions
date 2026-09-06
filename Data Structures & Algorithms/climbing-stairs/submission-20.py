class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        
        def recursion(curr):
            if curr == n:
                return 1
            
            if curr > n:
                return 0
            
            if cache[curr] != -1:
                return cache[curr]
            
            cache[curr] = recursion(curr + 1) + recursion(curr + 2)
            return cache[curr]
        
        return recursion(0)