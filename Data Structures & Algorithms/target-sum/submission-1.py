class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.ct = 0
        
        def backtrack(idx, total):

            if idx == len(nums):
                if total == target:
                    self.ct += 1
                return
            
            backtrack(idx + 1, total + nums[idx])
            backtrack(idx + 1, total - nums[idx])

        backtrack(0, 0)

        return self.ct