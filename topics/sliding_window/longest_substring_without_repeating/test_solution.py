from topics.sliding_window.longest_substring_without_repeating.solution import Solution


def test_example_1():
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3


def test_example_2():
    sol = Solution()
    assert sol.lengthOfLongestSubstring("bbbbb") == 1


def test_example_3():
    sol = Solution()
    assert sol.lengthOfLongestSubstring("pwwkew") == 3


def test_example_4():
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abba") == 2
