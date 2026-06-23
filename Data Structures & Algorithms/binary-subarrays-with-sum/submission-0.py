class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x):
            if x < 0:
                return 0
            total, l = 0, 0
            res = 0

            for r in range(len(nums)):
                total += nums[r]
                while total > x and l <= r:
                    total -= nums[l]
                    l += 1
                res += (r - l + 1)
            return res
        
        return helper(goal) - helper(goal - 1)