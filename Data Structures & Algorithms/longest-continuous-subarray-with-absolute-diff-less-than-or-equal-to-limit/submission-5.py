class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # low, high = nums[0], nums[0]
        # arr = [nums[0]]
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
                # print(arr, low, high)
                res = max(res, len(arr))
        # print(arr)
        return res