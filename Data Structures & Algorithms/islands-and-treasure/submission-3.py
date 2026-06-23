class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        stack = collections.deque()
        dist = 1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    stack.append((row, col))
        
        while stack:
            for _ in range(len(stack)):
                r, c = stack.popleft()

                for (x, y) in directions:
                    row, col = r + x, c + y
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == 2147483647:
                        grid[row][col] = dist
                        stack.append((row, col))
            dist += 1
        