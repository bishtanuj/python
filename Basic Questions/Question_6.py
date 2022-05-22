# Write a program to find the factorial of an entered number

num = int(input("Enter the number: "))

factorial = 1
if num == 0:
    print(num, "! =", 1)
elif num < 0:
    print("Kindly enter a positive number")
else:
    i = num
    while i > 0:
        factorial = factorial * i
        i -= 1
    print(num, "! =", factorial)

    

# OUTPUT
# Enter the number: 5
# 5 ! = 120
