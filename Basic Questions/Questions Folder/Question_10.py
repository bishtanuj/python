# Write a program to swap two elements in a list

list_1 = []
limit = int(input("Enter the number of elements to put in list: "))

# Scanning the list
i = 0
while i < limit:
    print("Element [", i, "]: ", end="")
    element = int(input())
    list_1.append(element)
    i += 1
print("Original List: ")
print(list_1)

# Scanning the position of elements in list to swap
position_1 = int(input("Enter first position of element to swap: "))
position_2 = int(input("Enter second position of element to swap: "))

# Swapping the elements
temp = list_1[position_1]
list_1[position_1] = list_1[position_2]
list_1[position_2] = temp

# Printing the modified list
print("Modified List: ")
print(list_1)


# # Output
# Enter the number of elements to put in list: 5
# Element [ 0 ]: 1
# Element [ 1 ]: 2
# Element [ 2 ]: 3
# Element [ 3 ]: 4
# Element [ 4 ]: 5
# Original List: 
# [1, 2, 3, 4, 5]
# Enter first position of element to swap: 3
# Enter second position of element to swap: 2
# Modified List: 
# [1, 2, 4, 3, 5]
