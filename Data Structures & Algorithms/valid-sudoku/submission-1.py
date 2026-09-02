class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def check_valid(row):
            seen = set()
            for num in row:
                if num == '.':
                    continue
                if num in seen:
                    # print(num)
                    return False
                seen.add(num)
            return True
        
        # Checking for rows
        for row in board:
            if not check_valid(row):
                # print(f'invalid row - {row}')
                return False
        
        # Checking for cols
        for r in range(ROWS):
            col = []
            for c in range(COLS):
                col.append(board[c][r])
            if not check_valid(col):
                # print('invalid col')
                return False
        
        # Checking for sub-boxes

        for col_start in range(0, COLS, 3):
            for row_start in range(0, ROWS, 3):
                sub_box = []
                for col in range(col_start, col_start + 3):
                    for row in range(row_start, row_start + 3):
                        print(col, row)
                        sub_box.append(board[col][row])
                if not check_valid(sub_box):
                    return False
        
        return True
            
            
