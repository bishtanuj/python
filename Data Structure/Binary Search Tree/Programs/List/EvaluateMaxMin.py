# Program to compute maximum and minimum element in the binary search tree

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

    def inorder(self, root):
        if not root:
            return []
        else:
            return self.inorder(root.left) + [root.data] + self.inorder(root.right)

    def compute_max_min(self):
        inorder_traversal = self.inorder(self.root)
        print("Maximum element of the binary search tree:", max(inorder_traversal))
        print("Minimum element of the binary search tree:", min(inorder_traversal))


if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert(12)
    bst.insert(23)
    bst.insert(35)
    bst.insert(6)
    bst.insert(2)
    bst.insert(1)

    bst.compute_max_min()

"""
OUTPUT:
Maximum element of the binary search tree: 35
Minimum element of the binary search tree: 1
"""
