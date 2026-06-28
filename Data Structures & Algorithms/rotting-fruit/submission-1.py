class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col))
        
        mins = 0
        while q:
            foundRot = False
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r, c))
                        foundRot = True
            
            if foundRot:
                mins += 1
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1
        
        return mins