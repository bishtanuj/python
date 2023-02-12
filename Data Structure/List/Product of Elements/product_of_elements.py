# Program to find the product of elements of list

# Creating an empty list
list = []

# Scanning size of the list
size = int(input("Enter the size of the list: "))

# Scanning the list
for i in range(size):
    print(f"Element [{i}]: ", end = "")
    element = int(input())

    list.append(element)

# Printing the list
print ("List:")
print (list)

product = 1
# Performing Addition of elements of list
for element in range(0, size):
    product = product * list[element]

# Printing addition of elements of list
print("Product:", product)
