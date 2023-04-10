# Program to check whether the given number is palindrome or not

# METHOD 1:
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

    
    
# METHOD 2
# Scan a number
number = int(input("Enter the number: "))

# Check whether the number is positive or not
# Because negative number cannot be a palindrome
if number < 0:
    print(f"{number} is not a palindrome")
else:
    # Convert the number into list
    list_number = [int(i) for i in str(number)]

    # Reverse the list
    reverse_list_number = list_number[::-1]

    # Compare both lists
    if list_number == reverse_list_number:
        print(f"{number} is a palindrome")
    else:
        print(f"{number} is not a palindrome")
