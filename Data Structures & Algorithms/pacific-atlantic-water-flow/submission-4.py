class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(x, y, seen, prevHeight):
            if x not in range(ROWS) or y not in range(COLS) or (x, y) in seen or heights[x][y] < prevHeight:
                return
            
            seen.add((x, y))
            dfs(x + 1, y, seen, heights[x][y])
            dfs(x - 1, y, seen, heights[x][y])
            dfs(x, y + 1, seen, heights[x][y])
            dfs(x, y - 1, seen, heights[x][y])
        
        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 or col == 0:
                    dfs(row, col, pac, 0)
                if row == ROWS - 1 or col == COLS - 1:
                    dfs(row, col, atl, 0)
        
        ans = []

        for x, y in pac:
            if (x, y) in atl:
                ans.append([x, y])
        
        return ans