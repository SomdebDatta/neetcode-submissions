class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Recursion
        def solve(pos):
            # BASE CASE
            if pos == 0:
                return cost[0]
            if pos == 1:
                return cost[1]
            
            return cost[pos] + min(solve(pos - 1), solve(pos - 2))
        
        # Recursion + Memoization
        def solve2(pos):
            # BASE CASE
            if pos == 0:
                return cost[0]
            if pos == 1:
                return cost[1]
            
            if dp[pos] != -1:
                return dp[pos]
            
            dp[pos] = cost[pos] + min(solve(pos - 1), solve(pos - 2))
            
            return dp[pos]

        def solve3(n):
            dp = [-1] * (n + 1)

            dp[0] = cost[0]
            dp[1] = cost[1]

            for i in range(2, n):
                dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
            
            return min(dp[n - 1], dp[n - 2])
        
        def solve4(n):
            prev2 = cost[0]
            prev1 = cost[1]
            ans = 0

            for i in range(2, n):
                ans = cost[i] + min(prev1, prev2)
                prev2 = prev1
                prev1 = ans
            
            return min(prev1, prev2)
        

        n = len(cost)
        # return min(solve(n - 1), solve(n - 2))

        # dp = [-1] * (n + 1)
        # return min(solve2(n - 1), solve2(n - 2))

        # return solve3(n)
        
        return solve4(n)


        

