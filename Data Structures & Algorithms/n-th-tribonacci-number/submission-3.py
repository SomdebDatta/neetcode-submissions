class Solution:

    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1

        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]

    # def tribonacci(self, n: int) -> int:
    #     dp = [-1] * (n + 1)

    #     def recursion(n):
    #         if n == 0:
    #             return 0
    #         if n == 1 or n == 2:
    #             return 1
            
    #         if dp[n] != -1:
    #             return dp[n]
            
    #         dp[n] = recursion(n - 1) + recursion(n - 2) + recursion(n - 3)
    #         return dp[n]
    
    #     return recursion(n)