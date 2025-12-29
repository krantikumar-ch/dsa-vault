from .solution import Solution


def test_example_1():
    sol = Solution()
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_example_2():
    sol = Solution()
    assert sol.maxArea([1, 1]) == 1
