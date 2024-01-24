# Program to create a linked list

# class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class to create a linked list
class LinkedList:
    # create an empty linked list
    def __init__(self):
        self.head = None
        self.tail = None

    # function to insert data into linked list
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
            print(current.data, end=" ")
            current = current.next


# driver
if __name__ == '__main__':
    items = LinkedList()
    items.insertion(12)
    items.insertion(13)
    items.insertion(51)
    items.insertion(97)
    print("Elements of Linked List:", end=" ")
    items.display()


'''
OUTPUT:
Elements of Linked List: 12 13 51 97 
'''
