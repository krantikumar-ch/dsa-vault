from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
            Find the container with most water
            Args:
                height: List[int] -> List of Integers
            Return:
                int -> most water

            Complexity:
            Time : O(N)
            Space: O(1) 
        """

        max_water = 0
        left, right = 0, len(height) - 1

        while left <= right:
            h_left = height[left]
            h_right = height[right]
            current_height = h_left if h_right > h_left else h_right

            current_water = (right - left) * current_height
            max_water = max(current_water, max_water)

            if h_left > h_right:
                right -= 1
            else:
                left += 1

        return max_water
