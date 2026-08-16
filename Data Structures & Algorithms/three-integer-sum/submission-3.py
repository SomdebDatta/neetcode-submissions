class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0

        while i < len(nums) - 2:

            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                curr_total = nums[i] + nums[l] + nums[r]

                if curr_total < 0:
                    l += 1
                elif curr_total > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            i += 1
        
        return ans