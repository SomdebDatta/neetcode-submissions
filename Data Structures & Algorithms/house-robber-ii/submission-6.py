class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def recursion(idx, arr):
            if idx >= len(arr):
                return 0
            
            return max(arr[idx] + recursion(idx + 2, arr), recursion(idx + 1, arr))

        def mem(idx, arr):
            if idx >= len(arr):
                return 0
            if dp[idx] != -1:
                return dp[idx]
            
            dp[idx] = max(arr[idx] + mem(idx + 2, arr), mem(idx + 1, arr))
            return dp[idx]
        

        # return max(recursion(0, nums[:-1]), recursion(0, nums[1:]))

        dp = [-1] * (len(nums) + 1)
        res1 = mem(0, nums[:-1])
        dp = [-1] * (len(nums) + 1)
        res2 = mem(0, nums[1:])
        return max(nums[0], res1, res2)