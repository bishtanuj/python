# Program to print the product of elements in the given range of elements

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

    def product_in_range(self, root, low, high):
        if not root:
            return 1
        ans = root.data if (low <= root.data <= high) else 1
        if high < root.data:
            ans *= self.product_in_range(root.left, low, high)
        elif low > root.data:
            ans *= self.product_in_range(root.right, low, high)
        else:
            ans *= self.product_in_range(root.left, low, high) * self.product_in_range(root.right, low, high)
        return ans


if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert(1)
    bst.insert(2)
    bst.insert(5)
    bst.insert(8)

    low_range, high_range = 1, 8

    result = bst.product_in_range(bst.root, low_range, high_range)
    print(f"Product of elements in range {low_range} to {high_range}:", result)

"""
OUTPUT:
Product of elements in range 1 to 8: 80
"""
