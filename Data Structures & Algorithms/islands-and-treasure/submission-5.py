class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        seen = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        time = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                seen.add((r, c))
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(ROWS) and col in range(COLS) and (row, col) not in seen and grid[row][col] == 2147483647:
                        grid[row][col] = time
                        q.append((row, col))
            time += 1
        