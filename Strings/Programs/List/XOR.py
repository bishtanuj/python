# Program to compute the xor of two strings

def compute_xor(str1: str, str2: str) -> str:
    result = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            result += '0'
        else:
            result += '1'
    return result


if __name__ == '__main__':
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")
    print(f"XOR of {string1} & {string2}: {compute_xor(string1, string2)}")

'''
OUTPUT:
Enter first string: 11011
Enter second string: 00110
XOR of 11011 & 00110: 11101
'''
