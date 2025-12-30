from topics.sliding_window.minimum_size_subarray_sum.solution import Solution


def test_example_1():
    sol = Solution()
    assert sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2


def test_example_2():
    sol = Solution()
    assert sol.minSubArrayLen(4, [1, 4, 4]) == 1


def test_example_3():
    sol = Solution()
    assert sol.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
