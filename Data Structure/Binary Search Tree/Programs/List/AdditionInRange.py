# Program to print the addition of elements in the given range of elements

# class to create a node:
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

    def sum_in_range(self, root, low, high):
        if not root:
            return 0
        ans = root.data if (low <= root.data <= high) else 0
        if high < root.data:
            ans += self.sum_in_range(root.left, low, high)
        elif low > root.data:
            ans += self.sum_in_range(root.right, low, high)
        else:
            ans += self.sum_in_range(root.left, low, high) + self.sum_in_range(root.right, low, high)
        return ans


if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(18)

    low_range, high_range = 7, 15

    result = bst.sum_in_range(bst.root, low_range, high_range)
    print(f"Addition of elements in range {low_range} to {high_range}:", result)
