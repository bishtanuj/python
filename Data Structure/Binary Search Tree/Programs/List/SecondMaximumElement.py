# Program to compute the second maximum of the binary search tree

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
    
    def compute_second_maximum(self):
        inorder_traversal = self.inorder(self.root)
        maximum = max(inorder_traversal)
        second_maximum = float('-infinity')
        for i in inorder_traversal:
            if maximum > i > second_maximum:
                second_maximum = i
        return second_maximum


if __name__ == '__main__':
    bst = BinarySearchTree()
    
    bst.insert(21)
    bst.insert(18)
    bst.insert(19)
    bst.insert(30)
    bst.insert(36)
    bst.insert(26)
    bst.insert(12)
    
    print("Second maximum element of the binary search tree:", bst.compute_second_maximum())
