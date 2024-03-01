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

### Properties of the binary search tree
**1. Ordered Structure**