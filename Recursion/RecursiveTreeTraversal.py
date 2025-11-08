# Binary Tree node structure
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

# Preorder traversal (recursive)
def preorder(node):
    if not node:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)

# Inorder traversal (recursive)
def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)

# Postorder traversal (recursive)
def postorder(node):
    if not node:
        return []
    return postorder(node.left) + postorder(node.right) + [node.val]

# Test
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
assert preorder(root) == [1,2,3,4,5]
assert inorder(root) == [2,1,4,3,5]
assert postorder(root) == [2,4,5,3,1][web:24][web:25][web:37]
