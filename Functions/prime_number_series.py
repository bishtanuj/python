# Write a program to print the prime numbers in the given range by user using user defined function

def prime(num_1, num_2):
    for number in range(num_1, num_2 + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number, end=" ")


num_1 = int(input("Enter the minimum limit of the prime number series: "))
num_2 = int(input("Enter the maximum limit of the prime number series: "))
print("The prime numbers within range", num_1, "and", num_2, "is/are:")
if num_1 <= 1:
    num_1 = 2
if num_2 <= 1:
    num_2 = 2
prime(num_1, num_2)


# OUTPUT
# Enter the minimum limit of the prime number series: 1
# Enter the maximum limit of the prime number series: 10
# The prime numbers within range 1 and 10 is/are:
# 2 3 5 7 
