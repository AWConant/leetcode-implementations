class Solution:
    # binary searches a row of a 2D matrix, starting at `col_min`
    def horizontal_binary_search(self, matrix, target, row, col_min):
        lo = col_min
        hi = len(matrix[0])-1
        while hi >= lo:
            mid = (lo + hi)//2
            if matrix[row][mid] < target:
                lo = mid + 1
            elif matrix[row][mid] > target:
                hi = mid - 1
            else: # found target
                return True
        
        return False

    # binary searches a column of a 2D matrix, from 0 up to `row_max`
    def vertical_binary_search(self, matrix, target, row_max, col):
        lo = 0
        hi = row_max
        while hi >= lo:
            mid = (lo + hi)//2
            if matrix[mid][col] < target:
                lo = mid + 1
            elif matrix[mid][col] > target:
                hi = mid - 1
            else: # found target
                return True
        
        return False

    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        # iterate over matrix diagonals starting in bottom left.
        row_descending = range(len(matrix)-1, -1, -1)
        col_ascending = range(len(matrix[0]))
        for row, col in zip(row_descending, col_ascending):
            vertical_found = self.vertical_binary_search(matrix, target, row, col)
            horizontal_found = self.horizontal_binary_search(matrix, target, row, col)
            if vertical_found or horizontal_found:
                return True
        
        return False