class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def dfs(x, y, idx, seen):

            if idx == len(word):
                return True

            if x not in range(ROWS) or y not in range(COLS) or (x, y) in seen or board[x][y] != word[idx]:
                return False
            
            seen.add((x, y))
            
            ans = dfs(x + 1, y, idx + 1, seen) or dfs(x - 1, y, idx + 1, seen) or dfs(x, y + 1, idx + 1, seen) or dfs(x, y - 1, idx + 1, seen)
            seen.remove((x, y))
            return ans


        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0] and dfs(row, col, 0, set()):
                    return True
        
        return False