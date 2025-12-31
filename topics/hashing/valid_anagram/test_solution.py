from topics.hashing.valid_anagram.solution import Solution


def test_example_1():
    sol = Solution()
    assert sol.isAnagram("anagram", "nagaram") == True


def test_example_2():
    sol = Solution()
    assert sol.isAnagram("rat", "car") == False


def test_example_3():
    sol = Solution()
    assert sol.isAnagramByPredefinedMethod("rat", "car") == False


def test_example_4():
    sol = Solution()
    assert sol.isAnagramByPredefinedMethod("rat", "car") == False
