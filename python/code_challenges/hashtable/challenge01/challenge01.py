# Write here the code challenge solution
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_pair_with_sum(root, target_sum):
    """
    Find a pair of values in a binary search tree that sum up to a given target sum.
    """
  
    seen_values = set()
 
    def inorder_traversal(node):
        """Perform an in-order traversal of a binary search tree."""
        if not node:
            return False
  
        if inorder_traversal(node.left):
            return True
        
    
        complement = target_sum - node.value
        if complement in seen_values:
            return True
        
        
        seen_values.add(node.value)
        
        return inorder_traversal(node.right)
    
    # Start in-order traversal from the root
    return inorder_traversal(root)


# Constructing the BST:
#        7
#       / \
#      2   9
#     / \   \
#    1   5   14

root = TreeNode(7)
root.left = TreeNode(2)
root.right = TreeNode(9)
root.left.left = TreeNode(1)
root.left.right = TreeNode(5)
root.right.right = TreeNode(14)

# Example 1
print(find_pair_with_sum(root, 3))  # Output: True
print(find_pair_with_sum(root, 4))  # Output: True
print(find_pair_with_sum(root, 10)) # Output: True (5 + 5 or 9 + 1)
print(find_pair_with_sum(root, 20)) # Output: False

