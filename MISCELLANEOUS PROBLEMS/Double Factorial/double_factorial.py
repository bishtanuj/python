# Program to print the double factorial of a number

# Function to compute double factorial
def double_factorial(num):
    fact = 1
    if num == 0 or num == 1:
        return fact
    elif num % 2 == 0 and num > 0:
        i = num
        while(i > 0):
            fact *= i
            i -= 2
        return fact
    elif num % 2 != 0 and num > 1:
        j = num
        while(j > 0):
            fact *= j
            j -= 2
        return fact


# Driver Function
if __name__ == '__main__':
    num = int(input("Enter the number: "))
    print(f"{num}!! = {double_factorial(num)}")

    

'''
OUTPUT:
Enter the number: 5
5!! = 15
'''
