# Program to print the factorial of a number

fact = 1
num = int(input("Enter a number: "))
if num < 0:
    print("Number should not be negative")
elif num == 0:
    print("0! = 1")
else:
    i = num
    while i > 0:
        fact *= i
        i -= 1
    print(f"{num}! = {fact}")
    
    
'''
OUTPUT:
Enter a number: 5
5! = 120
'''
