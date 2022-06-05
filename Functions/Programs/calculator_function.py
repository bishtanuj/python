# Write a program to implement calculator using user defined functions

# function for addition
def addition(a, b):
    add = a + b
    print("Addition:", add)


# function for subtraction
def subtraction(a, b):
    subtract = a - b
    print("Subtraction:", subtract)


# function for product
def product(a, b):
    multiply = a * b
    print("Product:", multiply)


# function for division
def division(a, b):
    divide = a / b
    print("Division:", divide)


# function for floor division
def floor_division(a, b):
    floor_divide = a // b
    print("Floor Division:", floor_divide)


# function for remainder
def remainder(a, b):
    rem = a % b
    print("Remainder:", rem)


if __name__ == '__main__':
    # scanning the numbers for operations
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter another number: "))

    # Printing the list of operations
    print("*** Calculator ***")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Product")
    print("4. Division")
    print("5. Floor Division")
    print("6. Remainder")

    # scanning the choice form the user
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        addition(num_1, num_2)

    elif choice == 2:
        subtraction(num_1, num_2)

    elif choice == 3:
        product(num_1, num_2)

    elif choice == 4:
        division(num_1, num_2)

    elif choice == 5:
        floor_division(num_1, num_2)

    elif choice == 6:
        remainder(num_1, num_2)

    else:
        print("Kindly enter a positive number!!")

        
  
# OUTPUT:
# Enter first number: 3
# Enter another number: 9
# *** Calculator ***
# 1. Addition
# 2. Subtraction
# 3. Product
# 4. Division
# 5. Floor Division
# 6. Remainder
# Enter Your Choice: 1
# Addition: 12
  

# OUTPUT
# Enter first number: 9
# Enter another number: 3
# *** Calculator ***
# 1. Addition
# 2. Subtraction
# 3. Product
# 4. Division
# 5. Floor Division
# 6. Remainder
# Enter Your Choice: 2
# Subtraction: 6
