class Solution:
    def climbStairs(self, n: int) -> int:
        def solveRecursion(num):
            if num == n:
                return 1
            
            if num > n:
                return 0
            
            return solveRecursion(num + 1) + solveRecursion(num + 2)
        
        def solveMem(num):
            if num == n:
                return 1
            if num > n:
                return 0
            if dp[num] != -1:
                return dp[num]
            
            dp[num] = solveMem(num + 1) + solveMem(num + 2)
            return dp[num]


        # return solveRecursion(0)

        dp = [-1] * (n + 1)
        return solveMem(0)

        

