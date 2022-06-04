# Write a program to reverse the elements of the list

list_1 = []
limit = int(input("Enter the number of element to put in list: "))
for i in range(limit):
    print("Element [", i, "]: ", end="")
    element = int(input())
    list_1.append(element)
print("Original List: ", list_1)
print("Reversed List: ", list_1[::-1])


# # OUTPUT
# Enter the number of element to put in list: 5
# Element [ 0 ]: 0
# Element [ 1 ]: 1
# Element [ 2 ]: 2
# Element [ 3 ]: 5
# Element [ 4 ]: 9
# Original List:  [0, 1, 2, 5, 9]
# Reversed List:  [9, 5, 2, 1, 0]
