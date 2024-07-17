# Write your test here
import pytest
from challenge04 import TreeNode, find_max_in_tree, insert_level_order

def test_find_max_in_tree():
    """function to test the max of the tree"""
    # Test case 1: Example tree provided in the problem statement
    tree_values = [1000, 500, 2000, 250, 600, 12000]
    root = insert_level_order(tree_values, None, 0, len(tree_values))
    assert find_max_in_tree(root) == 12000

    # Test case 2: Single node tree
    tree_values = [42]
    root = insert_level_order(tree_values, None, 0, len(tree_values))
    assert find_max_in_tree(root) == 42


    tree_values = [1, 1, 1, 1, 1, 1]
    root = insert_level_order(tree_values, None, 0, len(tree_values))
    assert find_max_in_tree(root) == 1

    tree_values = [3, -2, 9, -5, 0, -1]
    root = insert_level_order(tree_values, None, 0, len(tree_values))
    assert find_max_in_tree(root) == 9

  
    tree_values = [-10, -20, -30, -40, -50]
    root = insert_level_order(tree_values, None, 0, len(tree_values))
    assert find_max_in_tree(root) == -10


    assert find_max_in_tree(None) is None

if __name__ == "__main__":
    pytest.main()
