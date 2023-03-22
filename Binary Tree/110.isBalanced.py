# GPT
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: TreeNode) -> bool:
    """
    Returns True if the binary tree rooted at root is height-balanced,
    and False otherwise.
    """
    if root is None:
        return True

    # Recursively check if left and right subtrees are balanced
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    if abs(left_height - right_height) > 1:
        return False

    return is_balanced(root.left) and is_balanced(root.right)

def get_height(root: TreeNode) -> int:
    """
    Returns the height of the binary tree rooted at root.
    """
    if root is None:
        return 0

    left_height = get_height(root.left)
    right_height = get_height(root.right)

    return max(left_height, right_height) + 1
  
  
  
  
  
  
  
  ####################################################
'''
To determine if a binary tree is height-balanced, we can use the following approach:
1. A tree is considered height-balanced if the difference between the heights of its left and right subtrees is at most 1.
2. Recursively check the left and right subtrees of each node to see if they are height-balanced.
3. If a subtree is not height-balanced, then the entire tree is not height-balanced, and we can return False.
4. If all subtrees are height-balanced, then we can return True.
Here is a Python code implementation of this approach:
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: TreeNode) -> bool:
    if not root:
        # An empty tree is height-balanced by definition
        return True

    # Check if left and right subtrees are height-balanced
    left_balanced = is_balanced(root.left)
    right_balanced = is_balanced(root.right)

    if not left_balanced or not right_balanced:
        # If either subtree is not height-balanced, then the entire tree is not height-balanced
        return False

    # Check if the difference between the heights of the left and right subtrees is at most 1
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    if abs(left_height - right_height) > 1:
        return False

    # If all checks passed, then the tree is height-balanced
    return True

def get_height(node: TreeNode) -> int:
    if not node:
        return 0
    return 1 + max(get_height(node.left), get_height(node.right))
  
# We can test this implementation using the following example:
'''
   3
   / \
  9  20
    /  \
   15   7
 The above tree is height-balanced, so is_balanced(root) should return True.
 '''
