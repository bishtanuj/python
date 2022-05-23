# Write a program to print fibonacci series by taking range from user

limit = int(input("Enter the range of Fibonacci: "))
x, y = 0, 1
print(x, end=" ")
print(y, end=" ")
for i in range(0, limit-2):
  z = x + y
  print(z, end=" ")
  temp = x
  x = y
  y = z
  
  
# # Output
# Enter the range of Fibonacci: 5
# 0 1 1 2 3 
