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

        def solveTab(num):
            dp = [-1] * (num + 1)

            dp[-1] = 1
            dp[-2] = 1

            for i in range(num - 2, -1, -1):
                dp[i] = dp[i + 1] + dp[i + 2]
            
            return dp[0]

        def bu(num):
            if num < 3: return num
            last = 1
            secondLast = 1
            ans = 0
            for i in range(num - 2, -1, -1):
                ans = last + secondLast
                last = secondLast
                secondLast = ans
            
            return ans
        # return solveRecursion(0)

        # dp = [-1] * (n + 1)
        # return solveMem(0)

        # return solveTab(n)

        return bu(n)
        

