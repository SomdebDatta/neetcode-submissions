class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque([])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))
        
        dist = 1
        seen = set()
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r in range(ROWS) and c in range(COLS) and (r, c) not in seen and grid[r][c] == 2147483647:
                        seen.add((r, c))
                        grid[r][c] = dist
                        q.append((r, c))
            dist += 1
        