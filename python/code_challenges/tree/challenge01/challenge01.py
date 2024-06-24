# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """Initialize a tree node."""
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    """Build a binary tree from preorder and inorder traversal lists."""
    if not preorder or not inorder:
        return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)
    root_index = inorder.index(root_val)
    
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]
    
    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]
    
    root.left = buildTree(left_preorder, left_inorder)
    root.right = buildTree(right_preorder, right_inorder)
    
    return root

def print_level_order(root):
    """Return the level order traversal of the binary tree."""
    if not root:
        return []
    
    from collections import deque
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    while result and result[-1] is None:
        result.pop()
    
    return result


# Example usage:
preorder1 = [3, 9, 20, 15, 7]
inorder1 = [9, 3, 15, 20, 7]
root1 = buildTree(preorder1, inorder1)
print(print_level_order(root1))

preorder2 = [-1]
inorder2 = [-1]
root2 = buildTree(preorder2, inorder2)
print(print_level_order(root2))
