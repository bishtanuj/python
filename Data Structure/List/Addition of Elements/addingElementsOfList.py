# Program to add elements of list

# Creating an empty list
list = []

# Scanning size of the list
size = int(input("Enter the size of the list: "))

# Scanning the list
for i in range(0,size):
    print("Element [",i,"]: ", end = "")
    element = int(input())

    list.append(element)

# Printing the list
print ("List: ")
print (list)

sum = 0
# Performing Addition of elements of list
for element in range(0, size):
    sum = sum + list[element]

# Printing addition of elements of list
print("Addition: ", sum)
