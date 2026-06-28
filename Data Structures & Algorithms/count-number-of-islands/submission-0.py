class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        seen = set() # (x, y)
        islands = 0

        def dfs(x, y):
            if x in range(ROWS) and y in range(COLS) and grid[x][y] == '1' and (x, y) not in seen:
                seen.add((x, y))
                for r, c in directions:
                    dfs(x + r, y + c)


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1' and (row, col) not in seen:
                    islands += 1
                    dfs(row, col)
        return islands
        
