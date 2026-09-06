class Solution:
    def climbStairs(self, n: int) -> int:
        # ans = [0] * (n+1)
        # ans[0] = 1
        # ans[1] = 1
        first = 1
        second = 1
        if n < 2:
            return 1
        ans = first + second

        for i in range(2, n + 1):
            # ans[i] = ans[i - 1] + ans[i - 2]
            ans = first + second
            first = second
            second = ans
            # first = second
        
        return ans

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