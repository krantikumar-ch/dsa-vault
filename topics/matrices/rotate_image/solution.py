from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the given matrix into 90 degrees
        Args:
            matrix(List[List[int]]) -> N * N matrix

        Returns: 
            None -> rotating in given matrix

        Approach
            Transpose (rows to colums and columns to rows)
            swap columns from left to right

        Complexity
            Time : O(N^2)
            Space: O(1)


        """
        n = len(matrix)
        # swap rows into columns and columns into rows
        for row_idx, row in enumerate(matrix):
            # col_idx = row_idx + 1
            for col_idx in range(row_idx + 1, n):
                matrix[row_idx][col_idx], matrix[col_idx][row_idx] = matrix[col_idx][row_idx], matrix[row_idx][col_idx]
                col_idx += 1

        # swap the columns from left to right
        for row in matrix:
            left = 0
            right = n-1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1
