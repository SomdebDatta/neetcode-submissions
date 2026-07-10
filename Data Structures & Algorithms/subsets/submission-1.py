class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(curr, pos):
            if pos == len(nums):
                ans.append(curr.copy())
                return
            
            curr.append(nums[pos])
            dfs(curr, pos + 1)
            curr.pop()
            dfs(curr, pos + 1)

        dfs([], 0)

        return ans