from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
         Find number of subarrays whose sum is equal to K

            Args:
                nums(List[int]) -> Given input array
                k(int) -> target sum

            Returns:
                int -> total number f subarrays whose sum equals to k

            Approach
                prefix technique + HashMap

                sum(i, j) = k
                prefix[j] - prefix[i-1] = k
                prefix[j] - k = prefix[i-1]

            Complexity:
                Time: O(N)
                Space: O(N)    

        """

        count = 0
        prefix_freq_map = defaultdict(int)
        prefix_freq_map[0] = 1
        prefix_sum = 0
        for number in nums:
            prefix_sum += number

            if prefix_sum - k in prefix_freq_map:
                count += prefix_freq_map[prefix_sum - k]

            prefix_freq_map[prefix_sum] += 1

        return count
