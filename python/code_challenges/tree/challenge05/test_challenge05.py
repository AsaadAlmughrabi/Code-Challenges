import pytest
from challenge05 import TreeNode, max_height

def test_empty_tree():
    assert max_height(None) == -1

def test_single_node_tree():
    root = TreeNode(1)
    assert max_height(root) == 0

def test_balanced_tree():
    root = TreeNode(10)
    root.left = TreeNode(20)
    root.right = TreeNode(30)
    root.left.left = TreeNode(40)
    root.left.right = TreeNode(28)
    root.right.right = TreeNode(50)
    root.left.right.left = TreeNode(29)
    assert max_height(root) == 3

def test_unbalanced_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert max_height(root) == 2

def test_tree_with_one_child():
    root = TreeNode(10)
    root.left = TreeNode(20)
    assert max_height(root) == 1

def test_tree_with_no_children():
    root = TreeNode(10)
    assert max_height(root) == 0