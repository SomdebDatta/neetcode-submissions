class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        def backtracking(idx, balance, path):

            if len(path) == 4:
                if balance == 0:
                    ans.append(path.copy())
                return

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
            
                path.append(nums[i])
                backtracking(i + 1, balance - nums[i], path)
                path.pop()
        
        backtracking(0, target, [])
        return ans


        
        