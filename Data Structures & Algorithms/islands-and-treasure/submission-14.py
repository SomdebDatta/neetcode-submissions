class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        seen = set()
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))

        
        dist = 0

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = min(dist, grid[row][col])

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(ROWS) and c in range(COLS) and (r, c) not in seen and grid[r][c] == 2147483647:
                        q.append((r, c))
                        seen.add((r, c))
        
            dist += 1
        
