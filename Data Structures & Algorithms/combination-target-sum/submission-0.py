class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(curr, pos, total):
            if total == target:
                ans.append(curr.copy())
                return
            
            if total > target or pos == len(nums):
                return
            
            curr.append(nums[pos])
            dfs(curr, pos, total + nums[pos])
            # dfs(curr, pos + 1, total + nums[pos])
            curr.pop()
            dfs(curr, pos + 1, total)
        
        dfs([], 0, 0)
        return ans