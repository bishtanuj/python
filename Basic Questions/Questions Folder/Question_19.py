# Write a program to create a string, concatenate strings and perform following operations
# 1. Check type cast of string
# 2. Comparison of strings
# 3. Slicing and Indexing
# 4. Modification of Strings
# 5. max(), len(), min(), join(), split(), capatialize(), strip(), rstrip(), lstrip()

# Creating a string
name = input("Enter the name: ")
print(name)

# Concatenate two strings
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(first_name + " " + last_name)

# Check type cast of string
value = input("Enter a value: ")
print(type(value))


# Comparison of strings
string_1 = input("Enter a string: ")
string_2 = input("Enter another string: ")

if string_1 == string_2:
    print("Both Strings are equal")
else:
    print("Both Skills are not equal")
