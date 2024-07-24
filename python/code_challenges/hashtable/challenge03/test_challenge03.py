import pytest
from challenge03 import sum_of_unique_elements


def test_sum_of_unique_elements():
    # Test case 1: Array with unique element
    arr1 = [1, 2, 3, 4, 5]
    assert sum_of_unique_elements(arr1) == 15

    arr2 = [1, 2, 3, 2, 1]
    assert sum_of_unique_elements(arr2) == 3

    arr3 = []
    assert sum_of_unique_elements(arr3) == 0

    arr4 = [1, 2, 3, 3, 1]
    assert sum_of_unique_elements(arr4) == 2

    arr5 = [1, 2, 3, 3, 4]
    assert sum_of_unique_elements(arr5) == 7
