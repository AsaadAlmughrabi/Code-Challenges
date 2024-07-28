import pytest
from challenge04 import reorder_people_by_heights


def test_reorder_people_by_heights():
  
    people = ["Alice", "Bob", "Charlie"]
    heights = [165, 180, 175]
    assert reorder_people_by_heights(people, heights) == ["Bob", "Charlie", "Alice"]

    people = ["Alice"]
    heights = [165]
    assert reorder_people_by_heights(people, heights) == ["Alice"]

    people = []
    heights = []
    assert reorder_people_by_heights(people, heights) == []

    people = ["Alice", "Bob", "Charlie", "David"]
    heights = [160, 180, 175, 170]
    assert reorder_people_by_heights(people, heights) == [
        "Bob",
        "Charlie",
        "David",
        "Alice",
    ]


if __name__ == "__main__":
    pytest.main()
