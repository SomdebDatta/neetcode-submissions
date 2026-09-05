class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtracking(curr: list, seen: set):
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                
                curr.append(nums[i])
                seen.add(nums[i])
                backtracking(curr, seen)
                curr.pop()
                seen.remove(nums[i])
        
        backtracking([], set())

        return ans