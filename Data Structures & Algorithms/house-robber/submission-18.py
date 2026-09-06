class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        
        def recursion(curr):
            if curr >= len(nums):
                return 0
            
            if cache[curr] != -1:
                return cache[curr]
            
            cache[curr] = max(nums[curr] + recursion(curr + 2), recursion(curr + 1))
            return cache[curr]
        
        return max(recursion(0), recursion(1))