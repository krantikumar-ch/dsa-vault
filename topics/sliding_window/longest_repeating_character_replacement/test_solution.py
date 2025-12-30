

from topics.sliding_window.longest_repeating_character_replacement.solution import Solution


def test_example_1():
    sol = Solution()
    assert sol.characterReplacement("ABAB", 2) == 4


def test_example_2():
    sol = Solution()
    assert sol.characterReplacement("AABABBA", 1) == 4
