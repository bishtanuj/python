# Program to find whether the number is odd or even

# funtion to check a number
def check_odd_even(num: int) -> bool:
  return True if num % 2 == 0 else False


# driver function
if __name__ == "__main__":
  # Scan the number from user
  number = int(input("Enter the number: "))

  # call function to check the number and saves the output in "result" variable
  result = check_odd_even(number)

  # Print the conclusion
  if result:
    print(f"{number} is an even number")
  else:
    print(f"{number} is an odd number")



'''
OUTPUT:
Enter the number: 269
269 is an odd number
'''
