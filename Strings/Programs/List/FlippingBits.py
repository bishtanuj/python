# Program to flip all the bits of 32-bit unsigned integers i.e., 0 -> 1 and 1 -> 0 and return the decimal number of the result
"""
Example:
    n = 9
    9 = 1001
    as we are working with 32-bits so:
    00000000000000000000000000001001 = 9
    11111111111111111111111111110110 = 4294967286
    return 4294967286
"""


def flipping_bits(n: int) -> int:
    binary = bin(n).replace("0b", "")
    required_zero = 32 - len(binary)
    binary32 = ""
    for i in range(required_zero):
        binary32 += '0'
    binary32 += binary
    binary32 = binary32.replace("0", "2")
    binary32 = binary32.replace("1", "0")
    binary32 = binary32.replace("2", "1")

    return int(binary32, 2)


if __name__ == '__main__':
    number = int(input("Enter the number: "))
    print(f"Decimal number after flipping all the bits of number: {flipping_bits(number)}")
