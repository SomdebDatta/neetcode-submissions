class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        pacSet, atlSet = set(), set()
        

        def dfs(x, y, val, seen):
            if x in range(ROWS) and y in range(COLS) and (x, y) not in seen and heights[x][y] >= val:
                seen.add((x, y))
                dfs(x + 1, y, heights[x][y], seen)
                dfs(x, y + 1, heights[x][y], seen)
                dfs(x, y - 1, heights[x][y], seen)
                dfs(x - 1, y, heights[x][y], seen)
        
        # Pacific DFS
        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 or (row != 0 and col == 0):
                    dfs(row, col, heights[row][col], pacSet)
        
        # Atlantic DFS
        for row in range(ROWS):
            for col in range(COLS):
                if col == COLS - 1 or (col != COLS - 1 and row == ROWS - 1):
                    dfs(row, col, heights[row][col], atlSet)
        ans = []
        for x, y in pacSet:
            if (x, y) in atlSet:
                ans.append([x, y])
        
        return ans
        