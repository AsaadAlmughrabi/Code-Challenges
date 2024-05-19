import math

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

    def find_middle(self):
        """
        Find the middle node(s) of the linked list and return them.
        """
        arr = []
        current = self
        while current:
            arr.append(current.val)
            current = current.next

        middle_nodes = []
        if len(arr) % 2 == 0:
            
            for i in range(len(arr) // 2, len(arr)):
                middle_nodes.append(arr[i])
        else:
            
            for i in range(math.ceil(len(arr) // 2), len(arr)):
                middle_nodes.append(arr[i])

        return middle_nodes

if __name__ == "__main__":
    
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)
    head.append(5)
    head.append(6)
    head.append(7)
    head.append(8)
   

    middle_nodes = head.find_middle()
    print("Middle node(s):", middle_nodes)

    
    head.print_linked_list()
