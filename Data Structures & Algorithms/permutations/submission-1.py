class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()

        def dfs(curr, pos):
            if pos == len(nums):
                ans.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if i not in seen:
                    curr.append(nums[i])
                    seen.add(i)
                    dfs(curr, pos + 1)
                    curr.pop()
                    seen.remove(i)
        
        dfs([], 0)
        return ans