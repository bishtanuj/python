# Linked List
***A linked list is a linear data structure that stores a collection of data elements dynamically.***

### Representation of the linked list
The representation of a linked list depicts that each node consist of two fields. The first field consists of data, and the second field consists of pointer that point to another node.

### Creation of the node
```md
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
```
