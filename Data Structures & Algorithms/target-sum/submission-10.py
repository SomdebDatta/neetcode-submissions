class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        def backtrack(idx, total):
            if idx == len(nums):
                if total == target:
                    return 1
                return 0
            
            return backtrack(idx + 1, total + nums[idx]) + backtrack(idx + 1, total - nums[idx])

        return backtrack(0, 0)