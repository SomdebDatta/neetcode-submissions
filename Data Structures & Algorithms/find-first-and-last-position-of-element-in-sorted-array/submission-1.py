class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        lfound, rfound = False, False
        

        while l <= r and not (lfound and rfound):
            if nums[l] != target:
                l += 1
            elif nums[l] == target:
                lfound = True
            if nums[r] != target:
                r -= 1
            elif nums[r] == target:
                rfound = True
        
        if lfound and rfound:
            return [l, r]
        return [-1, -1]
        
