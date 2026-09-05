class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def backtracking(idx, curr, total):
            if total > target:
                return
            if total == target:
                ans.append(curr.copy())
                return
            
            if idx == len(nums):
                return
            
            curr.append(nums[idx])
            backtracking(idx, curr, total + nums[idx])
            curr.pop()
            backtracking(idx + 1, curr, total)
            

        backtracking(0, [], 0)
        return ans