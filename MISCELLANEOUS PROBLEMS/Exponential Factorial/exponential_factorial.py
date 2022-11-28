# Program to print the exponential factorial

# Function to compute exponential factorial
def exponential_factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num > 1 and num < 5:
        return pow(num, pow(num-1, num-2))
    elif num > 4:
        return ("Infinity")
    else:
        return ("Enter Positive Value")


# Driver Function
if __name__ == '__main__':
    num = int(input("Enter the positive number less than or equals to 4: "))
    if num >= 0: 
        print(f"Exponential Factorial of {num} = {exponential_factorial(num)}")
    else:
        print(exponential_factorial(num))

        
'''
OUTPUT:
Enter the number: 3
Exponential Factorial of 3 = 9

OUTPUT:
Enter the number: 4
Exponential Factorial of 4 = 262144
'''
