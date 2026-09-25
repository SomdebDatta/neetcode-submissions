class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        idx = 0
        while idx < len(nums):
            if idx == len(nums) - 1 or nums[idx] != nums[idx + 1]:
                return nums[idx]
            idx += 2