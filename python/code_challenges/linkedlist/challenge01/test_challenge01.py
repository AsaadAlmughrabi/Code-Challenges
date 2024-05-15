from challenge01 import ListNode, deleteNode

# Define the test function
def test_delete_node():
    
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)


    deleteNode(head.next)

    
    assert head.val == 1
    assert head.next.val == 3
    assert head.next.next is None

    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)


    deleteNode(head.next.next)

    assert head.val == 4
    assert head.next.val == 5
    assert head.next.next.val == 9
    assert head.next.next.next is None