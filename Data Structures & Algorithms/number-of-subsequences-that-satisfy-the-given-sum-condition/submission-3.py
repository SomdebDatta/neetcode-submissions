class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        MOD = 10**9 + 7

        while l <= r:
            if nums[l] + nums[r] <= target:
                ans += 2**(r - l)
                l += 1
                ans %= MOD
            else:
                r -= 1
        
        return ans%MOD