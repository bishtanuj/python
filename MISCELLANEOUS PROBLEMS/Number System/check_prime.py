def checkPrime(num: int) -> bool:
    temp = 0
    if num == 0 or num == 1:
        temp = 1
    else:
        for i in range(2, num//2 + 1):
            if num % i == 0:
                temp = 1
                break
    
    if temp == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    number = int(input("Enter the number: "))
    result = checkPrime(number)
    if result:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
