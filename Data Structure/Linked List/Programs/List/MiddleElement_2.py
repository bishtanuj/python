# Program to print the middle element of linked list

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

    # function to display the elements
    def display(self):
        current = self.head
        if self.head:
            print("Elements of the linked list:", end=" ")
            while current:
                print(current.data, end=" ")
                current = current.next
        else:
            print("Linked list is empty")

    # function to compute the middle element of linked list
    def compute_middle(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)


# driver
if __name__ == '__main__':
    items = LinkedList()
    items.insertion(12)
    items.insertion(13)
    items.insertion(14)
    items.insertion(15)
    items.insertion(20)
    
    items.display()
    
    print("\nMiddle Element:", end=" ")
    items.compute_middle()

"""
OUTPUT:
Elements of the linked list: 12 13 14 15 20 
Middle Element: 14
"""
