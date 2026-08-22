class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        selected_row = []

        for row in matrix:
            if target <= row[-1]:
                selected_row = row
                if target == row[-1]:
                    return True
                break
        
        if not selected_row:
            return False

        low, high = 0, len(selected_row) - 1
        while low <= high:
            mid = (low + high) // 2
            if target < selected_row[mid]:
                high = mid - 1
            elif target > selected_row[mid]:
                low = mid + 1
            else:
                return True
        return False