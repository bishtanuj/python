# Program to print the largest and smallest element of the linked list

# class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class to create a linked list
class LinkedList:
    # function to create an empty linked list
    def __init__(self):
        self.head = None
        self.tail = None

    # function to insert the data into linked list
    def insertion(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    # generator function to display the elements of linked list
    def display(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    # function to print the maximum element of linked list
    def compute_max(self):
        current = self.head
        maximum = current.data
        while current:
            if current.data > maximum:
                maximum = current.data
            else:
                current = current.next
        print("\nMaximum Element:", maximum)

    # function to print the minimum element of linked list
    def compute_min(self):
        current = self.head
        minimum = current.data
        while current:
            if current.data < minimum:
                minimum = current.data
            else:
                current = current.next
        print("\nMinimum Element:", minimum)


# driver
if __name__ == '__main__':
    items = LinkedList()
    items.insertion(17)
    items.insertion(79)
    items.insertion(45)
    items.insertion(49)
    items.insertion(98)
    items.insertion(72)
    items.insertion(3)
    print("Elements of Linked List:", end=" ")
    for i in items.display():
        print(i, end=" ")
    items.compute_max()
    items.compute_min()
