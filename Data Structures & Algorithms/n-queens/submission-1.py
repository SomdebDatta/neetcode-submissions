class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        res = []

        board = [["." for _ in range(n)]  for _ in range(n)]

        def backtracking(row):
            if row == n:
                copy = ["".join(curr_row) for curr_row in board]
                res.append(copy)
                return
            
            for col in range(n):
                if col in cols or row + col in posDiag or row - col in negDiag:
                    continue

                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                board[row][col] = 'Q'

                backtracking(row + 1)

                board[row][col] = '.'
                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)
        
        backtracking(0)

        return res