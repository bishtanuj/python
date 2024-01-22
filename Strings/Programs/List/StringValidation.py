"""
Program to check if a string is composed of alphabetical characters, alphanumeric characters,
digits, lower characters and upper characters
"""

"""
Definition and Usage:
1. any()
    The any() function returns True if any item in an iterable are true, otherwise it returns False.
    If the iterable object is empty, the any() function will return False.
2. isalnum()
    This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
3. isalpha()
    This method checks if all the characters of a string are alphabetical (a-z and A-Z).
4. isdigit()
    This method checks if all the characters of a string are digits (0-9).
5. islower()
    This method checks if all the characters of a string are lowercase characters (a-z).
6. isupper()
    This method checks if all the characters of a string are uppercase characters (A-Z).
"""

if __name__ == '__main__':
    string = input("Enter the string: ")
    print(f"String contains alphanumeric characters: {any(letter.isalnum() for letter in string)}")
    print(f"String contains alphabetical characters: {any(letter.isalpha() for letter in string)}")
    print(f"String contains digits: {any(letter.isdigit() for letter in string)}")
    print(f"String contains lower alphabetical characters: {any(letter.islower() for letter in string)}")
    print(f"String contains upper alphabetical characters: {any(letter.isupper() for letter in string)}")


"""
OUTPUT:
Enter the string: qA2
String contains alphanumeric characters: True
String contains alphabetical characters: True
String contains digits: True
String contains lower alphabetical characters: True
String contains upper alphabetical characters: True
"""
