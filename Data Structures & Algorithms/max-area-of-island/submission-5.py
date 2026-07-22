class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        area = 0


        def recursion(x, y):
            if x not in range(ROWS) or y not in range(COLS) or (x, y) in seen or grid[x][y] != 1:
                return 0
            
            seen.add((x, y))
            
            return 1 + recursion(x + 1, y) + recursion(x - 1, y) + recursion(x, y + 1) + recursion(x, y - 1)
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, recursion(r, c))
        
        return area
