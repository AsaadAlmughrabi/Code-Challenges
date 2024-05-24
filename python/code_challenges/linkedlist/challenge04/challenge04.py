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

    def reverse_linked_list(self):
        """
        Reverse the linked list starting from the current node and return the new head.
        """
        prev = None
        curr = self
        
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev

def main():
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> None
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)

    print("Original linked list:")
    head.print_linked_list()

    
    new_head = head.reverse_linked_list()

    print("Reversed linked list:")
    new_head.print_linked_list()

if __name__ == "__main__":
    main()
