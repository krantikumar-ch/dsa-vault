from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
           Return the elements in spiral order

           Args:
            matrix(List[List[int]) -> input matrix

            Returns:
                List[int] -> spiral order elements in list

            Complexity:
                Time: O(N * M)
                Space: O(1)
        """
        spiral_list = []

        top = left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        while top <= bottom and left <= right:

            # top row
            for i in range(left, right + 1):
                spiral_list.append(matrix[top][i])
            top += 1

            # right column
            for i in range(top, bottom + 1):
                spiral_list.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # Bottom row
                for i in range(right, left-1, -1):
                    spiral_list.append(matrix[bottom][i])

                bottom -= 1

            if left <= right:
                # Left column
                for i in range(bottom, top-1, -1):
                    spiral_list.append(matrix[i][left])

                left += 1

        return spiral_list
