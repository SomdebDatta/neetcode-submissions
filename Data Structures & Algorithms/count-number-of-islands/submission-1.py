class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        ROWS, COLS = len(grid), len(grid[0])
        

        def dfs(x, y):
            if x not in range(ROWS) or y not in range(COLS) or (x, y) in seen or grid[x][y] != '1':
                return
            
            seen.add((x, y))
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
    
        ans = 0
            
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1' and (row, col) not in seen:
                    dfs(row, col)
                    ans += 1
        
        return ans
