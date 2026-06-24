class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, ans, total = 0, 100001, 0

        for r in range(len(nums)):
            total += nums[r]
            if total >= target:
                ans = min(ans, r - l + 1)
            while total >= target:
                ans = min(ans, r - l + 1)
                total -= nums[l]
                l += 1
        if ans == 100001: return 0
        return ans