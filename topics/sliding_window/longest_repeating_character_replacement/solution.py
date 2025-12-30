from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            Finds the length of the longest substring containing the same letter 
        after replacing at most k characters.

           Args:
            s (str): The input string.
            k (int): The maximum number of allowed character replacements.

        Returns:
            int: The maximum length of the uniform substring.
            Args:
                s: str 
                k: int
            returns
                int: longest substring length

            Approach:
                sliding window technique + map data structure
            Hint:
                window size - most frequent char <= K

            complexity:
                Time: O(N)
                Space: O(1) 
        """

        max_frequency = left = 0
        frequency_dict = defaultdict(int)

        for right, character in enumerate(s):
            frequency_dict[character] += 1

            # Optimization: We only care about the historical max frequency
            # to see if we can expand the best window found so far.
            max_frequency = max(max_frequency, frequency_dict[character])

            window_size = right - left + 1

            # violated the condition of k
            if (window_size - max_frequency) > k:
                frequency_dict[s[left]] -= 1
                left += 1

        # The window size at the end is effectively the max length found
        return len(s) - left
