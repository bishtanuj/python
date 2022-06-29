# Write a program to create a string, concatenate strings and perform following operations
# 1. Check type cast of String
# 2. Comparison of Strings
# 3. Slicing and Indexing
# 4. Modification of Strings
# 5. max(), len(), min(), join(), split(), capitalize(), strip()

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
    print("Both Strings are not equal")

# Slicing of string
string_1 = input("Enter a string: ")
length = len(string_1)
print(string_1[2:length])

# Use of len()
print("Length of the name: ", len(name))

# Use of max()
print("Maximum ASCII value element in name: ", max(name))

# use of min()
print("Minimum ASCII value element in name: ", min(name))

# Use of join()
first_name = input("Enter Your First Name: ")
middle_name = input("Enter Your Middle Name: ")
last_name = input("Enter Your Last Name: ")
m = first_name, middle_name, last_name
print("Your Name: ", " ".join(m))

# Use of split()
file_name = input("Enter a file name with the extension: ")
x, y = file_name.split(".")
print("Extension of your file:", y)

# Use of capitalize()
str_1 = input("Enter the string: ")
print("String with first letter as capital letter: \n", str_1.capitalize())

# Use of upper()
print("String in Capital Letters: \n", str_1.upper())

# Use of lower()
print("String in Lower Letters: \n", str_1.lower())

place = "   Taj Mahal   "
txt = place.strip()
print(f"{txt} is one of the beautiful wonders of world")


# OUTPUT
# Enter the name: Anuj Bisht
# Anuj Bisht
# Enter your first name: Anuj
# Enter your last name: Bisht
# Anuj Bisht
# Enter a value: 5
# <class 'str'>
# Enter a string: Hi! How are you?
# Enter another string: Wow! What a fantastic day.
# Both Strings are not equal
# Enter a string: Have a nice day.
# ve a nice day.
# Length of the name:  10
# Maximum ASCII value element in name:  u
# Minimum ASCII value element in name:   
# Enter Your First Name: Anuj
# Enter Your Middle Name: 
# Enter Your Last Name: Bisht
# Your Name:  Anuj  Bisht
# Enter a file name with the extension: anuj.java
# Extension of your file: java
# Enter the string: What an excellent performance!
# String with first letter as capital letter: 
#  What an excellent performance!
# String in Capital Letters: 
#  WHAT AN EXCELLENT PERFORMANCE!
# String in Lower Letters: 
#  what an excellent performance!
# Taj Mahal is one of the beautiful wonders of world
