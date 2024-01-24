# Program to print the fibonacci series in linked list

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

    # function to display the elements of Linked List
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next


# driver
if __name__ == '__main__':
    items = LinkedList()
    limit = int(input("Enter the range of fibonacci series: "))
    num_0, num_1 = 0, 1
    if limit > 0:
        match limit:
            case 1:
                items.insertion(num_0)
            case 2:
                items.insertion(num_0)
                items.insertion(num_1)
            case _:
                items.insertion(num_0)
                items.insertion(num_1)
                for i in range(limit - 2):
                    temp = num_0 + num_1
                    items.insertion(temp)
                    num_0, num_1 = num_1, temp
        print("Fibonacci Series:", end=" ")
        items.display()
    else:
        print("Enter the positive range only!!")


'''
OUTPUT:
Enter the range of fibonacci series: 10
Fibonacci Series: 0 1 1 2 3 5 8 13 21 34 
'''
