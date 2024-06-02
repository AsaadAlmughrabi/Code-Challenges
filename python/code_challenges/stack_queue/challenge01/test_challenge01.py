import pytest
from challenge01 import MyQueue  # ensure the MyQueue class is in the file challenge01.py

@pytest.fixture
def queue():
    """Fixture to create a new MyQueue instance for each test."""
    return MyQueue()

def test_push(queue):
    """Test the push operation of MyQueue."""
    queue.push(1)
    assert queue.size == 1
    queue.push(2)
    assert queue.size == 2

def test_pop(queue):
    """Test the pop operation of MyQueue."""
    queue.push(1)
    queue.push(2)
    assert queue.pop() == 1
    assert queue.size == 1
    assert queue.pop() == 2
    assert queue.size == 0
    assert queue.pop() is None

def test_peek(queue):
    """Test the peek operation of MyQueue."""
    assert queue.peek() is None
    queue.push(1)
    assert queue.peek() == 1
    queue.push(2)
    assert queue.peek() == 1
    queue.pop()
    assert queue.peek() == 2

def test_empty(queue):
    """Test the empty check of MyQueue."""
    assert queue.empty() is True
    queue.push(1)
    assert queue.empty() is False
    queue.pop()
    assert queue.empty() is True
