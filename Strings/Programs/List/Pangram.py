"""
A pangram is a string that contains every letter of the alphabet.

Program to check whether the given string is pangram or not.
"""


def check_pangram(string: str) -> str:
    set_string = set(string.lower().replace(" ", ""))
    if len(set_string) == 26:
        return 'a pangram'
    else:
        return 'not a pangram'


if __name__ == '__main__':
    sentence = input("Enter the string: ")
    print(f"The given sting is {check_pangram(sentence)}")


'''
OUTPUT:
Enter the string: We promptly judged antique ivory buckles for the next prize
The given sting is a pangram

OUTPUT:
Enter the string: We promptly judged antique ivory buckles for the prize
The given sting is not a pangram
'''
