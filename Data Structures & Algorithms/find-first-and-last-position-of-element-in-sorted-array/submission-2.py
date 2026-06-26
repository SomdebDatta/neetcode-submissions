class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        if l > r:
            return [-1, -1]
        
        l = mid
        print(mid)
        while l >= 0 and nums[l] == target:
            l -= 1
        l += 1
        r = mid
        while r < len(nums) and nums[r] == target:
            r += 1
        r -= 1
        return [l, r]