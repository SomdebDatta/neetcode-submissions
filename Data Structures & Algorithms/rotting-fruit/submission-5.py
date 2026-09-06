class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        fresh = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        
        time = 0

        while q:
            rot = False
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = dr + row, col + dc

                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh -= 1
                        rot = True
            
            if not rot:
                break
            time += 1
        
        if fresh:
            return -1
        
        return time
                