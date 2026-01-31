class Solution(object):
    def setZeroes(self, matrix):
        # Get dimensions of matrix
        m = len(matrix)
        n = len(matrix[0])

        # Flag to track if first row should be zeroed
        first_row_zero = False
        # Flag to track if first column should be zeroed
        first_col_zero = False

        # Check if first row has any zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if first column has any zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Use first row/column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to zero based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

