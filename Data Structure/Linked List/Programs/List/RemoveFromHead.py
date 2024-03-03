# Program to delete a node of the linked list from the head

# Program to remove the node from the head

# class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class for the linked list
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

    def delete_from_head(self):
        if self.head:
            temp = self.head
            self.head = temp.next
            del temp
        else:
            print("Linked list is empty!!")


if __name__ == '__main__':
    linkedlist = LinkedList()

    for i in range(1, 12):
        linkedlist.insert_at_tail(i)
    linkedlist.display()

    linkedlist.delete_from_head()
    linkedlist.display()

"""
OUTPUT:
Linked List: 1->2->3->4->5->6->7->8->9->10->11->None
Linked List: 2->3->4->5->6->7->8->9->10->11->None
"""
