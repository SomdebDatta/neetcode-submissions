class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        dp[0][0] = 1

        for idx in range(len(nums)):
            for total, count in dp[idx].items():
                dp[idx + 1][total + nums[idx]] += count
                dp[idx + 1][total - nums[idx]] += count
        
        return dp[len(nums)][target]