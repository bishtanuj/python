# Program to check whether the number is prime or not

# function to check prime
def check_prime(num: int) -> bool:
    if num < 2:
        return False
    else:
        for i in range(2, num//2 + 1):
            if num % i == 0:
                return False
    return True


# driver
if __name__ == '__main__':
    number = int(input("Enter the number: "))
    if check_prime(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


"""
OUTPUT 1:
Enter the number: 12
12 is not a prime number

OUTPUT 2:
Enter the number: 71
71 is a prime number
"""
