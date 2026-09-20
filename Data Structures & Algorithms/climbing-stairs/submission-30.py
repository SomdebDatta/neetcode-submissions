class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        cache = [0] * (n)
        cache[0] = 1
        cache[1] = 2

        for i in range(2, n):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[-1]





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