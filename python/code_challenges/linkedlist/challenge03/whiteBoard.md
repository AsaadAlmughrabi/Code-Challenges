# Linked List Nth Node Removal

This repository contains a Python implementation to remove the nth node from the end of a singly linked list. 

## Overview

Given a linked list, the goal is to remove the nth node from the end and return the head of the modified list.

## Implementation

The solution involves creating a `ListNode` class that represents each node in the linked list and includes methods for appending nodes, printing the linked list, and removing the nth node from the end.

### ListNode Class

- **`__init__(self, val)`**: Initializes a `ListNode` with the given value.
- **`append(self, value)`**: Appends a new node with the given value to the end of the linked list.
- **`print_linked_list(self)`**: Prints the values of nodes in the linked list starting from the current node.
- **`remove_nth_from_end(self, n)`**: Removes the nth node from the end of the list and returns the head of the modified list.

### Algorithm for Removing Nth Node from End

1. Create a dummy node and set its next to the head of the linked list.
2. Initialize two pointers, both pointing to the dummy node.
3. Move the first pointer `n+1` steps ahead to create a gap of `n` nodes between the first and second pointers.
4. Move both pointers one step at a time until the first pointer reaches the end of the list.
5. Change the next pointer of the second pointer to skip the nth node from the end.
6. Return the next node of the dummy node, which is the new head of the modified list.

### Time and Space Complexity

- **Time Complexity**: `O(L)`, where `L` is the number of nodes in the linked list. This is because we make a single pass through the list.
- **Space Complexity**: `O(1)`, as we only use a constant amount of extra space.


