class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1)
        def recursion(balance):
            if balance < 0:
                return 0
            
            if balance == 0:
                return 1
            
            if dp[balance] != -1:
                return dp[balance]
            ans = 0

            for num in nums:
                ans += recursion(balance - num)
            
            dp[balance] = ans
            return dp[balance]
        
        return recursion(target)