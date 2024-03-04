# Program to remove the nth element from the last of the linked list

# class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class for the linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, data):
        node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
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

    def count_length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def remove_nth_element_from_end(self, n):
        length = self.count_length()
        current = self.head
        count = 1
        while current:
            if count < (length + 1) - n:
                count += 1
                current = current.next
            else:
                break
        if current != self.head:
            temp = self.head
            while temp.next != current:
                temp = temp.next
            temp.next = current.next
        else:
            temp = self.head
            self.head = temp.next
            del temp


if __name__ == '__main__':
    linkedlist = LinkedList()

    for i in range(1, 6):
        linkedlist.insert_at_tail(i)

    linkedlist.display()

    linkedlist.remove_nth_element_from_end(2)
    linkedlist.display()
