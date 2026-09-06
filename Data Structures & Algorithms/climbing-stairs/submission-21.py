class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [0] * (n+1)
        ans[0] = 1
        ans[1] = 1

        for i in range(2, n+1):
            ans[i] = ans[i - 1] + ans[i - 2]
        
        return ans[n]

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