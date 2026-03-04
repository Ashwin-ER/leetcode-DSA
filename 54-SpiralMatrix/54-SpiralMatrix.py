# Last updated: 04/03/2026, 13:36:08
class Solution:
    # Function to return matrix in spiral order
    def spiralOrder(self, matrix):
        # Result list to store output
        result = []

        # Initialize boundaries
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        # Loop while boundaries are valid
        while top <= bottom and left <= right:

            # Traverse top row from left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # Move top boundary down

            # Traverse right column from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Move right boundary left

            # Check for remaining rows
            if top <= bottom:
                # Traverse bottom row from right to left
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # Move bottom boundary up

            # Check for remaining columns
            if left <= right:
                # Traverse left column from bottom to top
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Move left boundary right

        return result