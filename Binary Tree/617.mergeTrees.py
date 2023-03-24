class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    if not root1 and not root2:
        return None
    elif not root1:
        return root2
    elif not root2:
        return root1
    else:
        new_node = TreeNode(root1.val + root2.val)
        new_node.left = mergeTrees(root1.left, root2.left)
        new_node.right = mergeTrees(root1.right, root2.right)
        return new_node

      
 # 2
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1, root2):
    if root1 is None:
        return root2
    if root2 is None:
        return root1

    root1.val += root2.val
    root1.left = mergeTrees(root1.left, root2.left)
    root1.right = mergeTrees(root1.right, root2.right)

    return root1
