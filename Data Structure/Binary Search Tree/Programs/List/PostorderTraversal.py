# Program to print the elements of binary search tree in postorder traversal

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
        self.root = self.insert_recursive(self.root, data)
    
    def insert_recursive(self, root, data):
        if not root:
            root = TreeNode(data)
        elif data < root.data:
            root.left = self.insert_recursive(root.left, data)
        else:
            root.right = self.insert_recursive(root.right, data)
        return root
    
    def postorder(self, root):
        if not root:
            return
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


if __name__ == '__main__':
    bst = BinarySearchTree()
    
    bst.insert(120)
    bst.insert(40)
    bst.insert(16)
    bst.insert(180)
    bst.insert(18)
    
    print("Postorder traversal of the binary search tree:", end=" ")
    bst.postorder(bst.root)

"""
OUTPUT:
Postorder traversal of the binary search tree: 18 16 40 180 120
"""
