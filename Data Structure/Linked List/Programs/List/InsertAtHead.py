# Program to add elements of the linked list from the head

# class to create a node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# class having all functionalities of the linked list
class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_head(self, data):
    node = Node(data)
    if self.head:
      temp = node
      temp.next = self.head
      self.head = temp
    else:
      self.head = node

  def display(self):
    if self.head:
      print("Linked List:", end=" ")
      current = self.head
      while current:
        print(current.data, end="->")
        current = current.next
      print(None)
    else:
      print("Linked list is empty!!")


if __name__ == '__main__':
    linkedlist = LinkedList()
    
    linkedlist.insert_at_head(12)
    linkedlist.insert_at_head(14)
    linkedlist.insert_at_head(18)
    linkedlist.insert_at_head(16)
    linkedlist.insert_at_head(22)
    linkedlist.insert_at_head(26)

    linkedlist.display()
