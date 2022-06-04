# Write a program to find the length of the string

list_1 = []
limit = int(input("Enter the number of elements to put in list: "))
for i in range(limit):
    print("Element [", i, "]: ", end="")
    element = input()
    list_1.append(element)
print("List: ", list_1)
print("Length of the list: ", len(list_1))

# Output:
# Enter the number of elements to put in list: 5
# Element [ 0 ]: a
# Element [ 1 ]: b
# Element [ 2 ]: c
# Element [ 3 ]: d
# Element [ 4 ]: e
# List:  ['a', 'b', 'c', 'd', 'e']
# Length of the list:  5
