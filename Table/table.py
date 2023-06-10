# Program to print the table 

# Scanning the number
number = int(input("Enter the number: "))

# Printing the table
print(f"Table of {number}: ")
for i in range(1,11):
    product = number * i
    print(f"{number} * {i} = {product}")

    

Enter the number: 5
Table of 5: 
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
