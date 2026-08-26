class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtracking(op, cl, curr):
            if op == cl == n:
                ans.append(''.join(curr))
                return
            
            if cl < op:
                curr.append(')')
                backtracking(op, cl + 1, curr)
                curr.pop()
            if op <= n:
                curr.append('(')
                backtracking(op + 1, cl, curr)
                curr.pop()
        
        backtracking(0, 0, [])

        return ans
            
