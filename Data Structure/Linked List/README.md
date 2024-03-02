# Linked List
***A linked list is a linear data structure that stores a collection of data elements dynamically.***

### Representation of the linked list
_The representation of a linked list depicts that each node consist of two fields. The first field consists of data, and the second field consists of pointer that point to another node._

### Properties of the linked list
**1. Dynamic Size:**
   * Unlike fixed - size arrays, linked list can **expand or contract** as needed during program execution.
   * This dynamic sizing makes linked lists suitable for scenarios where the number of elements can change over time.

**2. Effective Element Insertion and Deletion:**
  * Linked list allow **efficient insertion and deletion** of elements.
  * By updating pointers, you can insert or delete elements from anywhere in the list.
  * This flexibility is especially useful when dealing with dynamic data.

**3. Node Structure:**
  * A linked list consists of **nodes**, where each node contains two components:
    * **Data**: The actual value or payload associated with the node.
    * **Reference (Link)**: A pointer to the next node in the sequence.   
  * This structure allows for **sequential traversal** through the list.

**4. Memory Efficiency**:
  * Linked list do not waste memory due to fixed sizes.
  * However, they consume extra memory because they use pointers to keep track of the next successive node.


### Creation of the node
```md
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### Programs
👉 [Visit here!](https://github.com/bishtanuj/python/tree/main/Data%20Structure/Linked%20List/Programs#list-of-programs) - To study the programs of the linked list.
