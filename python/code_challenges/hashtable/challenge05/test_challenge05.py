# Write your test here
import pytest
from challenge05 import intersection

def test_intersection():
    """Test intersection of arrays with duplicates."""
    arr1 = [1, 2, 2, 1]
    arr2 = [2, 2]
    assert intersection(arr1, arr2) == [2]

def test_no_intersection():
    """Test arrays with no common elements."""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert intersection(arr1, arr2) == []

def test_empty_arrays():
    """Test with both arrays empty."""
    arr1 = []
    arr2 = []
    assert intersection(arr1, arr2) == []

def test_one_empty_array():
    """Test with one array empty."""
    arr1 = [1, 2, 3]
    arr2 = []
    assert intersection(arr1, arr2) == []

def test_same_elements():
    """Test arrays with same elements."""
    arr1 = [1, 1, 1]
    arr2 = [1, 1]
    assert intersection(arr1, arr2) == [1]

def test_multiple_intersections():
    """Test arrays with multiple common elements."""
    arr1 = [1, 2, 3, 4]
    arr2 = [2, 3, 5]
    assert set(intersection(arr1, arr2)) == {2, 3}

if __name__ == "__main__":
    pytest.main()
