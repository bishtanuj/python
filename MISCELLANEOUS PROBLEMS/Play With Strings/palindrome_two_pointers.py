# Program to check whether the input string is palindrome

# function to check the palindrome
def check_if_palindrome(a: str) -> bool:
    # setting of two pointers
    i, j = 0, len(a) - 1
    while i < j:
        if a[i] != a[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


if __name__ == "__main__":
    # scanning the string from user
    string = input("Enter the string: ")

    # Calling function to check the palindrome
    result = check_if_palindrome(string)

    # printing the conclusion
    if result:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

