class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data <root.item:
            root.left=self.rinsert(root.left,data)
        elif data> root.item:
            root.right=self.rinsert(root.right,data)
        return root
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root is None or root.item==data:
            return root
        if data <root.item:
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)
    def min_value(self,temp):
        current=temp
        while current.left is not None:
            current=current.left
        return current.item
    def max_value(self,temp):
        current=temp
        while current.right is not None:
            current=current.right
        return current.item
    def delete(self,data):
        self.root=self.rdelete(self.root,data)
    def rdelete(self, root, data):
        if root is None:
            return root
        if data < root.item:
            root.left=self.rdelete(root.left,data)
        elif data > root.item:
            root.right=self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item=self.min_value(root.right)
            self.rdelete(root.right,root.item)
        return root
    def size(self):
        return len(self.inorder())
bst = BST()

# Insert elements into the BST
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

# Search for an element in the BST
print("Search for 40:", bst.search(40))

# Inorder traversal
print("Inorder traversal:", bst.inorder())

# Preorder traversal
print("Preorder traversal:", bst.preorder())

# Postorder traversal
print("Postorder traversal:", bst.postorder())

# Find the minimum value in the BST
print("Minimum value:", bst.min_value(bst.root))

# Find the maximum value in the BST
print("Maximum value:", bst.max_value(bst.root))

# Delete an element from the BST
bst.delete(30)
print("Inorder traversal after deleting 30:", bst.inorder())
