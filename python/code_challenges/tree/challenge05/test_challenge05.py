# Write your test here
# Write your test here
import pytest
from challenge05 import TreeNode, max_height

def test_empty_tree():
    root = None
    assert max_height(root) == 0

def test_single_node_tree():
    root = TreeNode(5)
    assert max_height(root) == 1

def test_balanced_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert max_height(root) == 3

def test_unbalanced_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert max_height(root) == 3
