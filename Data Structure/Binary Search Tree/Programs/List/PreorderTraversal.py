# Program to print the elements of binary search tree in preorder traversal

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
    
    def insert(self, data):
        self.root = self.insert_recursion(self.root, data)
    
    def insert_recursion(self, root, data):
        if not root:
            root = TreeNode(data)
        elif data < root.data:
            root.left = self.insert_recursion(root.left, data)
        else:
            root.right = self.insert_recursion(root.right, data)
        return root
    
    def preorder(self, root):
        if not root:
            return
        else:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)


if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert(12)
    bst.insert(14)
    bst.insert(22)
    bst.insert(24)
    bst.insert(26)
    bst.insert(48)
    bst.insert(46)
    
    print("Preorder traversal of the the binary search tree:", end=" ")
    bst.preorder(bst.root)
  
