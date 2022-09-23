"""Test Cases for ex05."""

__author__ = "730515426"

from utils import only_evens

def test_only_evens_empty() -> None:
    """Test for empty list"""
    given_list: list(int) = []
    assert only_evens(given_list) == []


def test_only_evens_odds() -> None