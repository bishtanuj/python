# Write a program to interchange first and last element of list

list_1 = []
limit = int(input("Enter the number of elements to put in list: "))

#  Scanning the list
i = 0
while i < limit:
    print("Element [", i, "]: ", end="")
    element = int(input())
    list_1.append(element)
    i += 1

# Printing the list
print("Original List: ")
print(list_1)

# Swapping the first and last element of list
length = len(list_1)
temp = list_1[0]
list_1[0] = list_1[length-1]
list_1[length-1] = temp

# Printing the modified list
print("\nThe modified list: ")
print(list_1)

# Output
Enter the number of elements to put in list: 5
Element [ 0 ]: 1
Element [ 1 ]: 2
Element [ 2 ]: 3
Element [ 3 ]: 4
Element [ 4 ]: 5
Original List: 
[1, 2, 3, 4, 5]

The modified list: 
[5, 2, 3, 4, 1]
