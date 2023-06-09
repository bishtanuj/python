""" Calculator """

print("Calculator")
print("1.   Add")
print("2.   Subtract")
print("3.   Product")
print("4.   Division")
print("5.   Exponent")
print("6.   EXIT")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        add = x + y
        print("Addition:", add)
    case 2:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        subtraction = x - y
        print("Subtraction: ", subtraction)
    case 3:
        x = int(input("Enter multiplicand: "))
        y = int(input("Enter multiplier: "))
        product = x * y
        print("Product:", product)
    case 4:
        x = int(input("Enter dividend: "))
        y = int(input("Enter divisor: "))
        if y > x:
            division = x / y
            print("Division:", division)
        else:
            division = x // y
            print("Division:", division)
    case 5:
        x = int(input("Enter the number: "))
        y = int(input("Enter the power: "))
        exponent = x ** y
        print("Exponent:", exponent)
    case 6:
        print("Thanks for using")
    case _:
        print("!! Enter right choice !!")
