class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        cache = [0] * (n)
        step1 = 1
        step2 = 2

        for i in range(2, n):
            ans = step1 + step2
            step1 = step2
            step2 = ans

        return ans





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