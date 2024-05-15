# Write here the code challenge solution
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def deleteNode(node):
    if(node is None):
        return False
    node.val = node.next.val
    temp = node.next
    node.next = temp.next
    temp.next = None
