class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dist = 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for x, y in directions:
                    curr_r, curr_c = r + x, c + y
                    if curr_r in range(rows) and curr_c in range(cols) and grid[curr_r][curr_c] == 2147483647:
                        grid[curr_r][curr_c] = dist
                        q.append((curr_r, curr_c))
            dist += 1