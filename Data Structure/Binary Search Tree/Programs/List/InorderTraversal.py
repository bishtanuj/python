# Program to print the elements of binary search tree in inorder traversal

# class to create a node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# class for the bianry search tree
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self.insert_recursion(self.root, data)
    
    def insert_recursion(self, root, data):
        if root is None:
            return TreeNode(data)
        elif data < root.data:
            root.left = self.insert_recursion(root.left, data)
        else:
            root.right = self.insert_recursion(root.right, data)
        return root
    
    def inorder(self, root):
        if not root:
            return
        else:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


if __name__ == '__main__':
    bst = BinarySearchTree()
    
    bst.insert(12)
    bst.insert(18)
    bst.insert(20)
    bst.insert(36)
    bst.insert(6)
    bst.insert(4)
    bst.insert(2)
    bst.insert(10)
    
    print("Inorder traversal of bianry search tree:", end=" ")
    bst.inorder(bst.root)

"""
OUTPUT:
Inorder traversal of bianry search tree: 2 4 6 10 12 18 20 36
"""
