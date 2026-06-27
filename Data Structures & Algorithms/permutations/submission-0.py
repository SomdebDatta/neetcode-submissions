class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtracking(seen, curr):
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return
            
            for num in nums:
                if num in seen:
                    continue
                seen.add(num)
                curr.append(num)
                backtracking(seen, curr)
                seen.remove(num)
                curr.pop()
        backtracking(set(), [])
        return ans