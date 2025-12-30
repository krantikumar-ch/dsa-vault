

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            calculate the length of longest substriing without repeating characters
            Args: str -> string
            Return: int -> length of longest substring

            Solved using  sliding window + Map data structure

            Complexity:
                Time : O(N)
                Space: O(N)

        """

        left = max_length = 0

        n = len(s)

        index_dict = dict()

        for right, character in enumerate(s):
            # check this is exists in dict and within the range from left to right
            if character in index_dict and index_dict[character] >= left:
                left = index_dict[character] + 1

            index_dict[character] = right

            # calculate maximum length
            max_length = max(max_length, right - left + 1)

        return max_length
