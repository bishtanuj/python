# Program to print the table 

# Scanning the number
number = int(input("Enter the number: "))

# Printing the table
print(f"Table of {number}: ")
for i in range(1,11):
    product = number * i
    print(f"{number} * {i} = {product}")
