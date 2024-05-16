class ListNode:
    def __init__(self, val):
        """
        Initialize a ListNode with the given value.
        """
        self.val = val
        self.next = None

def deleteNode(node):
    """
    Delete the given node from a singly linked list.
    
    Args:
        node: ListNode, the node to be deleted.
    
    Returns:
        bool: True if the node is deleted successfully, False otherwise.
    """
    if node is None:
        return False
    
    node.val = node.next.val
    temp = node.next
    node.next = temp.next
    temp.next = None
    
    return True

def print_linked_list(head):
    """
    Print the values of nodes in the linked list starting from the given head.
    """
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Test case
if __name__ == "__main__":
    # Create a linked list
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    
    # Print the original linked list
    print("Original linked list:")
    print_linked_list(head)
    
    # Delete a node
    deleteNode(head.next)
    
    # Print the linked list after deletion
    print("\nLinked list after deletion:")
    print_linked_list(head)
