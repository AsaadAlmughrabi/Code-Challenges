# Write your test here
import pytest
from challenge03 import ListNode

def listnode_to_list(node):
    """Transfer Linked list to array"""
    result = []
    current = node
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_remove_nth_from_end():
    """
    Test function for the remove_nth_from_end method.
    """
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)
    head.append(5)
    
    head = head.remove_nth_from_end(2)
    assert listnode_to_list(head) == [1, 2, 3, 5]
