# Program to find the second minimum element

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertion(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def display(self):
        current = self.head
        if self.head:
            print("Elements of the linked list:", end=" ")
            while current:
                print(current.data, end=" ")
                current = current.next
        else:
            print("Linked list is empty!!")

    def compute_second_minimum(self):
        current = self.head
        minimum = current.data
        while current:
            if current.data < minimum:
                minimum = current.data
            else:
                current = current.next
        temp = self.head
        second_minimum = float('infinity')
        while temp:
            if minimum < temp.data < second_minimum:
                second_minimum = temp.data
            else:
                temp = temp.next
        return second_minimum


if __name__ == '__main__':
    linkedlist = LinkedList()

    linkedlist.insertion(10)
    linkedlist.insertion(11)
    linkedlist.insertion(12)
    linkedlist.insertion(15)
    linkedlist.insertion(18)
    linkedlist.insertion(20)

    linkedlist.display()

    print(f"\nSecond minimum element of the linked list: {linkedlist.compute_second_minimum()}")


"""
OUTPUT:
Elements of the linked list: 10 11 12 15 18 20 
Second minimum element of the linked list: 11
"""
