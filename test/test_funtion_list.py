import pytest
from funtions_list_test import find_max_min, find_average


def test_find_max_min():
    assert find_max_min([35]) == 35
    # assert find_max_min([]) == TypeError(None)


def test_find_average():
    assert find_average([3, 1, 4, 1, 5, 9.5, 0, 2, 6, 5, 3, -3, 5]) == "Середнє значення: " + str(3.1923076923076925)
    # assert find_average([]) == TypeError(None)
