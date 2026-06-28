class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()
        seen = set()

        for row in range(ROWS):
            for col in range(COLS):
                if (row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1) and board[row][col] == 'O':
                    q.append((row, col))
        
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                
                if row in range(ROWS) and col in range(COLS) and (row, col) not in seen and board[row][col] == 'O':
                    seen.add((row, col))
                    q.append((row + 1, col))
                    q.append((row, col + 1))
                    q.append((row, col - 1))
                    q.append((row - 1, col))
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O' and (row, col) not in seen:
                    board[row][col] = 'X'
            