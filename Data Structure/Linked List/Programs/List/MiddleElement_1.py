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

    # generator function to display the linked list
    def display(self):
        current = self.head
        if self.head:
            print("Elements of the linked list:", end=" ")
            while current:
                print(current.data, end=" ")
                current = current.next
        else:
            print("Linked list is empty!!")

    # function to compute the middle element of linked list
    def compute_middle(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        if count % 2 != 0:
            mid = count // 2
        else:
            x = count // 2
            y = (count // 2) + 1
            mid = (x + y) // 2
        temp = self.head
        count_new = 0
        while temp:
            if count_new == mid:
                print(temp.data)
                break
            else:
                count_new += 1
                temp = temp.next


# driver
if __name__ == '__main__':
    items = LinkedList()
    items.insertion(12)
    items.insertion(13)
    items.insertion(14)
    items.insertion(80)

    items.display()
    print("\nMiddle Element:", end=" ")
    items.compute_middle()


"""
OUTPUT:
Elements of the linked list: 12 13 14 80 
Middle Element: 14
"""
