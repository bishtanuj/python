# Program to remove the node from the tail

# class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class of the linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, data):
        node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
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

    def delete_from_tail(self):
        if self.head:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
        else:
            print("Linked list is empty!!")


if __name__ == '__main__':
    linkedlist = LinkedList()

    for i in range(1, 12):
        linkedlist.insert_at_tail(i)
    linkedlist.display()

    linkedlist.delete_from_tail()
    linkedlist.display()
