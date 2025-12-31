from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            Check 2 strings are valid anagrams
            Args:
                s(str) -> input string1
                t(str) -> another input string
            Return:
                bool -> True if both are same else False

            Complexity:
                Time : O(N)
                Space: O(1)
        """
        # if both strings length not same no need to check further
        if len(s) != len(t):
            return False

        # Given s and t has lower case letters. we will s_char_frequency
        s_char_frequency = [0] * 26
        for character in s:
            index = ord(character) - ord('a')
            s_char_frequency[index] += 1

        # check same character and frequency exists in t
        for character in t:
            index = ord(character) - ord('a')
            if s_char_frequency[index] == 0:
                return False

            s_char_frequency[index] -= 1

        return True

    def isAnagramByPredefinedMethod(self, s: str, t: str) -> bool:
        """
       Check 2 strings are valid anagrams byCounter method in collections
            Args:
                s(str) -> input string1
                t(str) -> another input string
            Return:
                bool -> True if both are same else False

            Complexity:
                Time : O(N)
                Space: O(1)
        """
        return Counter(s) == Counter(t)
