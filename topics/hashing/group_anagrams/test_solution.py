import pytest
from typing import List
from topics.hashing.group_anagrams.solution import Solution


# --- Test Cases ---


@pytest.mark.parametrize("input_strs, expected_output", [  # pyright: ignore[reportUndefinedVariable]
    # Case 1: Standard example from LeetCode
    (
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    ),
    # Case 2: Empty list
    (
        [],
        []
    ),
    # Case 3: Single string
    (
        ["a"],
        [["a"]]
    ),
    # Case 4: Empty string
    (
        [""],
        [[""]]
    ),
    # Case 5: Multiple empty strings (they are anagrams of each other)
    (
        ["", "", ""],
        [["", "", ""]]
    ),
    # Case 6: No anagrams (all distinct character sets)
    (
        ["cat", "dog", "bird"],
        [["cat"], ["dog"], ["bird"]]
    ),
    # Case 7: All strings are anagrams
    (
        ["abc", "bca", "cab", "cba"],
        [["abc", "bca", "cab", "cba"]]
    ),
    # Case 8: Strings with overlapping characters but different counts (not anagrams)
    (
        ["ddg", "dgg"],
        [["ddg"], ["dgg"]]
    ),
])
def test_group_anagrams(input_strs, expected_output):
    sol = Solution()
    actual_output = sol.groupAnagrams(input_strs)

    # Normalize both expected and actual results before comparing
    assert normalize_result(actual_output) == normalize_result(expected_output)

# --- Performance / Edge Case Check (Optional) ---


def test_large_input():
    """
    Simple smoke test for a larger input to ensure no recursion/depth errors.
    """
    sol = Solution()
    # Create 1000 "abc" and 1000 "def"
    input_strs = ["abc"] * 1000 + ["def"] * 1000
    result = sol.groupAnagrams(input_strs)

    # We expect exactly 2 groups
    assert len(result) == 2

    # Verify groupings
    normalized = normalize_result(result)
    assert len(normalized[0]) == 1000  # group "abc"
    assert len(normalized[1]) == 1000  # group "def"


# --- Helper for Assertions ---
def normalize_result(result: List[List[str]]) -> List[List[str]]:
    """
    Normalizes the result for comparison.
    1. Sorts strings within each inner list.
    2. Sorts the outer list based on the first element of the inner lists.
    """
    # Sort strings inside each group
    sorted_inner = [sorted(group) for group in result]
    # Sort the groups themselves to ensure order independence
    return sorted(sorted_inner)
