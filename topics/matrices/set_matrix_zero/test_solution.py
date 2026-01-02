from .solution import Solution

sol = Solution()


def test_example_1():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol.setZeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]


def test_example_2():
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol.setZeroes(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
