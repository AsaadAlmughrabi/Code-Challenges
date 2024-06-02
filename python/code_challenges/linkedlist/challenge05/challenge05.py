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
    
    def insert_after(self, before, after):
        """
        Insert a new node with the value 'after' after the node with the value 'before'.
        """
        current = self
        while current:
            if current.val == before:
                new_node = ListNode(after)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise ValueError("Node with value '{}' not found".format(before))
        


def main():
    # Create a linked list
    head = ListNode(1)
    head.append(2)
    head.append(4)
    head.append(5)

    # Print the original linked list
    print("Original linked list:")
    head.print_linked_list()

    # Insert a new node with value 3 after the node with value 2
    head.insert_after(2, 3)

    # Print the linked list after insertion
    print("Linked list after insertion:")
    head.print_linked_list()

if __name__ == "__main__":
    main()
