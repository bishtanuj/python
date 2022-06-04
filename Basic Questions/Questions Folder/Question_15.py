# Write a program to find the smallest and largest element in the list

list_1 = []
limit = int(input("Enter the number of elements to put in list: "))
for i in range(limit):
    print("Element [", i, "]: ", end="")
    element = int(input())
    list_1.append(element)

print("List: ", list_1)
print("Maximum element in list: ", max(list_1))
print("Minimum element in list: ", min(list_1))


# # OUTPUT
# Enter the number of elements to put in list: 5
# Element [ 0 ]: 1
# Element [ 1 ]: 2
# Element [ 2 ]: 5
# Element [ 3 ]: 6
# Element [ 4 ]: 9
# List:  [1, 2, 5, 6, 9]
# Maximum element in list:  9
# Minimum element in list:  1
