class MyQueue:
    def __init__(self):
        """Initialize the queue with two stacks."""
        self.stack1 = []
        self.stack2 = []
        self.size = 0

    def push(self, x: int) -> None:
        """Push an element to the back of the queue."""
        self.size += 1
        self.stack1.append(x)
    
    def pop(self) -> int:
        """Remove and return the element from the front of the queue."""
        if self.size == 0:
            return None
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        self.size -= 1
        return self.stack2.pop()
    
    def peek(self) -> int:
        """Return the element at the front of the queue without removing it."""
        if self.size == 0:
            return None
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    
    def empty(self) -> bool:
        """Check if the queue is empty."""
        return self.size == 0

# Example usage:
myQueue = MyQueue()
myQueue.push(1)  # queue is: [1]
myQueue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
print(myQueue.peek())  # returns 1
print(myQueue.pop())   # returns 1, queue is [2]
print(myQueue.empty()) # returns False
