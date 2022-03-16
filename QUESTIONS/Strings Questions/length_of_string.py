# Program to compute the length of the string

# string = input("Enter a string: ")
# print(len(string))


def length_of_string(str1):
    count = 0
    for char in str1:
        count += 1

    print("Length of string:", count)


if __name__ == '__main__':
    string = input("Enter a string: ")
    length_of_string(string)
