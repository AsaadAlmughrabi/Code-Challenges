# Maximum Value in Binary Tree

This project demonstrates how to find the maximum value in a binary tree using inorder traversal. The solution is implemented in Python and includes functionality for constructing a binary tree, performing inorder traversal, and finding the maximum value. Additionally, test cases are provided using `pytest`.

## Problem Domain

Given the root of a binary tree, the goal is to find the maximum value present in the tree using inorder traversal.

## Algorithms

### Tree Construction
The binary tree is constructed by inserting elements in level order (breadth-first).

### Inorder Traversal
Inorder traversal visits nodes in the following order: 
1. Visit the left subtree.
2. Visit the root node.
3. Visit the right subtree.

During this traversal, the maximum value encountered is tracked and returned.



# Example usage:
```
tree_values = [1000, 500, 2000, 250, 600, 12000]
root = insert_level_order(tree_values, None, 0, len(tree_values))
max_value = find_max_in_tree(root)
Print max_value
```
