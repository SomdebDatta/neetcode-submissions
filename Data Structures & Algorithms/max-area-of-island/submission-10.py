class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        ans = 0

        def dfs(x, y):
            if (x, y) in seen or x not in range(ROWS) or y not in range(COLS) or grid[x][y] != 1:
                return 0
            seen.add((x, y))
            return 1 + (dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r, c))
        
        return ans