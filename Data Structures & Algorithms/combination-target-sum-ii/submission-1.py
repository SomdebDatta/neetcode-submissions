class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtracking(idx, curr, total):
            if total > target:
                return
            
            if total == target:
                ans.append(curr.copy())
                return
            
            if idx >= len(candidates):
                return
            
            curr.append(candidates[idx])
            backtracking(idx + 1, curr, total + candidates[idx])
            curr.pop()

            while idx < len(candidates) - 1 and candidates[idx + 1] == candidates[idx]:
                idx += 1
            
            idx += 1
            backtracking(idx, curr, total)

        backtracking(0, [], 0)

        return ans
