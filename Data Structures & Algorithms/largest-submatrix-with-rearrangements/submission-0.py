class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        copy = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        
        # Calculate height of every col
        for c in range(COLS):
            total = 0
            for r in range(ROWS):
                if matrix[r][c] == 1:
                    total += 1
                else:
                    total = 0
                copy[r][c] = total
        
        # Sorting each row
        for row in copy:
            row.sort(reverse=True)

        # Calculating the max area
        area = 0

        for r in range(ROWS):
            for c in range(COLS):
                curr_area = copy[r][c] * (c + 1)
                area = max(area, curr_area)
        
        return area
        
