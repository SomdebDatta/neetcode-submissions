class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp = defaultdict(int)

        dp[0] = 1

        for idx in range(len(nums)):
            new_dp = defaultdict(int)
            for total, count in dp.items():
                new_dp[total + nums[idx]] += count
                new_dp[total - nums[idx]] += count
            dp = new_dp
        
        return dp[target]