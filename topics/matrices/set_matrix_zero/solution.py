from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
            Update the given matrix entire row and column is 0 if an element is 0
            Args:
                matrix(List[list[int]]) -> input matrix
            Returns:
                None -> in place changes

            Complexity:
                Time: O(N * M) N is row length and M is column length
                Space: O(1)
        """
        n = len(matrix)
        m = len(matrix[0])
        is_col = False

        for row_idx in range(n):
            # Since first cell for both first row and first column is the same
            # i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix
            if matrix[row_idx][0] == 0:
                is_col = True

            for col_idx in range(1, m):

                # update row first cell, column first cell to 0
                if matrix[row_idx][col_idx] == 0:
                    matrix[0][col_idx] = 0
                    matrix[row_idx][0] = 0

        # Iterate once again update the elements
        for row_idx in range(1, n):
            for col_idx in range(1, m):
                if matrix[row_idx][0] == 0 or matrix[0][col_idx] == 0:
                    matrix[row_idx][col_idx] = 0

        # if the first row needs to be set to 0 as well
        if matrix[0][0] == 0:
            for col_idx in range(m):
                matrix[0][col_idx] = 0

        # if the first column needs to set to 0 as well

        if is_col:
            for row_idx in range(n):
                matrix[row_idx][0] = 0
