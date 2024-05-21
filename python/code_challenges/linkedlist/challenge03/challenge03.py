# Write here the code challenge solution
class ListNode:
    def __init__(self, val):
        """
        Initialize a ListNode with the given value.
        """
        self.val = val
        self.next = None

    def append(self, value):
        """
        Append a new node with the given value to the end of the linked list.
        """
        node = ListNode(value)  
        
        if self.next is None:
            self.next = node
        else:  
            current = self
            while current.next is not None:
                current = current.next
            current.next = node

    def print_linked_list(self):
        """
        Print the values of nodes in the linked list starting from the current node.
        """
        current = self
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def remove_nth_from_end(self, n):
        """
        Remove the nth node from the end of the list and return the head of the list.
        """
        dummy = ListNode(0)
        dummy.next = self
        first = dummy
        second = dummy
        
        # Move first ahead by n+1 steps
        for _ in range(n + 1):
            first = first.next
        
        # Move both first and second until first reaches the end
        while first:
            first = first.next
            second = second.next
        
        # Remove the nth node from end
        second.next = second.next.next
        
        return dummy.next

if __name__ == "__main__":
    
    head = ListNode(1)
    head.append(2)
    # head.append(3)
    # head.append(4)
    # head.append(5)
  
    
    print("Original linked list:")
    head.print_linked_list()

    # Remove the 2nd node from the end
    head = head.remove_nth_from_end(1)
    
    print("Linked list after removing the 2nd node from the end:")
    head.print_linked_list()
