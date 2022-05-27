# Write a program to print the factorial of a number using user defined funciton

def factorial(n):
  fact = 1
  if n == 0:
    return fact
  elif n > 0:
    i = n
    while i > 0:
      fact = fact * i
      i -= 1
    return fact
  

if __name__ == '__main__':
  num = int(input("Enter a number: "))
  if num < 0:
    print("Kindly enter a positive number!!")
  else:
    result = factorial(num)
    print("Factorial:", result)
 

# # OUTPUT:
# Enter a number: 5
# Factorial:  120

# OUTPUT:
# Enter a number: 0
# Factorial:  1
  
# OUTPUT:  
# Enter a number: -2
# Kindly enter a positive number!!
