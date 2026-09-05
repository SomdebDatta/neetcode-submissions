class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtracking(opened, closed, curr):
            if opened == closed == n:
                ans.append(''.join(curr))
                return
            
            if opened < n:
                curr.append('(')
                backtracking(opened + 1, closed, curr)
                curr.pop()
            
            if closed < opened:
                curr.append(')')
                backtracking(opened, closed + 1, curr)
                curr.pop()
        
        backtracking(0, 0, [])

        return ans