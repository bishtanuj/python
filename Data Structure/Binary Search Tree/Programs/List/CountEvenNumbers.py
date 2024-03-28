# Program to count even numbers in the binary search tree

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

    def count_even(self):
        inorder_traversal = self.inorder(self.root)
        answer = len([i for i in inorder_traversal if i % 2 == 0])
        return answer


if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert(12)
    bst.insert(24)
    bst.insert(18)
    bst.insert(10)
    bst.insert(9)
    bst.insert(17)
    bst.insert(35)

    print("Inorder traversal of the binary search tree:", bst.inorder(bst.root))
    print("Total even numbers in the binary search tree:", bst.count_even())

"""
OUTPUT:
Inorder traversal of the binary search tree: [9, 10, 12, 17, 18, 24, 35]
Total even numbers in the binary search tree: 4
"""
