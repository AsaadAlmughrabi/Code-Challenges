class Stack:
    """A class representing a stack data structure."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

class Queue:
    """A class representing a queue data structure."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

def reverse_queue(queue):
    """Reverse the given queue using a stack."""
    stack = Stack()

    print("Original Queue:", queue.items)

    while not queue.is_empty():
        stack.push(queue.dequeue())

    reversed_queue = Queue()

    while not stack.is_empty():
        reversed_queue.enqueue(stack.pop())

    print("Reversed Queue:", reversed_queue.items)

    return reversed_queue

original_queue = Queue()
original_queue.enqueue(5)
original_queue.enqueue(4)
original_queue.enqueue(3)
original_queue.enqueue(2)
original_queue.enqueue(1)

reversed_queue = reverse_queue(original_queue)
