# Write your test here
import pytest
from challenge01 import TreeNode, buildTree, print_level_order


def test_TreeNode():
    node = TreeNode(1)
    assert node.val == 1
    assert node.left is None
    assert node.right is None

def test_buildTree():
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    root1 = buildTree(preorder1, inorder1)
    assert print_level_order(root1) == [3, 9, 20, None, None, 15, 7]
    
    preorder2 = [-1]
    inorder2 = [-1]
    root2 = buildTree(preorder2, inorder2)
    assert print_level_order(root2) == [-1]

def test_print_level_order():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert print_level_order(root) == [3, 9, 20, None, None, 15, 7]

    root = TreeNode(-1)
    assert print_level_order(root) == [-1]

    assert print_level_order(None) == []

if __name__ == "__main__":
    pytest.main()