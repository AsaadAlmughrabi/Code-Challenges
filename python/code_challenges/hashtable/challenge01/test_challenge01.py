# Write your test here
import pytest
from challenge01 import find_pair_with_sum, TreeNode

def test_empty_tree():
    assert not find_pair_with_sum(None, 10)

def test_no_pair_summing_to_target():
    root = TreeNode(5)
    assert not find_pair_with_sum(root, 10)

def test_pair_summing_to_target():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    assert find_pair_with_sum(root, 10)

def test_multiple_pairs_summing_to_target():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    assert find_pair_with_sum(root, 10)
    assert find_pair_with_sum(root, 7)

if __name__ == '__main__':
    pytest.main()
    