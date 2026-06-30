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

        # return solveRecursion(0)
        dp = [-1] * (len(nums) + 1)
        return solveMem(0)

