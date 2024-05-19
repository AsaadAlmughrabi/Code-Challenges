from challenge02 import ListNode


def test_find_middle():
    """
    Test function for the find_middle method.
    """

    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)
    head.append(5)

    middle_nodes = head.find_middle()

    assert middle_nodes == [3, 4, 5]
