from collections import defaultdict
from typing import List


class Solution:

    def getSortedString(self, s: str) -> str:
        """
            sort the string
            Args:
                s(str) -> input string to sort
            Returns:
                str -> sorted string

            Complexity:
                Time: O(N)
                Space: O(1)
        """
        char_frequency = [0] * 26
        for character in s:
            index = ord(character) - ord('a')
            char_frequency[index] += 1

        anagram_key = ""
        for index, number in enumerate(char_frequency):

            if number != 0:
                character = chr(97+index)
                anagram_key += character * number

        return anagram_key

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            find anagrams in given list group them together
            Args:
                strs(List[str]) -> List of strings

            Returns:
                List[List[str]]: list of grouped anagrams

            complexity:
                Time: O(N * K)
                Space: O(N * K)

                N = length of the List
                W = length of Each word

        """

        word_dict = defaultdict(list)

        for word in strs:
            sorted_word = self.getSortedString(word)
            word_dict[sorted_word].append(word)

        return list(word_dict.values())
