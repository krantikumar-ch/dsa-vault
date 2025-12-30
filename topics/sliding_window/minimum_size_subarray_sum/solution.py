import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
            find the minimum size subarray sum
            Args:
                target(int): The minimal sum required for the subarray.
                nums(List[int]): input array
            Returns
                int: minimum sub array size

            Approach:
                sliding window technqiue

            complexity:
                Time : O(N)
                Space: O(1)
        """

        left = current_sum = 0
        min_size = math.inf

        for right, number in enumerate(nums):

            current_sum += number

            while current_sum >= target:
                min_size = min(min_size, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return 0 if min_size == math.inf else min_size
