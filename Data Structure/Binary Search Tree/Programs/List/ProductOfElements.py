# Program to print the product of the elements of the binary search tree

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

    def product_of_elements(self, root):
        if not root:
            return 1
        ans = 1
        ans *= root.data
        ans *= self.product_of_elements(root.left) * self.product_of_elements(root.right)
        return ans


if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert(1)
    bst.insert(5)
    bst.insert(2)
    bst.insert(8)

    result = bst.product_of_elements(bst.root)
    print("Product of elements of the binary search tree:", result)
