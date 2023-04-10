# Program to check whether the number is palindrome or not

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
