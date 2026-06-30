class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def solve(n):
            if n == 0:
                return nums[0]
            if n == 1:
                return max(nums[0], nums[1])
            
            return max(solve(n - 1), nums[n] + solve(n - 2))
        
        def solve2(n):
            if n == 0:
                return nums[0]
            
            if n == 1:
                return max(nums[0], nums[1])
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = max(solve2(n - 1), nums[n] + solve2(n - 2))
            return dp[n]
        
        def solve3(n):
            if n  == 1:
                return nums[0]
            dp = [-1] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            
            return dp[n - 1]

        def solve4(n):
            if n == 1:
                return nums[0]
            prev2 = nums[0]
            prev1 = max(nums[0], nums[1])
            ans = 0

            for i in range(2, n):
                ans = max(prev1, nums[i] + prev2)
                prev2 = prev1
                prev1 = ans
            
            return max(prev1, prev2)

        # return solve(len(nums) - 1)
        
        n = len(nums)

        # dp = [-1] * n
        # return solve2(n - 1)

        # return solve3(n)

        return solve4(n)
        


