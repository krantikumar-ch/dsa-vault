from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            Find longest consecutive sequence in the given array
            Args:
                nums(List[int]) -> array to analyze

            Returns:
                int -> length of longest consecutive element

            Approach: HashSet

            Complexity:
                Time : O(N)
                Space: O(N)
        """
        unique_set = set(nums)
        max_length = 0

        for current_num in unique_set:

            # previous value is there so we will not check.
            # This condition will avoid redundant iterations
            if current_num - 1 in unique_set:
                continue

            current_max = 1
            while current_num + 1 in unique_set:
                current_num += 1
                current_max += 1

            max_length = max(max_length, current_max)

        return max_length
