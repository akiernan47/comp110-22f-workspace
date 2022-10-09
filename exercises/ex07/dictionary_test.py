"""Tests for Dictionary Functions."""

__author__ = "730515426"


import pytest
from dictionary import invert, count, favorite_color


def test_invert_empty() -> None:
    """Test for invert empty dictionary."""
    given_dict: dict[str, str] = {}
    assert invert(given_dict) == {}


def test_invert_use1() -> None:
    """Test for invert use case."""
    given_dict: dict[str, str] = {"UNC": "Dukie"}
    assert invert(given_dict) == {"Dukie": "UNC"}


def test_invert_use2() -> None:
    """Test for invert use case."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_count_empty() -> None:
    """Test for count empty list."""
    given_list: list[str] = []
    assert count(given_list) == {}


def test_count_use1() -> None:
    """Test for count use case."""
    given_list: list[str] = ["1", "1", "1", "2", "2", "3"]
    assert count(given_list) == {'1': 3, '2': 2, '3': 1}


def test_count_use2() -> None:
    """Test for count use case."""
    given_list: list[str] = ["Duck", "Duck", "Goose"]
    assert count(given_list) == {'Duck': 2, 'Goose': 1}


def favorite_color_empty() -> None:
    """Test for favorite_color empty dictionary."""
    given_dict: dict[str, str] = {}
    assert favorite_color(given_dict) == ""


def favorite_color_use1() -> None:
    """Test for favorite_color use case."""
    given_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(given_dict) == "blue"


def favorite_color_use2() -> None:
    """Test for favorite_color use case."""
    given_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue"}
    assert favorite_color(given_dict) == "yellow"
