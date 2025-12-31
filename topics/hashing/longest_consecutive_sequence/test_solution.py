from topics.hashing.longest_consecutive_sequence.solution import Solution


def test_example_1():
    sol = Solution()
    assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4


def test_example_2():
    sol = Solution()
    assert sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_example_3():
    sol = Solution()
    assert sol.longestConsecutive([1, 0, 1, 2]) == 3
