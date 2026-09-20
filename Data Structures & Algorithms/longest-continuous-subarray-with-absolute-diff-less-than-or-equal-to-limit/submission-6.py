class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 1

        for j in range(len(nums)):
            arr = [nums[j]]
            low, high = nums[j], nums[j]

            for i in range(j + 1, len(nums)):
                if nums[i] <= low:
                    if high - nums[i] > limit:
                        low = nums[i]
                        high = nums[i]
                        arr = [nums[i]]
                    else:
                        low = nums[i]
                        arr.append(nums[i])
                elif nums[i] >= high:
                    if nums[i] - low > limit:
                        low = nums[i]
                        high = nums[i]
                        arr = [nums[i]]
                    else:
                        high = nums[i]
                        arr.append(nums[i])
                else:
                    arr.append(nums[i])
                res = max(res, len(arr))
                
        return res