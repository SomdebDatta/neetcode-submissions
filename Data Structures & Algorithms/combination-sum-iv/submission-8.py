class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [0] * (target + 1)
        dp[0] = 1
        
        for total in range(target + 1):
            curr = 0
            for num in nums:
                if total - num < 0:
                    continue
                curr += dp[total - num]
            dp[total] += curr

        return dp[target]