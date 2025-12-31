

from topics.hashing.subarray_sum_equals_k.solution import Solution


def test_example_1():
    sol = Solution()
    assert sol.subarraySum([1, 1, 1], 2) == 2


def test_example_2():
    sol = Solution()
    assert sol.subarraySum([1, 2, 3], 3) == 2


def test_example_3():
    sol = Solution()
    assert sol.subarraySum([1], 0) == 0


def test_example_4():
    sol = Solution()
    assert sol.subarraySum([1, -1, 0], 0) == 3
