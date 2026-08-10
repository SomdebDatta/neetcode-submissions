class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        
        def backtracking(curr, idx, total):
            if total > target or idx == len(nums):
                return

            if total == target:
                ans.append(curr.copy())
                return
            
            curr.append(nums[idx])
            backtracking(curr, idx, total + nums[idx])
            curr.pop()
            backtracking(curr, idx + 1, total)
        
        backtracking([], 0, 0)
        return ans