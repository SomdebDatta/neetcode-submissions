class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(curr, pos):
            if pos == len(nums):
                ans.append(curr.copy())
                return
            
            dfs(curr, pos + 1)
            curr.append(nums[pos])
            dfs(curr, pos + 1)
            curr.pop()

        dfs([], 0)

        return ans