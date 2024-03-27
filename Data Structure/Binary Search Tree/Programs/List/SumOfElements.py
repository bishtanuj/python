# Program to print the addition of elements of the binary search tree

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

    def insert_recursive(self, root, data) -> TreeNode:
        if not root:
            root = TreeNode(data)
        elif data < root.data:
            root.left = self.insert_recursive(root.left, data)
        else:
            root.right = self.insert_recursive(root.right, data)
        return root

    def sum_of_elements(self, root) -> int:
        if not root:
            return 0
        ans = root.data
        ans += self.sum_of_elements(root.left) + self.sum_of_elements(root.right)
        return ans


if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert(10)
    bst.insert(25)
    bst.insert(15)
    bst.insert(30)

    result = bst.sum_of_elements(bst.root)
    print("Sum of elements of the binary search tree:", result)

"""
OUTPUT:
Sum of elements of the binary search tree: 80
"""
