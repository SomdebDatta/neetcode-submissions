class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(curr, pos):
            if pos == len(nums):
                ans.append(curr.copy())
                return
            
            curr.append(nums[pos])
            dfs(curr, pos + 1)
            curr.pop()

            while pos + 1 < len(nums) and nums[pos] == nums[pos + 1]:
                pos += 1
            
            dfs(curr, pos + 1)
        
        dfs([], 0)
        return ans