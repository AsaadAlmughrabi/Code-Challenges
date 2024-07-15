class TreeNode:
    """
    Definition for a binary tree node.
    
    Attributes:
        val (int): Value of the node.
        left (TreeNode): Reference to the left child node.
        right (TreeNode): Reference to the right child node.
    """
    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a TreeNode with given value and optional left and right children.
        
        Args:
            val (int): Value of the node (default is 0).
            left (TreeNode): Left child node (default is None).
            right (TreeNode): Right child node (default is None).
        """
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    """
    Constructs a balanced Binary Search Tree (BST) from a sorted array of integers.
    
    Args:
        nums (list of int): Sorted array of integers.
        
    Returns:
        TreeNode: Root node of the constructed BST.
    """
    if not nums:
        return None
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    
    return root

from collections import deque

def printTree(root):
    """
    Prints the tree in level order (Breadth-First Search traversal) for visualization.
    
    Args:
        root (TreeNode): Root node of the tree.
        
    Returns:
        list: List representing the tree values in level order.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Trim trailing None values from result
    while result[-1] is None:
        result.pop()
    
    return result

# Example 1
nums1 = [-10, -3, 0, 5, 9]
root1 = sortedArrayToBST(nums1)
print(printTree(root1))  # Output: [0, -3, 9, -10, None, 5]

# Example 2
nums2 = [1, 3]
root2 = sortedArrayToBST(nums2)
print(printTree(root2))  # Output: [3, 1]
