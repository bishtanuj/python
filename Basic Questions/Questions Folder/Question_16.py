# Write a program to print first 5 even numbers using break statement

print("First 5 even numbers: ")
for i in range(100):
    if i % 2 == 0:
        print(i, end=" ")
        if i > 6:
            break

 
# OUTPUT
# First 5 even numbers: 
# 0 2 4 6 8 
