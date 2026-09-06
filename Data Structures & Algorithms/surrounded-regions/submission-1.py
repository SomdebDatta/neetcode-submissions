class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        saved = set()

        def dfs(x, y):
            if x not in range(ROWS) or y not in range(COLS) or (x, y) in saved or board[x][y] == 'X':
                return
            
            saved.add((x, y))
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O' and (row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1):
                    dfs(row, col)


        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O' and (row, col) not in saved:
                    board[row][col] = 'X'
        