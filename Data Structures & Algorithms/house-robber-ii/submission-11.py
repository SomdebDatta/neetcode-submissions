class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        def recursion(idx, arr):
            if idx >= len(arr):
                return 0
            
            if cache[idx] != -1:
                return cache[idx]
            
            cache[idx] = max(arr[idx] + recursion(idx + 2, arr), recursion(idx + 1, arr))
            return cache[idx]
 
        ans1 = recursion(0, nums[:-1])
        cache = [-1] * len(nums)
        ans2 = recursion(0, nums[1:])
        return max(nums[0], ans1, ans2)