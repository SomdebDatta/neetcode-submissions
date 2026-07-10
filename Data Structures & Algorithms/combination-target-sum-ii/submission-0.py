class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        
        def dfs(curr, pos, total):
            if total == target:
                ans.append(curr.copy())
                return
            
            if pos >= len(candidates) or total > target:
                return
            
            curr.append(candidates[pos])
            dfs(curr, pos + 1, total + candidates[pos])
            curr.pop()

            while pos + 1 < len(candidates) and candidates[pos] == candidates[pos + 1]:
                pos += 1
            
            dfs(curr, pos + 1, total)
        
        dfs([], 0, 0)
        return ans
