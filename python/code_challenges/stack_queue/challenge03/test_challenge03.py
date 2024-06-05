import pytest
from challenge03 import Stack

@pytest.fixture
def stack():
    """
    Fixture to set up a stack with some initial elements for testing.
    """
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    return stack

def test_delete_middle(stack):
    """
    Test whether the delete_middle method correctly removes the middle element from the stack.
    """
    stack.delete_middle()
    assert stack.display() == [1, 2, 4, 5]

def test_delete_middle_empty_stack():
    """
    Test whether delete_middle returns None when attempting to delete from an empty stack.
    """
    stack = Stack()
    result = stack.delete_middle()
    assert result is None

def test_delete_middle_single_element():
    """
    Test whether delete_middle correctly handles the case when there's only one element in the stack.
    """
    stack = Stack()
    stack.push(1)
  
    result = stack.delete_middle()
    assert result == 1
    assert stack.is_empty()
