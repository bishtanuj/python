# Write a program to multiply all the elements of list

list_1 = []
limit = int(input("Enter the number of element to put in list: "))
result = 1
for i in range(limit):
    print("Element [", i, "]: ", end="")
    element = int(input())
    list_1.append(element)
    result = result * element
print("List: ", list_1)
print("Product of elements in list:", result)


# # OUTPUT
# Enter the number of element to put in list: 6
# Element [ 0 ]: 2
# Element [ 1 ]: 1
# Element [ 2 ]: 4
# Element [ 3 ]: 5
# Element [ 4 ]: 8
# Element [ 5 ]: 9
# List:  [2, 1, 4, 5, 8, 9]
# Product of elements in list: 2880
