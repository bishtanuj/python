# Binary Search Tree

***A binary search tree is a non - linear data structure that stores a collection of data elements dynamically.***

### Representation of the binary search tree
_The representation of a binary search tree depicts that each node consists of three fields. The first field consists of data, and the second and third field consists of pointer that points to another node in left and right direction respectively, i.e, left and right child respectively._

### Creation of node
```md
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
```

### Properties of the Binary Search Tree (BST)
**1. Ordered Structure** <br>
  * Each node in a BST has at most two children: a left child and a right child. <br>
  * The left child contains values less than the parent node, while the right child contains values greater than the parent node. <br>
  * This hierarchical arrangement ensures that the tree is sorted.

**2. No Duplicate Values** <br>
&emsp; - In a BST, there are no duplicate values. <br>
&emsp; - Each value appears only once in the tree.

**3. Search Efficiency:** <br>
&emsp; - BSTs allow for efficient searching operations. <br>
#^ - When searching for a specific value, we can traverse the tree by comparing the target value with the current node's value and moving left or right accordingly. <br>
&emsp; - The search time complexity is logarithmic $O(log n)$ on average, where $n$ is the number of nodes in the tree.
