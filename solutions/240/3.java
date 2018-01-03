class Solution {
    // binary searches a row of a 2D matrix, starting at `col_min`
    private boolean horizontalBinarySearch(int[][] matrix, int target, int row, int colMin) {
        int lo = colMin;
        int hi = matrix[0].length-1;
        while (hi >= lo) {
            int mid = (lo + hi)/2;
            if (matrix[row][mid] < target) {
                lo = mid + 1;
            } else if (matrix[row][mid] > target) {
                hi = mid - 1;
            } else { // found target
                return true;
            }
        }

        return false;
    }

    // binary searches a column of a 2D matrix, from 0 up to `row_max`
    private boolean verticalBinarySearch(int[][] matrix, int target, int rowMax, int col) {
        int lo = 0;
        int hi = rowMax;
        while (hi >= lo) {
            int mid = (lo + hi)/2;
            if (matrix[mid][col] < target) {
                lo = mid + 1;
            } else if (matrix[mid][col] > target) {
                hi = mid - 1;
            } else { // found target
                return true;
            }
        }
        
        return false;
    }

    public boolean searchMatrix(int[][] matrix, int target) {
        // an empty matrix obviously does not contain `target`
        if (matrix == null) {
            return false;
        }

        // iterate over matrix diagonals starting in bottom left.
        int row = matrix.length-1;
        int col = 0;
        while (row >= 0 && col < matrix[0].length) {
            boolean verticalFound = verticalBinarySearch(matrix, target, row, col);
            boolean horizontalFound = horizontalBinarySearch(matrix, target, row, col);
            if (verticalFound || horizontalFound) {
                return true;
            }
            row--;
            col++;
        }
        
        return false; 
    }
}