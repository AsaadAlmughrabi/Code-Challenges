class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        """
        Initializes a new instance of the class.

  
        """
        self.value = value
        self.left = left
        self.right = right

def max_height(root):
    """
    Calculates the maximum height of a binary tree starting from the given root node.

   
    """
    if not root:
        return -1
    
    left_height = max_height(root.left)
    right_height = max_height(root.right)
    
    return max(left_height, right_height) + 1



root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(28)
root.right.right = TreeNode(50)
root.left.right.left = TreeNode(29)

print(max_height(root)) 
