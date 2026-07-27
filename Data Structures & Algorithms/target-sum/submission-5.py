class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def backtrack(idx, total):
            if idx == len(nums):
                return 1 if total == target else 0
            

            return backtrack(idx + 1, total + nums[idx]) + backtrack(idx + 1, total - nums[idx])
        
        return backtrack(0, 0)