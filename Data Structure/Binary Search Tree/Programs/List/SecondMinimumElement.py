# Program to compute the second minimum element of the binary search tree

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
    
    def compute_second_minimum(self):
        inorder_traversal = self.inorder(self.root)
        minimum = min(inorder_traversal)
        second_minimum = float('infinity')
        for i in inorder_traversal:
            if minimum < i < second_minimum:
                second_minimum = i
        return second_minimum


if __name__ == '__main__':
    bst = BinarySearchTree()
    
    bst.insert(90)
    bst.insert(76)
    bst.insert(72)
    bst.insert(85)
    bst.insert(68)
    bst.insert(40)
    
    print("Second minimum element of the binary search tree:", bst.compute_second_minimum())

"""
OUTPUT:
Second minimum element of the binary search tree: 68
"""
