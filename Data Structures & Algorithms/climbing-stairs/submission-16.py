class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0] * (n + 1)

        cache[0] = cache[1] = 1

        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
    
        return cache[n]







        cache = [-1] * (n + 1)

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



        

        
            

