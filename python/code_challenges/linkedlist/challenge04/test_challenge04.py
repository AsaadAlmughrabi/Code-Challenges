# Write your test here
import pytest
from challenge04 import ListNode

def test_reverse_linked_list():
    """ test Reversing the linked list"""
   
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)

   
    reversed_head = head.reverse_linked_list()


    reversed_values = []
    current = reversed_head
    while current is not None:
        reversed_values.append(current.val)
        current = current.next

    
    expected_values = [4, 3, 2, 1]

    assert reversed_values == expected_values, f"Expected {expected_values}, but got {reversed_values}"

