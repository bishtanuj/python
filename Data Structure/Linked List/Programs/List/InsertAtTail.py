# Program to insert a node of the linked list from the tail

# class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class having all functionalities of the linked list
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtTail(self, data):
        node = Node(data)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
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
    
    for i in range(12, 25):
        linkedlist.insertAtTail(i)
    linkedlist.display()


'''
OUTPUT:
Linked List: 12->13->14->15->16->17->18->19->20->21->22->23->24->None
'''
