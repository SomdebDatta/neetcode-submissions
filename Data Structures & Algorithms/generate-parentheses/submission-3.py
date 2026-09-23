class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
         
        def recursion(curr, op, cl):
            if op == cl == n:
                ans.append(''.join(curr))
                return

            if op < n:
                curr.append('(')
                recursion(curr, op + 1, cl)
                curr.pop()
            
            if cl < op:
                curr.append(')')
                recursion(curr, op, cl + 1)
                curr.pop()
        
        recursion([], 0, 0)

        return ans
        