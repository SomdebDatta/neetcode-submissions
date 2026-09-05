class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def backtracking(idx, curr):
            if idx >= len(nums):
                ans.append(curr.copy())
                return
            
            curr.append(nums[idx])
            backtracking(idx + 1, curr)
            curr.pop()

            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
                idx += 1
            idx += 1
            backtracking(idx, curr)
        
        backtracking(0, [])

        return ans