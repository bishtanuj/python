# Write a program to perform the binary search

# function to perform binary search
def binary_search(lst_1, lst_size, element_key):
    low = 0
    high = lst_size - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if lst_1[mid] == element_key:
            return mid
        elif lst_1[mid] > element_key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# scanning the size of the list from the user
size = int(input("Enter the size of the list: "))

# declaring an empty list
list_1 = []

# scanning the elements of the list
print(f"Enter {size} elements of the list:")
for i in range(size):
    print(f"Element {i}:", end=" ")
    element = int(input())
    list_1.append(element)

# scanning the key elements from the user
key = int(input("Enter the element to find in the list: "))

# calling the binary_search() function and printing the result
result = binary_search(list_1, size, key)
if result == -1:
    print(f"{key} element is not found!")
else:
    print(f"{key} element is found at {result}")

    
  
# # OUTPUT
# Enter the size of the list: 5
# Enter 5 elements of the list:
# Element 0: 0
# Element 1: 1
# Element 2: 2
# Element 3: 3
# Element 4: 4
# Enter the element to find in the list: 2
# 2 element is found at 2

# OUTPUT
# Enter the size of the list: 5
# Enter 5 elements of the list:
# Element 0: 0
# Element 1: 1
# Element 2: 2
# Element 3: 3
# Element 4: 4
# Enter the element to find in the list: 5
# 5 element is not found!
