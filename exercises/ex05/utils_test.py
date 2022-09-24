"""Test Cases for ex05."""

__author__ = "730515426"


from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Test for empty list."""
    given_list: list[int] = []
    assert only_evens(given_list) == []


def test_only_evens_mix1() -> None:
    """Test for list of mixed ints (odds and evens)."""
    given_list: list[int] = [1, 2, 3, 4]
    assert only_evens(given_list) == [2, 4]


def test_only_evens_mix2() -> None:
    """Test for another list of mixed ints (odds and evens)."""
    given_list: list[int] = [44, 66, 33, 55]
    assert only_evens(given_list) == [44, 66]


def test_concat_both_empty() -> None:
    """Test for both lists being empty."""
    ints_one: list[int] = []
    ints_two: list[int] = []
    assert concat(ints_one, ints_two) == []


def test_concat_normal1() -> None:
    """Test for expected list use cases of same lengths."""
    ints_one: list[int] = [1, 2, 3]
    ints_two: list[int] = [4, 5, 6]
    assert concat(ints_one, ints_two) == [1, 2, 3, 4, 5, 6]


def test_concat_normal2() -> None:
    """Test for expected list use cases of differing lengths."""
    ints_one: list[int] = [1, 3, 5]
    ints_two: list[int] = [3, 1]
    assert concat(ints_one, ints_two) == [1, 3, 5, 3, 1]


def test_sub_empty() -> None:
    """Test for empty given list."""
    given_list: list[int] = []
    start: int = 0
    end: int = 5
    assert sub(given_list, start, end) == []


def test_sub_normal1() -> None:
    """Test for an expected list and start/stop case."""
    given_list: list[int] = [1, 2, 3, 4]
    start: int = 0
    end: int = 2
    assert sub(given_list, start, end) == [1, 2]


def test_sub_normal2() -> None:
    """Test for an expected list and start/stop case."""
    given_list: list[int] = [3, 2, 4, 1, 0]
    start: int = 1
    end: int = 3
    assert sub(given_list, start, end) == [2, 4]
