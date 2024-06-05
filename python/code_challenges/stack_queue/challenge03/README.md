# Stack with Middle Element Deletion

This Python code provides a simple implementation of a stack data structure with the capability to delete the middle element efficiently. It consists of two classes:

1. **Node:** This class represents a single node in the linked list-based implementation of the stack. Each node stores data and a reference to the next node in the sequence.

2. **Stack:** This class represents the stack data structure. It supports typical stack operations such as push (to add an element), pop (to remove and return the top element), and isEmpty (to check if the stack is empty). Additionally, it provides a method `delete_middle` to remove the middle element from the stack.

## Usage

1. Clone the repository or copy the code into your project.
2. Import the `Stack` class into your Python code.
3. Create a `Stack` object.
4. Push elements onto the stack using the `push` method.
5. Optionally, delete the middle element using the `delete_middle` method.
6. Pop elements from the stack using the `pop` method as needed.

```python
# Example Usage

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print("Original stack:")
print(stack.display())

stack.delete_middle()

print("Stack after deleting middle element:")
print(stack.display())
