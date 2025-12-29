from .solution import Solution


def test_example_1():
    sol = Solution()
    assert sol.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]


def test_example_2():
    sol = Solution()
    assert sol.threeSum([0, 1, 1]) == []


def test_example_3():
    sol = Solution()
    assert sol.threeSum([0, 0, 0]) == [[0, 0, 0]]
