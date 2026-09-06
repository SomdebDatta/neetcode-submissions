class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(row, col):
            if row not in range(ROWS) or col not in range(COLS) or grid[row][col] != '1':
                return
            
            grid[row][col] = '0'
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
    
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(row, col)
        
        return islands