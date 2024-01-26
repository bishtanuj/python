# Program to find the second maximum element

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
        while current:
            print(current.data, end=" ")
            current = current.next

    def compute_second_maximum(self):
        current = self.head
        maximum = current.data
        while current:
            if current.data > maximum:
                maximum = current.data
            else:
                current = current.next
        second_maximum = float('-infinity')
        temp = self.head
        while temp:
            if maximum > temp.data > second_maximum:
                second_maximum = temp.data
            else:
                temp = temp.next
        return second_maximum


if __name__ == '__main__':
    linkedlist = LinkedList()

    linkedlist.insertion(10)
    linkedlist.insertion(11)
    linkedlist.insertion(14)
    linkedlist.insertion(15)
    linkedlist.insertion(18)
    linkedlist.insertion(20)

    print("Elements of linked list:", end=" ")
    linkedlist.display()

    print(f"\nSecond maximum element of the linked list: {linkedlist.compute_second_maximum()}")
