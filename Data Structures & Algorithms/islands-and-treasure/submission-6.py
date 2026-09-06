class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        
        q = deque()
        seen = set()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))
                    # grid[row][col] = -1

        dist = 0
        while q:
            
            for _ in range(len(q)):
                row, col = q.popleft()
                if row not in range(ROWS) or col not in range(COLS) or grid[row][col] == -1 or (row, col) in seen:
                    continue
                grid[row][col] = min(grid[row][col], dist)
                seen.add((row, col))
                q.append((row + 1, col))
                q.append((row - 1, col))
                q.append((row, col + 1))
                q.append((row, col - 1))
            dist += 1
        
        