# Program to create a binary search tree

# class to create a node
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


# class for the binary search tree
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insertion(self, data):
        self.root = self.insert_recursive(self.root, data)
    
    def insert_recursive(self, root, data):
        if not root:
            return TreeNode(data)
        elif data < root.data:
            root.left = self.insert_recursive(root.left, data)
        else:
            root.right = self.insert_recursive(root.right, data)
        return root

    def inorder(self, root):
        if not root:
            return
        else:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)
    
