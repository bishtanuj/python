# Write a program to add two numbers using user defined function

def addition(a, b):
    add = a + b
    print("Addition:", add)


if __name__ == '__main__':
    num_1 = int(input("Enter First Number: "))
    num_2 = int(input("Enter Another Number: "))

    addition(num_1, num_2)

    
# OUTPUT
# Enter First Number: 15
# Enter Another Number: 16
# Addition: 31
