# Program to check whether the integer is divisible by 5 or not after shuffling its digits

number = int(input("Enter a number: "))
count = 0
while number > 0:
    temp = number % 10
    if temp % 5 == 0:
        count += 1
    number //= 10
if count == 0:
    print("No")
elif count > 0:
    print("Yes")


# OUTPUT - 1
# Enter a number: 123
# No

# OUTPUT - 2
# Enter a number: 301
# Yes
