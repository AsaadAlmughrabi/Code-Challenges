
# sortedArrayToBST Function

This repository contains Python code that implements a function to convert a sorted array into a height-balanced binary search tree (BST). It includes tests to verify the correctness and functionality of the `sortedArrayToBST` function.



## Overview

The `sortedArrayToBST` function converts a sorted array of integers into a height-balanced BST. A height-balanced BST is defined as a binary tree in which the depth of the two subtrees of every node never differs by more than one.

## Functionality

The `sortedArrayToBST` function works as follows:

- **Input**: Takes a sorted list of integers as input (`nums`).
- **Output**: Returns the root of a height-balanced BST created from the elements in `nums`.

The function utilizes a recursive approach:
- It selects the middle element of the array as the root of the current subtree.
- Recursively constructs the left subtree using the left half of the array.
- Recursively constructs the right subtree using the right half of the array.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the directory:

   ```bash
   cd sortedArrayToBST
   ```

3. Install pytest (if not already installed):

   ```bash
   pip install pytest
   ```

## Usage

To use the `sortedArrayToBST` function in your own project, import it into your Python code:

```python
from sortedArrayToBST import sortedArrayToBST, TreeNode

# Example usage
nums = [-10, -3, 0, 5, 9]
root = sortedArrayToBST(nums)

# Use the root or perform operations on the BST as needed
```

## Tests

Tests are included to validate the correctness of the `sortedArrayToBST` function using `pytest`. To run the tests, use the following command:

```bash
pytest
```

The tests cover various scenarios, including different input arrays and expected outputs to ensure the function works correctly and produces a valid height-balanced BST.

