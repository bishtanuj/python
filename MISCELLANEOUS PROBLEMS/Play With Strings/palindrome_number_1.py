# Program to check whether the given number is palindrome or not

number = int(input("Enter a number: "))
reverse = 0
temp = number
while temp > 0:
    temp_1 = temp % 10
    reverse = reverse*10 + temp_1
    temp //= 10
if number == reverse:
    print(f"{number} is a palindrome number")
else:
    print(f"{number} is not a palindrome number")
