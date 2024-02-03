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
            return count
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

    linkedlist.insertion(12)
    linkedlist.insertion(14)
    linkedlist.insertion(15)
    linkedlist.insertion(19)
    linkedlist.insertion(23)

    linkedlist.display()

    print(f"\nTotal prime numbers in a linked list: {linkedlist.count_prime()}")
    
