# Program to create a binary search tree from sorted array

# class to create a node
class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


# class for the binary search tree
class BinarySearchTree:
    def array_to_bst(self, array: list[int]) -> TreeNode:
        if not array:
            return None
        mid_val = len(array) // 2
        node = TreeNode(array[mid_val])
        node.left = self.array_to_bst(array[:mid_val])
        node.right = self.array_to_bst(array[mid_val + 1:])
        return node
    
    def inorder(self, node):
        if not node:
            return
        else:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)


if __name__ == '__main__':
    nums = set(map(int, input("Enter the elements of the array: ").split()))
    nums = list(nums)
    nums.sort()
    
    bst = BinarySearchTree()
    
    result = bst.array_to_bst(nums)
    print("Inorder traversal of the binary search tree:", end=" ")
    bst.inorder(result)
