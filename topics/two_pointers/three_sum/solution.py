from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            Find all triples in the given array whose sum is equal to 0
            Args:
                A 1-indexed, list of integers
            Returns:
                A list 2-indexed containing list of integers [[number1, number2, number3]]

            Time: O(N^2)
            Space: O(1) (or O(N) depending on sort implementation), excluding output storage.
        """

        result = []
        n = len(nums)

        # sort the array
        nums.sort()

        for index in range(n):

            # Optimization: If the current number is positive, we can't sum to 0
            # because the array is sorted (remaining numbers are also positive).
            if nums[index] > 0:
                break

            # Skip duplicates for the pivot element
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            left, right = index + 1, n - 1

            while left < right:
                three_sum = nums[index] + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for the second element (left pointer)
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result
