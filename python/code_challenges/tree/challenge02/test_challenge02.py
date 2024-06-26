import pytest
from collections import deque

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p, q):
    """Check if two binary trees are structurally identical and have the same node values."""
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    queue = deque([(p, q)])
    
    while queue:
        node1, node2 = queue.popleft()
        
        if not node1 and not node2:
            continue
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        
        queue.append((node1.left, node2.left))
        queue.append((node1.right, node2.right))
    
    return True

def test_same_trees():
    """Test case for identical trees."""
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    assert is_same_tree(p, q) == True

def test_different_structures():
    """Test case for trees with different structures."""
    p = TreeNode(1)
    p.left = TreeNode(2)

    q = TreeNode(1)
    q.right = TreeNode(2)

    assert is_same_tree(p, q) == False

def test_different_values():
    """Test case for trees with different node values."""
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)

    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)

    assert is_same_tree(p, q) == False

def test_empty_trees():
    """Test case for two empty trees."""
    assert is_same_tree(None, None) == True

def test_one_empty_tree():
    """Test case for one empty tree and one non-empty tree."""
    p = TreeNode(1)
    assert is_same_tree(p, None) == False

def test_single_node_trees():
    """Test case for single node trees with the same value."""
    p = TreeNode(1)
    q = TreeNode(1)
    assert is_same_tree(p, q) == True

def test_single_node_different_values():
    """Test case for single node trees with different values."""
    p = TreeNode(1)
    q = TreeNode(2)
    assert is_same_tree(p, q) == False

if __name__ == "__main__":
    pytest.main()
