class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(idx, curr):
            if idx == len(nums):
                ans.append(curr.copy())
                return
            
            curr.append(nums[idx])
            backtracking(idx + 1, curr)
            curr.pop()
            backtracking(idx + 1, curr)
        
        backtracking(0, [])

        return ans