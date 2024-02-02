# Program to count the odd numbers in the linked list

# class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class to create a linked list
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
            print("Elements of the linked list: ")
            while current:
                print(current.data, end="->")
                current = current.next
            print(None)
        else:
            print("Linked list is empty!!")

    def count_odd(self):
        count = 0
        current = self.head
        while current:
            if current.data % 2 != 0:
                count += 1
            current = current.next
        return count


if __name__ == '__main__':
    linkedlist = LinkedList()

    linkedlist.insertion(14)
    linkedlist.insertion(16)
    linkedlist.insertion(18)
    linkedlist.insertion(21)
    linkedlist.insertion(29)
    linkedlist.insertion(17)

    linkedlist.display()

    print(f"\nNumber of odd elements in the linked list: {linkedlist.count_odd()}")
