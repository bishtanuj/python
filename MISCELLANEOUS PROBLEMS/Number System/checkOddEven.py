# Program to check whether the number is odd or even

def checkOddEven(num: int) -> bool:
  return True if num % 2 == 0 else False


if __name__ == "__main__":
  num = int(input("Enter the number: "))
  result = checkOddEven(num)
  print(f"{num} is even") if result else print(f"{num} is odd")

