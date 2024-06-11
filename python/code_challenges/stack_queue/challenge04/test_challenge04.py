# Write your test here
import pytest
from challenge04 import reverse_queue,Queue

@pytest.fixture
def sample_queue():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue(1)
    return queue

def test_reverse_queue(sample_queue):
   
    reversed_queue = reverse_queue(sample_queue)
    
    assert reversed_queue.items == [1, 2, 3, 4, 5]

