class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, ans, total = 0, float('inf'), 0

        for r in range(len(nums)):
            total += nums[r]
            if total >= target:
                ans = min(ans, r - l + 1)
            while total >= target:
                ans = min(ans, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if ans == float('inf') else ans