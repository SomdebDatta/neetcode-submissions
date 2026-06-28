class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        ans = 0

        def dfs(x, y):
            if x not in range(ROWS) or y not in range(COLS) or grid[x][y] != 1 or (x, y) in seen:
                return 0
            seen.add((x, y))
            return 1 + dfs(x + 1, y) + dfs(x, y + 1) + dfs(x - 1, y) + dfs(x, y - 1)
            
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in seen:
                    ans = max(ans, dfs(row, col))
        
        return ans