class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        """Initialize a binary tree node with a value and optional left and right children."""
        self.value = value
        self.left = left
        self.right = right

def find_max_in_tree(root):
    """Find the maximum value in the binary tree using inorder traversal."""
    def inorder_traversal(node):
        """Perform inorder traversal to update the maximum value found."""
        if node is None:
            return
        inorder_traversal(node.left)
        nonlocal max_value
        if node.value > max_value:
            max_value = node.value
        inorder_traversal(node.right)
    
    if root is None:
        return None
    
    max_value = float('-inf')
    inorder_traversal(root)
    return max_value

def insert_level_order(arr, root, i, n):
    """Insert nodes into the binary tree in level order."""
    if i < n:
        temp = TreeNode(arr[i])
        root = temp

        # insert left child
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

        # insert right child
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    
    return root

# Example usage:
tree_values = [1000, 500, 2000, 250, 600, 12000]
root = insert_level_order(tree_values, None, 0, len(tree_values))
print(f'tree :{tree_values} ')
max_value = find_max_in_tree(root)
print(f"The maximum value in the tree is: {max_value}")
