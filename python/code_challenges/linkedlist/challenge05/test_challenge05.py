# Write your test here
import pytest
from challenge05 import ListNode

@pytest.fixture
def sample_linked_list():
    # Create a sample linked list: 1 -> 2 -> 4 -> 5
    head = ListNode(1)
    head.append(2)
    head.append(4)
    head.append(5)
    return head

def test_insert_after(sample_linked_list):
    # Insert a new node with value 3 after the node with value 2
    sample_linked_list.insert_after(2, 3)
    
    # Expected linked list after insertion: 1 -> 2 -> 3 -> 4 -> 5
    current = sample_linked_list
    values = []
    while current:
        values.append(current.val)
        current = current.next
    assert values == [1, 2, 3, 4, 5]

    # Test inserting after the last node
    sample_linked_list.insert_after(5, 6)

    # Expected linked list after insertion: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    current = sample_linked_list
    values = []
    while current:
        values.append(current.val)
        current = current.next
    assert values == [1, 2, 3, 4, 5, 6]

    # Test inserting after a node that doesn't exist
    with pytest.raises(ValueError):
        sample_linked_list.insert_after(7, 8)
