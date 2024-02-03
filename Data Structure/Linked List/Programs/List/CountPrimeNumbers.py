# Program to count the prime numbers in the linked list

# class to create a node 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def check_prime(self, num: int) -> bool:
        if num <= 1:
            return False
        for i in range(2, num//2+1):
            if num % i == 0:
                return False
        return True
    
    def insertion(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node 
            self.tail = node 
        else:
            self.head = node
            self.tail = node
    
    def count_prime(self):
        if self.head:
            current = self.head
            count = 0
            while current:
                if self.check_prime(current.data):
                    count += 1
                current = current.next
            print("\nTotal prime numbers in the Linked list:", count)
        else:
            print("Linked List is empty!!")
    
    def display(self):
        if self.head:
            current = self.head
            print("Elements of the linked list:", end=" ")
            while current:
                print(current.data, end=" ")
                current = current.next
        else:
            print("Linked list is empty!!")
                
            
if __name__ == '__main__':
    linkedlist = LinkedList()

    total_elements = int(input("Enter the total elements of the linked list: "))
    for i in range(1, total_elements+1):
        element = int(input(f"Enter Element {i}: "))
        linkedlist.insertion(element)

    linkedlist.display()
    linkedlist.count_prime()
