class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def solveRecursion(n):
            if n >= len(nums):
                return 0
            
            return max(nums[n] + solveRecursion(n + 2), solveRecursion(n + 1))
        

        def solveMem(n):
            if n>= len(nums):
                return 0
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = max(nums[n] + solveMem(n + 2), solveMem(n + 1))
            return dp[n]


        def solveTab(nums):
            if len(nums) < 2: return max(nums)
            dp = [-1] * (len(nums) + 1)

            dp[-1] = max(nums[-1], nums[-2])
            dp[-2] = nums[-1]
            dp[-3] = max(nums[-1], nums[-2])
            
            for i in range(len(nums) - 3, -1, -1):
                dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
            
            return dp[0]

        # return solveRecursion(0)
        
        # dp = [-1] * (len(nums) + 1)
        # return solveMem(0)
    
        return solveTab(nums)

