class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if not self.root:
            self.root = BinaryTreeNode(val)
        else:
            self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        # Level order insertion
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            if not curr.left:
                curr.left = BinaryTreeNode(val)
                return
            elif not curr.right:
                curr.right = BinaryTreeNode(val)
                return
            else:
                queue.append(curr.left)
                queue.append(curr.right)
    
    def inorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder(node.left, result)
            result.append(node.val)
            self.inorder(node.right, result)
        return result
    
    def preorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.val)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
        return result
    
    def postorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.val)
        return result
    
    def level_order(self):
        if not self.root:
            return []
        result, queue = [], deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
