# Program to count the even numbers in the linked list

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
        while current:
            print(current.data, end=" ")
            current = current.next

    def count_even(self):
        count = 0
        current = self.head
        while current:
            if current.data % 2 == 0:
                count += 1
            current = current.next
        return count


if __name__ == '__main__':
    linkedlist = LinkedList()

    linkedlist.insertion(12)
    linkedlist.insertion(14)
    linkedlist.insertion(15)
    linkedlist.insertion(16)
    linkedlist.insertion(18)
    linkedlist.insertion(19)
    linkedlist.insertion(20)

    print("Elements of linked list:", end=" ")
    linkedlist.display()

    print(f"Total even numbers in the linked list: {linkedlist.count_even()}")
