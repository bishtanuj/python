# Write a program to check whether the element is existing in the list

list_1 = []
limit = int(input("Enter the number of elements to put in list: "))

# Scanning the elements in list
for i in range(limit):
    print("Element [", i, "]: ", end="")
    element = int(input())
    list_1.append(element)

# Printing the list
print("List: ", list_1)

# Scanning the element to find in list
element_1 = input("Enter an element: ")

# Finding the entered element and printing the conclusion
if element_1 in list_1:
    print(element_1, "is present in list")
else:
    print(element_1, "is not present in list")

    
# # Output
# Enter the number of elements to put in list: 6
# Element [ 0 ]: 5
# Element [ 1 ]: 4
# Element [ 2 ]: 3
# Element [ 3 ]: 2
# Element [ 4 ]: 1
# Element [ 5 ]: 0
# List:  [5, 4, 3, 2, 1, 0]
# Enter an element: 7
# 7 is not present in list

